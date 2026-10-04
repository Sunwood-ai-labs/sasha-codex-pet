# Compatibility / 対応状況

## Package format

This package uses v2: 1536×2288 pixels, 8×11 cells, 192×208 pixels per cell, 73 populated frames. `spriteVersionNumber` is `2`. The first nine rows are standard animations; rows 9–10 hold sixteen gaze directions.

The Codex desktop application implementation inspected on 2026-10-04 (Windows, version 26.930.3930.0) supports the v2 field and layout. The five manifest fields match the package prepared on that desktop. The older public hatch-pet-skill examples describe v1 (1536×1872, nine rows), so those examples alone are not evidence that an older app can load this package.

## Verification status

- Exact public WebP/PNG geometry and transparency: validated
- Public WebP and PNG decoded RGBA equality: validated
- Nine animation states and sixteen gaze directions: reviewed
- Direction checks: three independent reviewers; no unresolved direction classification
- White/black backgrounds: reviewed for visible green residue and white matte
- Offline comparison with all nine bundled pets at a common 112px display size: no clear break in occupancy, grounding, alpha edges, clipping, left/right gait, jump or gaze order; frame counts and cycle timing match the common specification
- State readability: idle, active work, review and failure are more restrained than some bundled pets; equivalent expressive quality is not claimed
- Native desktop selection, on-screen playback, following and state switching: not verified
- Cross-platform runtime compatibility: not independently tested

The boundary between the last down-right pose and the centered downward pose received additional sequential-frame review. The change was accepted as a natural head bow with stable shoes and torso. That independent review inspected extracted frames, not real-time continuous playback.

Do not claim successful desktop installation until the actual app has loaded this exact public asset. File validation does not substitute for runtime testing.

## 日本語

このパッケージは11行のv2形式です。準備時に確認したWindows版26.930.3930.0の実装はv2を扱えますが、公開されている旧9行形式の例だけを根拠に、古い版での対応を保証しないでください。

公開ファイルの寸法・透過・画素一致、9状態・16方向、白黒背景での輪郭を検証済みです。方向判定は独立した3名が確認しました。組み込み9種との同じ112px表示でのオフライン比較では、占有率・接地・透過縁・切れ・左右走行・ジャンプ・視線順序に明確な破綻はありませんでした。コマ数と再生周期も共通仕様に一致しています。

待機・作業中・確認・失敗の変化は比較対象の一部より控えめで、同等の表現品質とは断定していません。ネイティブアプリでの選択・実表示・追従・状態切替、他OSでの動作は未確認です。追加の境界レビューは連続フレームの実見であり、実時間再生の確認ではありません。比較に使った他のペット画像は同梱していません。
