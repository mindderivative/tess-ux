---
title: Video Player
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, content, video, tesserae-only]
related: ["[[Image]]", "[[Image Node]]", "[[Progress Indicator]]", "[[Icon Button]]", "[[Button]]", "[[Slider]]", "[[Tooltip]]", "[[Scrim]]", "[[Colour Roles]]", "[[Shape]]", "[[Typography]]", "[[Motion]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[Icon Button]]", "[[Progress Indicator]]", "[[Scrim]]"]
---

# Video Player

> [!info] Summary
> A picture surface for video frames with transport controls under it: play and pause, elapsed time, a seek slider, total time and mute. Tesserae-only: Material Design 3 treats video as content and has no player component; the spec rests on MD3 controls, [WAI-ARIA slider and button patterns](https://www.w3.org/WAI/ARIA/apg/) and WCAG 2.2 rules for media. Source of truth in code: see Status in code.

## Purpose

Let the user watch and control a video the application decodes and supplies as frames, with the controls and keys a desktop user expects, and with captions and busy state exposed to assistive technology.

## When to use and not

- Use when: the app plays recorded video or an animated sequence and the user must pause, seek and mute.
- Do not use when: the content is a still picture (use [[Image]]); the animation is decorative and short (use [[SVG]] animation or a path animation); only audio plays (use the media module of the shell, a different element).

## Anatomy

1. Stage: a rectangle with a dark background (`scrim` role, black) and rounded corners, clipping the picture.
2. Picture: the current frame, fitted into the stage (`contain` by default).
3. Buffering ring (optional): a circular progress indicator centred over the picture ([[Progress Indicator]]).
4. Caption band (optional): a line of subtitle on a darkened band at the foot of the stage.
5. Controls row under the stage: play and pause icon button, elapsed time, seek slider, total time, mute icon button.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Core (built) | the controls above | decoder-free: the app pushes frames |
| Extended (not built) | fullscreen, playback speed, volume level, poster frame | optional controls with the rules in Behaviour; absent from code today |
| Picture only | thumbnails, previews | stage and picture, no controls row; not interactive |

## States

| State | Visual change | Token values |
|---|---|---|
| Idle, not playing | play icon; picture is the current frame or blank `scrim` | `scrim` stage |
| Playing | pause icon; elapsed time and slider advance | |
| Buffering | ring over the picture; play state unchanged | `primary` ring on `scrim` |
| Ended | play icon; position equals duration | |
| Muted | volume-off icon; label "Unmute" | |
| No duration (live or unknown) | seek slider disabled; total shows `--:--` | slider disabled look, 38 percent |
| Control hover, focus, pressed | state layers per [[Icon Button]] | 8, 10, 10 percent, [[ADR-0009 State layer percentages]] |
| Error (decoder failed) | picture area shows the error glyph and message; controls disabled | see [[Error States]] |

## Tokens used

| Part | Token | Value |
|---|---|---|
| Stage background | `scrim` | #000000 (both schemes) |
| Stage shape | `medium` | 12 dp, children clipped |
| Caption band | `scrim` at 60 percent, text `body_medium`, white | height 40 dp |
| Elapsed and total | `label_medium`, `on_surface_variant` | width 44 dp each |
| Buttons | [[Icon Button]] tokens | icon 24, 20, 20 dp |
| Slider | [[Slider]] tokens | |
| Gap between control row parts | `space.3` | 8 dp |
| Gap between stage and controls | `space.3` | 8 dp |

Caption contrast, computed for this note: white text on `scrim` at 60 percent over a white frame composites to #666666 behind the text, 5.7 to 1; over a black frame 21 to 1. Both exceed 4.5 to 1, so the band is the minimum the spec allows. The caption colour should be the role `inverse_on_surface` or `on_surface` of a dark container rather than the literal #FFFFFF that tess-ui uses #needs-verification.

## Sizing and density

The stage size is the picture size set by the owner (480 by 270 dp default, 16:9). The controls row follows the icon button and slider sizes of the density level ([[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]]).

| Level | Controls row height | Icon button container | Icon | Time label width |
|---|---|---|---|---|
| default | 40 | 40 | 24 | 44 |
| compact | 32 | 32 | 20 | 44 |
| dense | 28 | 28 | 20 | 40 |

- The controls row is as wide as the stage; the slider takes the remaining width, at least 80 dp.
- Minimum player width where the full controls row fits: 280 dp (two 40 dp buttons, two 44 dp labels, 80 dp slider, four 8 dp gaps and padding). Below it the time labels hide and only play, slider and mute remain.
- Hit areas at least 24 dp by 24 dp at every level; the seek slider's thumb hit area is at least 24 dp high even when its track is thinner; 48 dp in a touch context.

## Layout and overflow

- Vertical stack: stage, then controls row, gap 8 dp. The player's height is stage height plus row height plus gap.
- The picture is fitted by `contain`, `cover` or `fill` ([[Image]], fit modes); default `contain`, centred, letterboxed in `scrim`. Frames may change size; the stage size does not change.
- The caption line is one line, centred in the band, ending with an ellipsis at the stage width minus 32 dp; the full caption is the live text for assistive technology (see Accessibility). Two-line captions grow the band to 56 dp (a Tesserae extension #needs-verification).
- Times are `m:ss` below one hour and `h:mm:ss` from 3600 s; the label width fits `h:mm:ss`. Text vertical centring in the row within 1 px.
- A window narrower than the player: the player is scaled to the container width with the same ratio (the stage width equals the container; height follows the ratio of the owner's width and height). A fixed-size player is clipped, never scrolled.

## Behaviour

- Pointer: clicking the play button toggles playing; clicking or dragging on the slider seeks (a drag lands on a multiple of `Step`); clicking the mute button toggles muted. Clicking the picture toggles playing (YouTube-style) #needs-verification-as-design-choice; double-click on the picture enters fullscreen where the extended variant exists.
- Keyboard. Tab and Shift+Tab move between play, slider and mute (the controls row is one focus group with the arrow keys moving between buttons only when focus is on a button; on the slider the arrows seek). Keys on the seek slider: `Space` plays or pauses, `Left` and `Right` move the position by `Step` seconds (default 1), `Home` and `End` go to 0 and to the duration, `Page Up` and `Page Down` move by 10 `Step`s, `M` mutes. When the player (any part) has focus: `K` also plays or pauses, `F` toggles fullscreen and `C` toggles captions where those features exist. A key never acts when focus is in a text field.
- Touch: tap the picture to toggle; the controls have 48 dp hit areas; horizontal drag on the slider seeks.
- Autoplay: `Playing` starts false; a video never starts by itself with sound. A player that autoplays is muted and shows its controls ([WCAG 1.4.2](https://www.w3.org/TR/WCAG22/#audio-control)).
- State ownership: the player owns none of the playing: `Playing`, `Position` and `Muted` are two-way values; the app's decoder follows them and advances `Position`. The app pushes one frame per displayed picture; a frame is dropped when the app is late, never queued.
- Extended controls (when built): volume is a slider of 0 to 100 percent beside the mute button, with `Up` and `Down` changing it by 5 and `M` toggling; playback speed offers 0.5, 0.75, 1, 1.25, 1.5, 2; fullscreen asks the window for a fullscreen layer and Escape leaves it; a poster is shown until the first frame.
- Seeking while buffering keeps the new position and shows the ring.

## Tooltip and overlay behaviour

Each icon button carries a tooltip equal to its name: "Play" or "Pause", "Mute" or "Unmute" ([[ADR-0004 Tooltip rule]]); the player as a whole, the stage and the slider track carry none. The slider may show the target time as a tooltip on pointer hover over the track (time at the pointer position), on the slider only. Overlays: none; fullscreen, when built, is a window or layer state, not an overlay of the player.

## Motion

The video itself is content: its motion is not governed by reduced motion, but it never starts without the user (see Autoplay). Control changes: icon swap play and pause is immediate; state layers per [[State Layers]]; the seek thumb follows the position without easing. The buffering ring is a [[Progress Indicator]] and is still under reduced motion. The caption band appears and disappears in one frame. No flashing content above 3 per second is added by the player ([WCAG 2.3.1](https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold)); video content is the owner's responsibility.

## Accessibility

- Role: `group` named by the player `Label` (default "Video"); the picture surface is `img` with that label when it is informative, otherwise hidden. Controls are real controls: `button` (play and pause; mute), `slider` (seek) with `value`, `value_min` 0, `value_max` the duration and `value_text` "1:05 of 2:05"; the slider's name is "Seek".
- Names: the play button's name is the action "Play" or "Pause" (the name changes with state; no extra `pressed` flag, so the name and flag do not contradict); the mute button is "Mute" or "Unmute". The name starts with its visible or tooltip text ([WCAG 2.5.3](https://www.w3.org/TR/WCAG22/#label-in-name)).
- Captions: the owner supplies caption text for spoken content ([WCAG 1.2.2](https://www.w3.org/TR/WCAG22/#captions-prerecorded)); the player draws it. A caption is not a live region (each line would interrupt the user's own reader); an alternative text track or transcript is the owner's means for blind users ([WCAG 1.2.1, 1.2.3](https://www.w3.org/TR/WCAG22/#audio-only-and-video-only-prerecorded)).
- Announcements: none on play or time updates. Buffering is `busy` on the ring node and on the player group; a long buffering over 3 s announces "Buffering" once, politely; the end of the video announces "Ended" once, politely.
- Pause: the play and pause control is the means of pausing moving content ([WCAG 2.2.2](https://www.w3.org/TR/WCAG22/#pause-stop-hide)); it is reachable in at most one Tab from the player's start.
- Audio: a mute control is present whenever audio plays ([WCAG 1.4.2](https://www.w3.org/TR/WCAG22/#audio-control)).
- Focus: ring 3 dp, 2 dp offset, around each control ([[Focus Ring]]); the focused control is not covered by the caption band or the buffering ring.
- Contrast: time labels `on_surface_variant` on the surface at least 4.5 to 1; icons at least 3 to 1; captions 4.5 to 1.

## Dark and light

The stage is `scrim` black in both schemes; the controls row follows the scheme through roles. The caption band is the same in both.

## Defaults

480 by 270 dp stage, 12 dp corners, `contain`, `Playing` false, `Position` 0, `Duration` 0 (slider disabled), `Muted` false, no buffering ring, no caption, `Step` 1 s, label "Video", no autoplay.

## Acceptance criteria

- [ ] AC-VID-1 (geometry check): the default player is 480 dp wide with a 480 by 270 dp stage; the controls row is 40, 32 and 28 dp high at default, compact and dense; the icon button containers are 40, 32 and 28 dp; gaps are 8 dp; time labels are 44 dp wide (40 dp at dense). Pass: equal within 0.5 dp at scale 1.0 and 2.0.
- [ ] AC-VID-2 (pixel check): the stage is `scrim` black with radius 12 dp and clips its children (the picture corner pixel outside the radius is the background); a 200 by 100 frame in a 480 by 270 stage with `contain` is drawn 480 by 240 centred with 15 dp bands above and below. Pass: pixels and bounds equal.
- [ ] AC-VID-3 (scripted input): focus the seek slider; `Space` toggles `Playing`, `Right` adds `Step`, `Left` subtracts it, `Home` goes to 0, `End` to the duration, `Page Down` adds 10 steps, `M` toggles `Muted`; each key changes exactly one value once. Pass: values and event counts equal.
- [ ] AC-VID-4 (scripted input): Tab visits play, slider and mute once each in order and leaves the player; no key sequence traps focus; with `Duration` 0 the slider is disabled and skipped. Pass: visited sequence equals the expected list.
- [ ] AC-VID-5 (AT tree assertion): the group is named "Video" (or the label); play has the name "Play" while not playing and "Pause" while playing; mute "Mute" or "Unmute"; the slider has role `slider`, name "Seek", `value_min` 0, `value_max` equal to the duration and `value_text` "1:05 of 2:05" at 65 s of 125 s. Pass: all equal.
- [ ] AC-VID-6 (scripted input): `Playing` is false at construction and no frame advances without a user action; an autoplaying configuration starts muted with controls visible. Pass: position equals 0 after 2 s and the muted flag is true in the autoplay case.
- [ ] AC-VID-7 (pixel check): a caption of 200 characters draws on one line with an ellipsis inside a 40 dp band of `scrim` at 60 percent; white text over a white frame measures at least 4.5 to 1 against the composited band. Pass: ellipsis present, ratio at least 4.5.
- [ ] AC-VID-8 (token test): time text shows `m:ss` below 3600 s and `h:mm:ss` from 3600 s (3599 shows `59:59`, 3600 shows `1:00:00`, 7325 shows `2:02:05`). Pass: strings equal.
- [ ] AC-VID-9 (scripted input): setting `Buffering` shows the ring centred on the stage within 1 px, marks the player busy and, after 3 s, raises exactly one polite "Buffering" announcement; clearing it removes the ring and the busy flag. Pass: bounds, flags and announce count equal.
- [ ] AC-VID-10 (scripted input): the ended video announces "Ended" once, politely, and shows the play icon; caption text changes raise no announcement. Pass: announce queue equal.
- [ ] AC-VID-11 (scripted input): each icon button's tooltip text equals its name; the stage and slider track show no tooltip; the slider track shows a time tooltip on hover only. Pass: visible tooltip owners equal.
- [ ] AC-VID-12 (geometry check): every control's hit area is at least 24 by 24 dp (48 in a touch context); the slider thumb hit area is at least 24 dp high. Pass: bounds at or above the limits.
- [ ] AC-VID-13 (scripted input): with reduced motion on or off the ring is still when on and moving when off; play and pause icon swap in one frame in both. Pass: frame diffs equal expectation.
- [ ] AC-VID-14 (scripted input): a window narrower than 280 dp hides the time labels and keeps play, slider and mute; a container narrower than the stage scales the stage to the container width with the same ratio. Pass: node visibility and bounds equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/VideoPlayer_View.tdl`, `tess-ui:src/tess_ui/views/VideoPlayer_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/media.py` (`video`), `tess-ui:docs/components/video.md` | partly meets: 480 by 270 default, stage `scrim`, radius 12 and clipping, `contain` default, play, time, slider, time, mute row with 8 dp gaps and 44 dp labels, Space, arrows and M on the slider, `Playing` default false, buffering ring, caption band 40 dp at 60 percent `scrim`, group role named "Video" (AC-VID-2, AC-VID-3 partly, AC-VID-6, AC-VID-7 partly, AC-VID-9 partly meet by reading, unrun); fails AC-VID-1 (no density levels), AC-VID-3 (no Home, End or Page keys), AC-VID-5 (slider has no `value_text`, name "Seek" present), AC-VID-8 (minutes unbounded: 3600 s shows `60:00`), AC-VID-9 and AC-VID-10 (no announcement), AC-VID-11 (tooltips unmeasured), AC-VID-14 (no narrow layout); no decoder, fullscreen, speeds, volume level or poster; caption colour is the literal `#ffffff` |
| tess-shell | none; the Media module is audio and metadata (`shell-vault:40 Specifications/Modules/Media Module.md`) | absent |
| tre | `tre:docs/reference/properties.md` (Image: `rgba`, `pixel_width`, `pixel_height`; "video is repeated `set(rgba=...)`"), `tre:docs/migrating-0.3.5.md` (`add_video` replaced by an `image` node) | not applicable: no video node and no decoder; the engine draws pushed RGBA frames |

Evidence: [[Gaps and Contradictions]] (Video: decoder, fullscreen, speed, volume, poster).

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/VideoPlayer_View.tdl` | exists, partial; not used by any app or example |
| tre | the [[Image Node]] with repeated `set(rgba=...)` | mechanism |
| tess-shell | none | absent |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A video player is specified; MD3 has none | Tesserae-only element; built from MD3 icon buttons, slider and the scrim | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Controls row follows density levels | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard map (`Space`, `K`, `M`, `Home`, `End`, `Page` keys) | desktop keyboard-first | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltips on icon buttons and on the slider track only | tooltips belong to controls | [[ADR-0004 Tooltip rule]] |
| State layers 8, 10, 10 percent on the controls | accepted state layer values | [[ADR-0009 State layer percentages]] |

## Sources

- WAI-ARIA Authoring Practices: [slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) (arrow keys, `Home`, `End`, `Page Up` and `Page Down`, `value_text`), [button](https://www.w3.org/WAI/ARIA/apg/patterns/button/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.2.1, 1.2.2, 1.2.3, 1.4.2, 2.2.2, 2.3.1, 2.5.3.
- Material Web tokens for icon button (container 40, icon 24) and the scrim role ([[Icon Button]], [[Scrim]]): [md-comp-icon-button](https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192).
- Code: `tess-ui:docs/components/video.md`, `tess-ui:src/tess_ui/views/VideoPlayer_View.tdl`, `tre:docs/reference/properties.md`.
- Not verifiable by tools: any Material Design 3 video guidance (MD3 has none); fullscreen, speed, volume and poster rules are Tesserae choices #needs-verification-as-design-choice; the keys `K`, `F`, `C` follow common web players and are not from a standard.
