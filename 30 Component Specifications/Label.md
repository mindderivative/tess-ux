---
title: Label
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, text]
related: ["[[Text]]", "[[Text Box]]", "[[Marquee Text]]", "[[Text Field]]", "[[Form Row]]", "[[Text Truncation]]", "[[Disabled State]]", "[[Owner Feedback 2026-11-20]]", "[[Accessibility Announcements]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Label

> [!info] Summary
> A Label is a single line of read-only text, a thin standard module over the [[Text]] block. The nearest Material Design 3 reference is the [type scale](https://m3.material.io/styles/typography/overview) applied to a text label. Source of truth in code: see the last section.

## Purpose

Names something or shows one short value in one line: a caption beside a control, a title in a row, a value in a status bar.

## When to use and not

- Use when: one line of static or slot-driven text.
- Do not use when: the text may wrap (use [[Text Box]]); it scrolls to fit (use [[Marquee Text]]); the user edits it (use [[Text Field]]); it explains a control as a hint (use [[Tooltip]]); it must name a control (put the name on the control or use a [[Form Row]] label association).

## Anatomy

1. Text: one line, no wrap (`Wrap: NONE`).
2. Accessible name: the text itself (`Label` = `Text`).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Default | Body text | `body_medium` (shell body 14/20) |
| Muted | Secondary text | colour `on_surface_variant` (shell `on_surface_muted`), set by the caller's style |
| Other roles | Titles, captions | the type role is set by the caller's style |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | `on_surface` text | [[Text]] |
| Disabled | Opacity 0.5 (`Label:disabled`); MD3 text disabled is `on_surface` at 38 percent; spec follows [[Disabled State]] | [[Disabled State]] |
| Hover, focus, pressed, selected | Not applicable: not interactive | not applicable |
| Empty | No text: the Label takes no width beyond its box; spec: an empty Label has zero width unless `Width` is set | not applicable |
| Cut | A text wider than the Label ends with an ellipsis (spec); code default is `CLIP` | [[Text Truncation]] |

## Tokens used

Colour role `on_surface` (default stylesheet `Text` rule); type: the shell `body` role (14/400/20) maps to `body_medium` ([[Typography]]); no shape or elevation.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Line box height | 20 | 20 | 20 | `body_medium`; type does not scale with density |
| Minimum hit area | Not applicable: not a target |  |  | a standalone Label with a tooltip needs a 24 dp high box |

## Layout and overflow

One line, never wraps. Overflow: spec `ELLIPSIS` (the Label silently clipping is the F5 defect in [[Owner Feedback 2026-11-20]]); code default is `CLIP`, so the author must set `Overflow: ELLIPSIS` in a stylesheet. Give the Label a `Width` to make it narrower than its text. Vertical centring by the parent row ([[10 Layout Overflow and Scrolling]]). In a flex row the Label has `Min_Width 0` so it can shrink.

## Behaviour

- Pointer: none; the Label takes no pointer events unless the caller sets handlers.
- Keyboard: not focusable.
- Touch: none.
- A slot updates the text in place with no rebuild.

## Tooltip and overlay behaviour

A Label carries a tooltip only when it names something the user needs help with, or when it is cut (the full text); the trigger is the Label itself, never the row ([[Form Row]], ADR-0004, F8). A Label inside a control that has its own tooltip carries none. 500 ms, 150 ms grace ([[Tooltip]]).

## Motion

Not applicable: a Label has no animation.

## Accessibility

- Role: none; `Label` = the text, so assistive technology reads it. Decorative duplicates are hidden with `A11y_Hidden` by the author.
- Keys: none.
- Announcements: a changing value is not live by default; a status value that matters uses a polite announcement from the module ([[Accessibility Announcements]]).
- Contrast: 4.5:1 against its surface in all schemes ([[Accessibility Rules]] AR-16).

## Dark and light

Text takes `on_surface` through the Default stylesheet and follows the theme mode ([[Theme Following the System]]); the disabled look is opacity.

## Defaults

| Setting | Default |
|---|---|
| `Text` | empty |
| `Wrap` | `NONE` |
| `Overflow` | `CLIP` in code, `ELLIPSIS` in spec |

## Acceptance criteria

- [ ] AC-MOD-LBL-1 (AT tree assertion): a Label with text `Volume` exposes name `Volume`; a slot change to `Mute` changes the name within one loop turn without creating a node.
- [ ] AC-MOD-LBL-2 (pixel check): a Label with a text wider than its `Width` ends with `…` inside the box and paints nothing past the box edge.
- [ ] AC-MOD-LBL-3 (static check): no project stylesheet sets a Label `Overflow` to `CLIP` for a text that can exceed its box.
- [ ] AC-MOD-LBL-4 (geometry check): the Label's line box is 20 dp high with `body_medium` and is centred in a 40, 32 or 28 dp row within 1 px.
- [ ] AC-MOD-LBL-5 (contrast script): Label text against the surface at least 4.5:1 in Light, Dark and High_Contrast.
- [ ] AC-MOD-LBL-6 (scripted input): a Label inside a row is never focusable and receives no key.
- [ ] AC-MOD-LBL-7 (scripted pointer): a Label with a tooltip shows exactly 1 layer after 500 ms and none from its row.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Label/Label_Module.tdl`, `Stylesheets/Default_Stylesheet.tdl` | partly meets: name = text, no wrap, `Label:disabled` (meets AC-MOD-LBL-1, -4 by reading); default overflow is `CLIP` (fails AC-MOD-LBL-2, -3 unless the stylesheet sets `ELLIPSIS`) |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (Label) | exists |
| tess-ui | `tess-ui:src/tess_ui/views/` text views | not applicable: tess-ui uses [[Text]] |
| tre | `text` node | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Single-line read-only text; no MD3 component named Label | MD3 has type roles, not a Label component | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Ellipsis by default | silent clipping is a defect (F5) | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Material Web typography tokens: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-typescale.scss (see [[Typography]]).
- WCAG 2.2 SC 1.4.3 Contrast (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, [[Owner Feedback 2026-11-20]] F5.
