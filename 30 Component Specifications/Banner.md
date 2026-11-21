---
title: Banner
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, communication, banner, live-region]
related: ["[[Snackbar]]", "[[Notifications]]", "[[Error States]]", "[[Dialog]]", "[[Button]]", "[[Icon Button]]", "[[Divider]]", "[[Tooltip]]", "[[Panel and Surface]]", "[[Colour Roles]]", "[[Elevation]]", "[[Shape]]", "[[Typography]]", "[[Motion]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]", "[[Button]]"]
---

# Banner

> [!info] Summary
> A persistent, in-flow message at the top of a window or a pane about a state that needs the user's attention, with one or two actions and a way to dismiss it. Counterpart: the Material Design banner, which the current Material Design 3 specification no longer lists; the token source is [Material Web banner tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-banner.scss). Source of truth in code: see Status in code.

## Purpose

Tell the user about a condition that stays true until they act: a file changed on disk, the connection is lost, a license expires. Unlike a [[Snackbar]] it does not disappear by itself and it takes room in the layout.

## When to use and not

- Use when: the condition persists, concerns the whole window or pane, needs a decision or acknowledgement, and the user can keep working meanwhile.
- Do not use when: the message is brief feedback on something the user just did (use [[Snackbar]]); work must stop until the user decides (use [[Dialog]]); the problem belongs to one field (inline error text); there are many messages (use a list or a problems panel).

## Anatomy

1. Container: a full-width rectangle in the layout, above the content it concerns.
2. Leading icon (optional but recommended for severity): 24 dp.
3. Supporting text: one to three lines, `body_medium`.
4. Actions: zero to two text buttons at the end; the first is the primary resolution (Reload), the second the alternative (Keep mine).
5. Dismiss control (optional): an icon button at the end.
6. Divider (optional): a 1 dp rule at the bottom edge separating the banner from the content.

## Variants

| Variant | Use | Container | Icon and text | Live behaviour |
|---|---|---|---|---|
| Info | a state worth knowing | `surface_container_low` | `on_surface_variant` text, `primary` actions | role `status`, polite |
| Warning | something may be lost | `tertiary_container` | `on_tertiary_container` | role `alert`, assertive only when the banner asks for a decision (see Accessibility) |
| Error | an operation failed or a service is down | `error_container` | `on_error_container` | role `alert`, assertive when it asks for a decision, else polite |

The three variants are a Tesserae set built on MD3 roles. Material Web has one baseline container (`surface_container_low`, level 1, shape `none`) and a newer standard (`surface_container`) and vibrant (`primary_container`) pair in the Expressive-era tokens ([banners](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-banners.scss)); the vibrant pair is not adopted here (see Deviations).

## States

| State | Visual change | Token values |
|---|---|---|
| Shown | static | per variant |
| Action hover, focus, pressed | state layer in the action's colour at 8, 10 and 10 percent | [[ADR-0009 State layer percentages]] |
| Action keyboard focus | focus ring 3 dp, 2 dp offset | [[Focus Ring]] |
| Dismissing | height collapses to 0 over 200 ms (`short4`), the content below moves up | see Motion |
| Disabled action | label 38 percent `on_surface` (an action that cannot run now) | [[State Layers]] |

## Tokens used

| Part | Token | Value |
|---|---|---|
| Container (info) | `md.comp.banner.container.color`, `container.elevation`, `container.shape` | `surface_container_low`, level 1 (1 dp), `none` |
| Supporting text | `supporting-text.*` | `body_medium` 14/20, `on_surface_variant` |
| Action label | `action.label-text.*` | `label_large` 14/20, 500, `primary` |
| Divider | `divider-height`, `divider-color` | 1 dp, `surface_variant` (Tesserae: `outline_variant`, see [[Divider]]) |
| Image size (with image) | `with-image-image-size` | 40 dp, shape `full` (not adopted) |
| Heights (desktop) | `desktop-with-single-line-container-height`, `desktop-with-two-lines-with-image-container-height`, `desktop-with-three-lines-container-height` | 52, 72, 90 dp |

Source: [Material Web banner tokens, latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-banner.scss), read 2026-11-21. Warning and error container pairs from [[Colour Roles]]: `tertiary_container` with `on_tertiary_container` and `error_container` with `on_error_container`; their ratios are checked by AC-BNR-8.

## Sizing and density

| Level | Single-line minimum height | Vertical padding | Horizontal padding | Gap between parts | Action button height |
|---|---|---|---|---|---|
| default | 52 | 6 | 16 | 8 | 40 |
| compact | 44 | 6 | 12 | 8 | 32 |
| dense | 36 | 4 | 8 | 4 | 28 |

- The default 52 dp is the Material Web desktop single-line height (40 dp button plus 6 dp above and below). Compact and dense are the button height at that level plus the padding, a Tesserae choice #needs-verification-as-design-choice.
- Two lines grow the height by one line (20 dp); three lines are the maximum.
- Icon 24 dp at default and 20 dp at compact and dense ([[Icon Button]] icon rule).
- The banner is as wide as the area it heads. Hit areas: actions and dismiss at least 24 dp by 24 dp at every level (the button heights satisfy it); 48 dp hit area in touch contexts.

## Layout and overflow

- The banner is in the layout flow, not an overlay: it pushes the content below it down and the content region shrinks; scroll position of the content below does not change ([[10 Layout Overflow and Scrolling]]). It is not scrolled with the content: it stays at the top of its area.
- Text is vertically centred against the icon and the actions for one line within 1 px; for 2 and 3 lines the icon and actions align to the first line's centre.
- Text wraps at word boundaries to at most 3 lines, then ends with an ellipsis; the full text is the accessible name. Actions never wrap: below the width where text plus actions fit in 3 lines, the actions move onto their own row below the text, end-aligned.
- Minimum width where one line of text and two actions fit: 480 dp; narrower, the stacked layout is used.
- Right-to-left: icon at the right, actions at the left.

## Behaviour

- One at a time. At most one banner is visible per area (window, or pane). Further banners queue by severity (error, then warning, then info), then by age. A banner with an identity (`disk-change:file.tdl`) replaces a queued or visible banner with the same identity. When several conditions of the same kind exist, one banner states the count ("3 files changed on disk") and its action works on all. The queue length is not shown; the project may show "1 of 3" in the text.
- Persistence: a banner stays until the user takes an action, dismisses it or the condition ends (the project removes it). It never times out. A banner for a recoverable condition is dismissible; one for a condition that blocks work (no dismissal) carries an action that resolves it.
- Pointer: actions and dismiss follow [[Button]] behaviour. A press elsewhere does nothing to the banner.
- Keyboard: a banner takes no focus when it appears. It sits in the Tab order at its place in the layout (top of its area, before the content) so a keyboard user reaches it with Shift+Tab from the content or with Tab from the top. The chord Alt+Shift+B moves focus to the current banner's first action ([[ADR-0019 Banner and snackbar focus chords]]). Alt+Shift+B is a proposed default: a collision check against the shell's shortcut map and the application's own map is required before a project adopts it, and the result is recorded. Enter or Space runs an action; Escape on a focused banner dismisses it if dismissible and returns focus to where it came from.
- Touch: actions and dismiss have 48 dp hit areas.
- After an action the banner closes (when the action resolves the condition) and focus returns to the control that had it before the banner was focused; if there was none, to the first focusable control of the content below.

## Tooltip and overlay behaviour

A banner shows no tooltip of its own ([[ADR-0004 Tooltip rule]]); its dismiss icon button has the tooltip "Dismiss" and an icon-only action has its label as tooltip. It opens no overlay and draws no scrim. A dialog or menu opened from an action is a normal overlay with focus return to the action.

## Motion

Appear: height expands from 0 to its full height over 200 ms (`short4`) with `standard`, content below follows; text and icons fade in over 150 ms (`short3`). Dismiss: height collapses over 150 ms with `standard_accelerate` (exit shorter than enter, [[Motion]] rule 3). With reduced motion the banner appears and disappears in one frame ([[Motion]], rule 4). The layout shift happens once, not each frame, for assistive technology (no repeated re-announce).

## Accessibility

- Live region: the banner announces when it appears, by the live region of its text, which must enter the tree when the banner appears.
  - Polite (role `status`, `live` polite): info, and warnings and errors that do not ask for a decision now.
  - Assertive (role `alert`, `live` assertive): only a banner that asks the user for a decision that cannot wait (file changed on disk with Reload or Keep mine; unsaved changes at risk). One assertive announcement per banner, once, not on each text change; a changed count updates the text politely.
  - Rationale: [[Accessibility Rules]] AR-24 and [WCAG 4.1.3](https://www.w3.org/TR/WCAG22/#status-messages): assertive interrupts and is reserved for what must be acted on.
- Role of the container: `region` named by the summary ("File changed on disk") so a user can find it with landmark navigation; tess-ui uses role `group` with a name. The text node carries the live setting.
- Name: the message text. Actions are buttons named by their labels; dismiss is "Dismiss". Icon is decorative and hidden unless it is the only severity cue (then named "Warning" or "Error"): colour is not the only carrier of severity ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).
- Contrast: text and icon on the container at least 4.5 to 1 and 3 to 1 for the icon; actions at least 4.5 to 1 on the container.
- Keys: Tab order as above; Alt+Shift+B moves focus to the banner (proposed default, [[ADR-0019 Banner and snackbar focus chords]]); Enter and Space activate; Escape dismisses a dismissible banner.
- A banner never moves focus on appearance.

## Dark and light

Roles only. `error_container` and `tertiary_container` are dark tones in dark theme with light `on_*` text; the severity is also shown by the icon. High contrast adds a 1 dp `outline` stroke and no elevation shadow.

## Defaults

Info variant, full width, at the top of the window area it concerns, 24 dp icon, text `body_medium`, one text-button action, not dismissible unless the caller sets it, no timeout, polite live region.

## Acceptance criteria

- [ ] AC-BNR-1 (token test): info container `surface_container_low` with elevation level 1 and shape `none`; warning `tertiary_container`; error `error_container`; text `body_medium`; action `label_large` in `primary` (info) or the variant's `on_*` role. Pass: all are role references with these values.
- [ ] AC-BNR-2 (geometry check): at default, compact and dense a single-line banner is 52, 44 and 36 dp high; two lines add 20 dp; the button heights are 40, 32 and 28 dp; horizontal padding 16, 12 and 8 dp; no padding literal outside {0, 2, 4, 8, 12, 16, 24, 32, 48}. Pass: equal within 0.5 dp.
- [ ] AC-BNR-3 (geometry check): the banner takes layout room: the content below starts at the banner's bottom edge and the content's height decreases by the banner height; removing the banner restores it. Pass: content bounds equal in both cases.
- [ ] AC-BNR-4 (scripted input): show three banners (info, error, warning): one is visible, the error first; dismissing it shows the warning, then the info; a banner with the same identity as the visible one replaces it without a second node. Pass: visible count at most 1 on every frame and order equal.
- [ ] AC-BNR-5 (AT tree assertion): info: live `polite`, role `status` on the text node; a banner that asks for a decision (disk change): role `alert`, live `assertive`; the container has a role of `region` or `group` with the summary as its name; each action is a button with a name; the dismiss button is named "Dismiss". Pass: all equal.
- [ ] AC-BNR-6 (scripted input): a banner appearing raises exactly one announcement with the politeness of its variant; changing its text raises at most one polite update and no assertive one; its disappearance raises none. Pass: counts and politeness equal.
- [ ] AC-BNR-7 (scripted input): the banner takes no focus on appearance (the focus owner is unchanged); Tab from the top of the area reaches the first action; the chord Alt+Shift+B (proposed default, [[ADR-0019 Banner and snackbar focus chords]]) moves focus to it; Enter runs it; focus then returns to the control that had it before. Pass: owners equal at each step.
- [ ] AC-BNR-8 (contrast script): text on the container at least 4.5 to 1 and icon at least 3 to 1, for the three variants, light, dark and high contrast; the action label on the container at least 4.5 to 1. Pass: no ratio below the limit.
- [ ] AC-BNR-9 (scripted input): a banner stays with no timeout for 60 s (frame sampling); a dismissible banner closes on the dismiss control and on Escape while it has focus; a non-dismissible banner has no dismiss control and ignores Escape. Pass: states equal.
- [ ] AC-BNR-10 (geometry check): below 480 dp wide the actions are on their own row below the text, end-aligned; at 480 dp and above they are at the end of the text row; text never exceeds 3 lines. Pass: bounds equal.
- [ ] AC-BNR-11 (scripted input): with reduced motion on, show and dismiss change the layout in one frame; with it off the height animation takes 200 ms in and 150 ms out (within 2 frames). Pass: frame counts equal.
- [ ] AC-BNR-12 (review): the severity of every banner is also given by an icon or a word (greyscale render differs between info and error). Pass: reviewer finds none that differs by colour only.
- [ ] AC-BNR-13 (review): a project that adopts Alt+Shift+B has run the collision check against the shell's shortcut map and each application's own map and records the result and any replacement chord ([[ADR-0019 Banner and snackbar focus chords]]). Pass: the record exists and lists no collision, or names the replacement.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | none as a shipped view; the config app builds one by hand: `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`disk_banner`, `disk_reload_button`, `disk_keep_button`), styled inline | absent as a component; the hand-built banner partly meets: in flow, `tertiary_container` with `on_tertiary_container`, role `group` named "File changed on disk", assertive live on the text, a filled "Reload" and an outlined "Keep mine" button, 8 dp padding, 18 dp icon (AC-BNR-3, AC-BNR-5 partly meet by reading); no density-level height (AC-BNR-2 fails: padding 8 and extra-small buttons), icon 18 dp is not 24 or 20, no dismiss, no queue and no identity (AC-BNR-4 fails), no Escape or chord (AC-BNR-7, AC-BNR-9 fail), no height animation (AC-BNR-11 fails), actions are filled and outlined buttons, not text buttons, a deviation from the token |
| tess-shell | none | absent: no banner; modules show a hidden state and the Launcher announces results; a persistent notice is not specified in v1 |
| tre | `tre:docs/guide/accessibility.md` (`live`, `announce`) | not applicable: the engine gives the live region; the banner is toolkit work |

Evidence: [[Gaps and Contradictions]] (hand-built disk-change banner, `Main_View.tdl` lines 974 to 1000; no banner in the toolkit).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui (config app) | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`disk_banner`) | exists as a one-off, not reusable |
| tess-ui (toolkit) | none | absent: candidate request for a `Banner` view |
| tess-shell | none | absent |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A banner component is specified although the current MD3 specification lists none | desktop apps need a persistent in-flow message (disk change, offline); Material Web keeps tokens for it | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Severity variants `tertiary_container` and `error_container` | MD3 has one container; severity needs a non-text cue and a role per level | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Heights 52, 44, 36 for single line | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Assertive live region allowed for a decision banner only | one-time interrupt for what must be acted on; MD3 gives no accessibility rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Vibrant and standard container pairs of the newer tokens not adopted | Expressive-era; adopt by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Divider colour `outline_variant` instead of `surface_variant` | `surface_variant` is a legacy role in the vault ([[Colour Roles]]) | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- [Material Web banner tokens (latest)](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-banner.scss): desktop heights 52, 72 (two lines with image), 90 (three lines), mobile 54, 112, 120; divider 1 px; container `surface-container-low`, elevation `level1`, shape `corner-none`; action `primary` `label-large`; text `on-surface-variant` `body-medium`. Verified 2026-11-21.
- [Material Web banners tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-banners.scss) and [banners-basic](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-banners-basic.scss): standard `surface-container`, vibrant `primary-container`, height 56 and two lines 64, shape round `corner-extra-large`; not adopted.
- [Material Components Android Banner](https://github.com/material-components/material-components-android/blob/master/docs/components/Banner.md): "yet to be completed". No guidance on lifetime or one-at-a-time rules exists in the tools-readable sources: those rules are Tesserae choices.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.3, 1.4.11, 2.1.1, 4.1.3; [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) `alert`, `status`, `region`.
- Code: `tess-ui:apps/shell_config/.../Main_View.tdl`; [[Accessibility Rules]] AR-24.
- The m3.material.io banner page is gone or not readable; whether current Material Design 3 retired the banner is #needs-verification.
