---
title: Marquee Text
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, text, motion]
related: ["[[Text]]", "[[Label]]", "[[Task Item]]", "[[Media Module]]", "[[14 Accessibility Basics#Reduced motion|Reduced Motion]]", "[[State Layers#Disabled scheme|Disabled State]]", "[[Bar]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Marquee Text

> [!info] Summary
> Marquee Text scrolls a text that is wider than its box so the whole text can be read in a small space, and shows an ellipsis with the whole text in a tooltip when it does not scroll. No Material Design 3 counterpart (Tesserae-specific); the nearest patterns are single-line [[Text]] truncation and the WCAG rule for moving content. Source of truth in code: see the last section.

## Purpose

Fits a long title, such as a window or a track title, into a fixed width in a [[Bar]] without losing the end of the text.

## When to use and not

- Use when: one line of changing text, such as a track or window title, must fit a narrow fixed width.
- Do not use when: the text is static and fits (use [[Label]]); the text is the only way to read information that a user must read once and quickly (a status message: use [[Text]] with a tooltip); the content is more than one line (use [[Text Box]]).
- Every Marquee needs a second route to the whole text: the tooltip and the accessible name carry it.

## Anatomy

1. Box: clips its children (`Width` 160 dp default).
2. Text: one line, moved by the engine with `translate_x` (no Python per frame).
3. Whole-text tooltip: on the Box, text equal to the Text.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Restart | Default (`Loop: RESTART`) | wait, scroll to the end, wait, jump back |
| Bounce | `Loop: BOUNCE` | wait, scroll to the end, wait, scroll back |
| Direction | `LEFT` (the start shows first) or `RIGHT` | scroll direction |
| Static | Disabled, reduced motion, or the text fits | no scroll; a cut text ends with an ellipsis |

## States

| State | Visual change | Token values |
|---|---|---|
| Fits | Static text, no animation, 0 frames at idle | [[Text]] |
| Scrolling | Text moves at `Speed` (30 dp per second) and pauses `Pause` (1500 ms) at each end | [[Motion]] |
| Paused (hover or focus) | Spec: the scroll stops while the pointer rests on the box or the box has keyboard focus; not built (see Accessibility) | WCAG 2.2 SC 2.2.2 |
| Disabled | Opacity 0.5 (`Marquee_Text:disabled`), no scroll, ellipsis, tooltip with the whole text (the one tooltip that opens over a disabled block, `Tooltip_When_Disabled`) | [[State Layers#Disabled scheme|Disabled State]] |
| Reduced motion | No scroll; ellipsis; whole text in the tooltip | [[14 Accessibility Basics#Reduced motion|Reduced Motion]] |
| Hidden or off-screen | The scroll stops while the block is not visible | not applicable |

## Tokens used

Text colour `on_surface`, type `body_medium` or the role of the parent; no container, no shape, no elevation. Motion values from [[Motion]]: speed and pause are module params, not tokens.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Width | 160 | 160 | 160 | param `Width`; the Tesserae default; the parent sets it |
| Height | line height of the role | same | same | 20 dp for `body_medium` |
| Edge fade | none | none | none | spec choice: none; a fade mask is a later request |

The Marquee is not interactive; the tooltip hover area is the box and is at least 24 dp high (`target.min`).

## Layout and overflow

One line, clipped at the box. The text is measured once the layout is known; it scrolls only when wider than the box (a 0.5 dp tolerance counts as fitting). Vertical centring in the row. Not scrolling and cut: ends with `…` ([[10 Layout Overflow and Scrolling]]).

## Behaviour

- Pointer: hover shows the whole-text tooltip after 500 ms; spec: hover also pauses the scroll.
- Keyboard: not focusable; the whole text is the accessible name.
- Touch: long press shows the tooltip.
- Timing: one engine animation per leg and one timer per pause; Python runs at the end of a leg, never per frame.

## Tooltip and overlay behaviour

One tooltip, on the Marquee box (the control), text = the whole text. 500 ms, 150 ms grace, dismissal list of [[Tooltip]]. A control that contains a Marquee (a [[Task Item]], the [[Media Module]] title) must not show a second tooltip for the same area: the Marquee needs an option that turns its own tooltip off inside a tooltip-bearing control, or lets the parent supply the text (candidate request to tess-shell). Today the tooltip is always set (`Tooltip: <| params.Text |>`) and gated only while disabled.

## Motion

The scroll is the only motion: linear, `Speed` dp per second, pause 1500 ms at each end. With reduced motion on the text does not scroll ([[14 Accessibility Basics#Reduced motion|Reduced Motion]], rule 4 of [[Motion]]). WCAG 2.2 SC 2.2.2 (Pause, Stop, Hide) asks for a way to pause moving content that lasts more than 5 seconds and starts automatically: spec: pause on hover and keyboard focus, and no scroll under reduced motion #needs-verification (whether hover pause is a sufficient mechanism).

## Accessibility

- Role: none (static text); `Label` = the whole text, so assistive technology never reads a moving fragment.
- Keys: none (not focusable).
- Announcements: none; a changing title is not announced by the Marquee.
- Contrast: text 4.5:1 on its surface in all schemes.
- The scroll never hides the only copy of information: the tooltip and the name carry it.

## Dark and light

Text takes `on_surface` through the Default stylesheet (`Text` rule) in light, dark and high contrast; see [[Theme Following the System]].

## Defaults

| Setting | Default |
|---|---|
| `Speed` | 30 dp per second |
| `Pause` | 1500 ms |
| `Direction` | `LEFT` |
| `Loop` | `RESTART` |
| `Width` | 160 dp |

## Acceptance criteria

- [ ] AC-MOD-MQT-1 (scripted input): a text wider than the box starts one animation leg after `Pause`, at `Speed` dp per second (tolerance 5 percent); a text that fits creates no animation and the window draws 0 frames at idle.
- [ ] AC-MOD-MQT-2 (scripted input): hiding the block stops the scroll and creates no further frame; showing it again restarts at the start.
- [ ] AC-MOD-MQT-3 (scripted input): with reduced motion on, a long text does not animate, ends with an ellipsis and the tooltip shows the whole text.
- [ ] AC-MOD-MQT-4 (scripted input): with `Enabled` false the text does not animate, opacity is 0.5 and the tooltip still opens with the whole text when the text is cut, and not when it fits.
- [ ] AC-MOD-MQT-5 (AT tree assertion): the node's accessible name equals the whole text, whatever the scroll position.
- [ ] AC-MOD-MQT-6 (scripted input): hover for 500 ms: exactly 1 tooltip layer with the whole text; leave removes it within 150 ms plus one frame.
- [ ] AC-MOD-MQT-7 (scripted input): with the pointer resting on the box the scroll position stays unchanged for 3 seconds (hover pause); moving away resumes.
- [ ] AC-MOD-MQT-8 (static check): a Marquee inside a tooltip-bearing control shows no second tooltip: hovering the control shows exactly 1 layer.
- [ ] AC-MOD-MQT-9 (contrast script): text against the surface at least 4.5:1 in Light, Dark and High_Contrast.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Marquee_Text/Marquee_Text_Module.tdl`, `Marquee_Text_Module.py`, `tess-shell:src/tess_shell/binder/marquee.py` | partly meets: engine-driven scroll, no frames at idle, reduced motion, disabled and tooltip gate, name = text (meets AC-MOD-MQT-1, -2, -3, -4, -5, -6, -9 by reading); no hover pause (fails AC-MOD-MQT-7); always-on tooltip nests inside tooltip-bearing controls (fails AC-MOD-MQT-8) |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (Marquee text) | exists |
| tess-ui | none | not applicable: no marquee |
| tre | engine animation of `translate_x` | not applicable: the shell composes the module |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Hover and focus pause of the scroll | WCAG 2.2 SC 2.2.2 | [[ADR-0004 Tooltip rule]] |

## Sources

- WCAG 2.2 SC 2.2.2 Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html (content that moves for more than 5 seconds needs a pause, stop or hide mechanism, except when essential). Verified 2026-11-21.
- WCAG 2.2 SC 2.3.3 Animation from Interactions and the reduced-motion preference are covered in [[14 Accessibility Basics#Reduced motion|Reduced Motion]].
- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `tess-shell:src/tess_shell/binder/marquee.py`.
