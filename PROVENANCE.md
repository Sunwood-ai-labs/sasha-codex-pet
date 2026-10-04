# Provenance / 出典

## Character and artwork

- Character: Sasha / サーシャ
- Visual source: character references provided by the repository owner
- Production: AI-assisted image generation and background repair; each animation row was generated as a coherent strip
- Transparency: the distributed revision was edited with a transparent background, preserving actual alpha rather than distributing a green-screen background
- Assembly: generated poses were extracted and registered into a v2 atlas; no other pet's artwork was used
- Public export: metadata-free lossless PNG and WebP encoding; decoded RGBA pixels and alpha verified equal to the reviewed artwork

The private reference sheets and production logs are not part of this public package. This is a production account, not a claim of exclusive copyright or a new license grant. See [RIGHTS.md](RIGHTS.md).

## Format references

- [Character Design Images pet package catalog](https://github.com/Sunwood-ai-labs/character-design-images/blob/main/docs/pets.md) — packaging precedent, not a source of redistributed art
- [Codex pet packaging implementation](https://github.com/Sunwood-ai-labs/hatch-pet-skill/blob/main/scripts/package_custom_pet.py) — legacy manifest field names and Codex-home directory convention
- [Legacy desktop sprite contract](https://github.com/Sunwood-ai-labs/hatch-pet-skill/blob/main/references/codex-pet-contract.md) — nine-row format; it does not by itself document the v2 extension
- [Pet overview](https://learn.chatgpt.com/docs/pets) — product terminology and overview

The public legacy examples and this eleven-row v2 package are not interchangeable. See [compatibility details](docs/COMPATIBILITY.md).
