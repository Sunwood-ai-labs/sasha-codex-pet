# Compatibility / 対応状況

## Package format

This package uses v2: 1536×2288 pixels, 8×11 cells, 192×208 pixels per cell, 73 populated frames. `spriteVersionNumber` is `2`. The first nine rows are standard animations; rows 9–10 hold sixteen gaze directions.

The Codex desktop application implementation inspected on 2026-10-04 (Windows, version 26.930.3930.0) supports the v2 field and layout. The five manifest fields match the package prepared on that desktop. The older public hatch-pet-skill examples describe v1 (1536×1872, nine rows), so those examples alone are not evidence that an older app can load this package.

## Verification status

- Exact public WebP/PNG geometry and transparency: validated
- Public WebP and PNG decoded RGBA equality: validated
- Nine animation states, 73 frames, sixteen gaze directions and loop joins: reviewed frame-by-frame and against timing settings; no missing/clipped frames or major face/limb breakdown found
- Direction classification: three independent reviewers; no unresolved classification, which does not establish smooth transitions
- White/black backgrounds: reviewed for visible green residue and white matte
- Offline comparison with all nine bundled pets at a common 112px display size: basic occupancy, grounding, alpha edges, clipping and state/gaze order checked; frame counts and configured cycle timing match the common specification. This does not resolve the continuity and readability issues below
- Normal-speed continuous playback: not watched; observations are based on frames and timing settings
- Native desktop selection, actual Codex on-screen display, pointer following and state switching: not verified
- Cross-platform runtime compatibility: not independently tested

## Known animation limitations

1. Jump to idle: hair width narrows abruptly at the transition
2. Gaze 157.5° to 180°: the head/hair outline jumps. Earlier direction review accepted the pose classification and noted stable shoes and torso; the later detailed review still identified this visible continuity issue
3. Idle: the configured closed-eye hold is about 1.5 seconds, based on frame/timing inspection rather than measured normal-speed playback
4. State readability: active work, waiting for input and review are hard to distinguish; failure can look like a bow. Equivalent expressive quality to bundled pets is not claimed

These are known issues in the distributed artwork, not fixes delivered by the documentation update. Frame inspection, configured timing and technical preflight do not establish a full animation-quality pass.

Do not claim successful desktop installation until the actual app has loaded this exact public asset. File validation does not substitute for runtime testing.

## 日本語

このパッケージは11行のv2形式です。準備時に確認したWindows版26.930.3930.0の実装はv2を扱えますが、公開されている旧9行形式の例だけを根拠に、古い版での対応を保証しないでください。

公開ファイルの寸法・透過・画素一致、白黒背景での輪郭を検証済みです。9状態・73コマ・16方向・ループのつなぎ目を、各コマと再生設定から確認し、コマの欠落・切れや顔・手足の重大な破綻は見つかりませんでした。方向判定は独立した3名が確認しましたが、方向を判別できることと、つながりが滑らかなことは別です。組み込み9種との112px表示でのオフライン比較では、基本的な占有率・接地・透過縁・切れ・状態と視線の順序を確認しました。コマ数と設定上の再生周期も共通仕様に一致しています。

現行素材には、次の課題が残っています。

1. ジャンプから待機へ戻る際、髪の幅が急に細くなる
2. 視線157.5°から180°の間で、頭・髪の輪郭が跳ねる。先の方向レビューではポーズの方向判定と靴・胴体の安定性を確認しましたが、その後の詳細レビューで輪郭の連続性の課題が指摘されました
3. 待機中の閉じ目が、再生設定上は約1.5秒続く。通常速度の実再生を計測した値ではありません
4. 作業中・入力待ち・確認の区別が弱く、失敗がお辞儀に見えることがある。組み込みペットと同等の表現品質とは断定していません

今回の文書更新で画像を修正したわけではありません。通常速度での連続再生の実視聴、Codexでの選択・実画面表示・ポインター追従・状態切替、他OSでの動作は未確認です。コマ・設定・技術的な事前検査の確認を、アニメーション品質の全面合格とは扱っていません。比較に使った他のペット画像は同梱していません。
