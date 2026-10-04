"""Check the public distribution; not a replacement for animation/visual QA."""
from __future__ import annotations

import hashlib
import json
import re
import struct
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def png_chunks(data: bytes) -> list[str]:
    require(data[:8] == b"\x89PNG\r\n\x1a\n", "Invalid PNG signature")
    chunks = []
    offset = 8
    while offset + 12 <= len(data):
        size = struct.unpack(">I", data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8].decode("ascii")
        chunks.append(kind)
        offset += size + 12
    require(offset == len(data), "Unexpected PNG trailing bytes")
    return chunks


def webp_chunks(data: bytes) -> list[str]:
    require(data[:4] == b"RIFF" and data[8:12] == b"WEBP", "Invalid WebP container")
    require(struct.unpack("<I", data[4:8])[0] + 8 == len(data), "Unexpected WebP trailing bytes")
    chunks = []
    offset = 12
    while offset + 8 <= len(data):
        kind = data[offset:offset + 4].decode("ascii")
        size = struct.unpack("<I", data[offset + 4:offset + 8])[0]
        chunks.append(kind)
        offset += 8 + size + size % 2
    return chunks


def check_image(path: Path) -> None:
    relative = path.relative_to(ROOT).as_posix()
    data = path.read_bytes()
    with Image.open(path) as image:
        require(not any(key in image.info for key in ("exif", "xmp", "comment", "icc_profile", "XML:com.adobe.xmp")), f"Unexpected metadata: {relative}")
        if path.suffix == ".png":
            require(set(png_chunks(data)) <= {"IHDR", "IDAT", "IEND"}, f"Ancillary PNG metadata: {relative}")
        elif path.suffix == ".webp":
            require(set(webp_chunks(data)) <= {"VP8X", "VP8L", "VP8 ", "ALPH"}, f"Unexpected WebP metadata: {relative}")
        elif path.suffix == ".gif":
            extension = image.info.get("extension")
            require(not extension or extension[0] == b"NETSCAPE2.0", f"Unexpected GIF application extension: {relative}")


def check_atlas(path: Path) -> bytes:
    with Image.open(path) as opened:
        require(opened.mode == "RGBA", f"Missing native alpha: {path.name}")
        image = opened.convert("RGBA")
    require(image.size == (1536, 2288), f"Wrong v2 dimensions: {path.name}")
    if image.size != (1536, 2288):
        return image.tobytes()
    require(0 < path.stat().st_size <= 20 * 1024 * 1024, f"Invalid asset size: {path.name}")
    for row, count in enumerate(COUNTS):
        for col in range(8):
            cell = image.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            alpha = cell.getchannel("A")
            used = col < count
            occupied = sum(alpha.histogram()[1:])
            require(occupied > 128 if used else occupied == 0, f"Incorrect cell occupancy: row {row}, column {col}")
            if used:
                require(alpha.getextrema()[0] == 0, f"Opaque cell background: row {row}, column {col}")
                require(all(alpha.getpixel((x, y)) == 0 for x in range(192) for y in (0, 207)), f"Vertical cell bleed: {row},{col}")
                require(all(alpha.getpixel((x, y)) == 0 for y in range(208) for x in (0, 191)), f"Horizontal cell bleed: {row},{col}")
    for red, green, blue, alpha in image.get_flattened_data():
        if alpha == 0 and (red or green or blue):
            ERRORS.append(f"Hidden RGB under zero alpha: {path.name}")
            break
    return image.tobytes()


def main() -> int:
    manifest = json.loads((ROOT / "pet.json").read_text(encoding="utf-8"))
    require(manifest.get("id") == "sasha", "Wrong pet id")
    require(manifest.get("displayName") == "サーシャ", "Wrong display name")
    require(manifest.get("spriteVersionNumber") == 2, "Wrong sprite version")
    require(manifest.get("spritesheetPath") == "spritesheet.webp", "Unexpected sprite path")
    require((ROOT / manifest.get("spritesheetPath", "missing")).is_file(), "Manifest asset missing")

    assets = json.loads((ROOT / "qa/assets.json").read_text(encoding="utf-8"))
    for record in assets["files"]:
        path = ROOT / record["path"]
        require(path.is_file(), f"Missing asset: {record['path']}")
        if not path.is_file():
            continue
        require(path.stat().st_size == record["bytes"], f"Size mismatch: {record['path']}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"], f"SHA mismatch: {record['path']}")
        if path.suffix in {".png", ".webp", ".gif"}:
            check_image(path)
    webp = check_atlas(ROOT / "spritesheet.webp")
    png = check_atlas(ROOT / "assets/spritesheet.png")
    require(webp == png, "PNG and WebP RGBA pixels differ")
    require(hashlib.sha256(webp).hexdigest() == assets["decoded_rgba_sha256"], "Decoded pixel hash mismatch")

    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)|(?:src|href)=\"([^\"]+)\"")
    for path in ROOT.rglob("*.md"):
        for match in link_pattern.finditer(path.read_text(encoding="utf-8")):
            target = (match.group(1) or match.group(2)).split("#", 1)[0]
            if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            require((path.parent / target).is_file(), f"Broken local link in {path.name}: {target}")
    require((ROOT / "README.md").read_text().count("## ") == (ROOT / "README.ja.md").read_text().count("## "), "README section parity mismatch")
    print(json.dumps({"ok": not ERRORS, "frames": sum(COUNTS), "unused_cells": 88 - sum(COUNTS), "checks": ["manifest", "hashes", "metadata", "v2 geometry", "alpha", "cell boundaries", "lossless format equality", "local links"], "errors": ERRORS}, indent=2))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
