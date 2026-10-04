# Installation / 導入ガイド

Use a v2-capable Codex desktop build. Read [compatibility](COMPATIBILITY.md) first. The commands below only copy the package; they do not launch software, grant permissions or switch the active pet.

Run them from the extracted repository directory. If `sasha` already exists, stop and make a backup before deliberately updating it. Never overwrite a different pet.

## Windows PowerShell

```powershell
$CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$Target = Join-Path $CodexHome 'pets/sasha'
if (Test-Path $Target) { throw 'Sasha already exists. Back it up before updating.' }
New-Item -ItemType Directory -Path $Target -Force | Out-Null
Copy-Item './pet.json', './spritesheet.webp' -Destination $Target
```

## macOS / Linux shell

```sh
target="${CODEX_HOME:-$HOME/.codex}/pets/sasha"
if [ -e "$target" ]; then
  printf '%s\n' 'Sasha already exists. Back it up before updating.'
  exit 1
fi
mkdir -p "$target"
cp pet.json spritesheet.webp "$target/"
```

Open the app's pet selection interface and choose Sasha when you want to activate her. If the package is not listed, check the Codex-home directory, the two filenames and v2 support. Follow the app's own refresh/restart guidance; don't edit unrelated configuration.

## PNG alternative

For a loader that supports the same v2 layout but needs PNG, copy `assets/spritesheet.png` beside `pet.json` and change only `spritesheetPath` to `spritesheet.png`. Both distributed formats decode to the same pixels. Keep `spriteVersionNumber` equal to `2`.

## 日本語

上のコマンドは展開したリポジトリの中で実行します。`CODEX_HOME` が設定されていればその場所を、未設定ならホーム内の `.codex` を使います。既存の `sasha` があると停止します。意図して更新する前にバックアップしてください。

コピー後、有効にしたい場合はアプリのペット選択画面でサーシャを選びます。表示されない場合は配置場所・2つのファイル名・v2対応を確認してください。関係のない設定を変更しないでください。

PNGを使用する場合は `assets/spritesheet.png` を `pet.json` と同じ場所へコピーし、`spritesheetPath` だけを `spritesheet.png` に変更します。`spriteVersionNumber` は `2` のままです。
