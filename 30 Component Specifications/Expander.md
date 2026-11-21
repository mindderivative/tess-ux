---
title: Expander
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, reveal, motion]
related: ["[[Accordion]]", "[[Button]]", "[[Popup]]", "[[Dialog]]", "[[Auto Hide|Content Fade]]", "[[14 Accessibility Basics#Reduced motion|Reduced Motion]]", "[[Motion]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Expander

> [!info] Summary
> An Expander shows or hides its content with a size and fade animation, driven by a button elsewhere. No direct Material Design 3 counterpart (Tesserae-specific); [[Accordion]] is the disclosure pattern with its own header, and the WAI-ARIA disclosure pattern is the reference. Source of truth in code: see the last section.

## Purpose

Reveals content on demand without leaving the view: a settings section, details under a row.

## When to use and not

- Use when: a button elsewhere toggles a region that grows from an edge.
- Do not use when: the header and the region are one control (use [[Accordion]]); the content is a modal task (use [[Dialog]]); a flyout over the layout is needed (use [[Popup]]).

## Anatomy

1. Root: clipping box (`Clip_Children`); its size animates between 0 and the content size.
2. Body: the content, opacity animates with the size (`Content_Fade`).
3. Controller: a [[Button]] with `Expandable: true` that carries the `expanded` state; it lives outside the module.

## Variants

| Variant | Use | Differences |
|---|---|---|
| DOWN, UP | Default DOWN | sizes the height; grows from the top or bottom edge |
| LEFT, RIGHT | Side panels in a bar | sizes the width |
| No fade | `Content_Fade: false` | content stays opaque, only the size eases |

## States

| State | Visual change | Token values |
|---|---|---|
| Collapsed | Size 0 on the animated axis; body opacity 0; body hidden from assistive technology | not applicable |
| Expanded | Size AUTO; body opacity 1 | not applicable |
| Opening, closing | Size and opacity ease together; an interrupted animation turns round from where it is | [[Motion]] |
| Hover, focus, pressed | Not applicable: the controller button carries them | [[Button]] |
| Disabled | Not applicable: the controller is disabled instead | not applicable |

## Tokens used

No colour or shape of its own. Duration: the theme's medium duration 200 ms (`$motion.duration.medium`) unless `Duration` is set; easing `standard` (0.2, 0, 0, 1) ([[Motion]]).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Own size | content size | content size | content size | the Expander adds no padding; the content uses [[Spacing and Density]] steps |
| Animation duration | 200 ms | 200 ms | 200 ms | [[Motion]]; a desktop control change is at most 200 ms |

## Dimensions and defaults

The Expander is a structural clipping box; current shell values read from `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl`: size AUTO when expanded and 0 on the animated axis when collapsed, no padding, no gap, no border, no fill, `Clip_Children: true`. The spec keeps these as the defaults at every density.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| root | height | - | N/A: content height (AUTO); 0 while collapsed on the DOWN and UP axis | N/A: same as the default column | N/A: as in Default | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height); tre: n/a: element absent in tre |
| root | min width | - | 0 | 0 | 0 | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` (width 0 when collapsed on the LEFT and RIGHT axis) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Width); tre: n/a: element absent in tre |
| root | min height | - | 0 | 0 | 0 | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` (height 0 when collapsed on the DOWN and UP axis) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Height); tre: n/a: element absent in tre |
| root | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]]; code sets none | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding); tre: n/a: element absent in tre |
| root | margin | - | N/A: the parent container sets the outer space | N/A: same as the default column | N/A: as in Default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Margin); tre: n/a: element absent in tre |
| body | gap | `space.0` | 0 | 0 | 0 | [[Spacing and Density]]; the Body holds one Content, the content sets its own gaps | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: n/a: element absent in tre |
| root | border width | - | 0 | 0 | 0 | [[Expander]] (no colour or shape of its own); code sets none | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| root | border color | - | N/A: the Expander draws no border; border is the content's | N/A: same as the default column | N/A: as in Default | [[Expander]] (Tokens used) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| root | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]]; the clip box is rectangular | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: n/a: element absent in tre |
| body | font | - | N/A: the Expander draws no text; the content sets the font | N/A: same as the default column | N/A: as in Default | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| body | icon size | - | N/A: the Expander draws no icon; the controller button does | N/A: same as the default column | N/A: as in Default | [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: n/a: element absent in tre |
| root | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: n/a: element absent in tre |

## Layout and overflow

The root clips its children, so content never paints outside while it grows. Overflow of the content follows its own rules ([[10 Layout Overflow and Scrolling]]); a tall content inside a bounded region scrolls in a scroll container. Collapsing does not move the controller button.

## Behaviour

- Pointer: the controller button toggles; the Expander has no pointer handling of its own.
- Keyboard: Enter and Space on the controller toggle it; the Expander has no keys and is not focusable. When collapsed, the content takes no focus.
- Touch: tap the controller.
- `On_Changed` fires when an opening or closing has finished, with `event.value` true when open; also when the module changed `Expanded`, and at once under reduced motion.

## Tooltip and overlay behaviour

The Expander has no tooltip; a tooltip belongs to the controller button if it is icon-only ([[Tooltip]], ADR-0004). Content inside may carry its own tooltips on its own controls. When the region collapses, a shown tooltip of a control inside it is removed with the control (trigger removal).

## Motion

200 ms, `standard` easing, size and opacity together; the fade is the surface content fade ([[Auto Hide|Content Fade]]). Reduced motion: the state switches in one frame and the end event fires at once ([[14 Accessibility Basics#Reduced motion|Reduced Motion]]). At rest the Expander draws no frames.

## Accessibility

- Role: none on the Expander; the controller button carries `expanded` (WAI-ARIA disclosure pattern).
- Collapsed content is `A11y_Hidden`, so a screen reader and the Tab order skip it.
- Keys: on the controller.
- Announcements: none; the `expanded` state change is read by the screen reader.
- Focus: focus is never lost into collapsed content: if the focused control is inside content that collapses, focus moves to the controller.

## Dark and light

No colours of its own; content follows the scheme.

## Defaults

| Setting | Default |
|---|---|
| `Expanded` | false |
| `Direction` | `DOWN` |
| `Duration` | -1 (theme medium, 200 ms) |
| `Content_Fade` | true |

## Acceptance criteria

- [ ] AC-MOD-EXP-1 (scripted input): setting `Expanded` true animates the height from 0 to the content height in 200 ms (tolerance one frame) with opacity 0 to 1 over the same time; the end event fires once with `value` true.
- [ ] AC-MOD-EXP-2 (scripted input): reversing the state at 50 percent progress turns the animation round from the current size and opacity, with no jump greater than one frame of travel.
- [ ] AC-MOD-EXP-3 (scripted input): with reduced motion on, the final state is drawn in the first frame and `On_Changed` fires at once.
- [ ] AC-MOD-EXP-4 (AT tree assertion): collapsed: the body is absent from the accessibility tree and takes no Tab stop; the controller reports `expanded` false; expanded: `expanded` true.
- [ ] AC-MOD-EXP-5 (scripted input): Enter and Space on the controller toggle it once each; a focused control inside content that collapses moves focus to the controller.
- [ ] AC-MOD-EXP-6 (pixel check): during the animation no pixel of the content paints outside the root box.
- [ ] AC-MOD-EXP-7 (scripted input): at rest the window draws 0 frames over 1 second.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl`, `Expander_Module.py` | partly meets: clip, size and fade together, interrupt turns round, hidden when collapsed, reduced motion, end event, no frames at rest (meets AC-MOD-EXP-1, -2, -3, -4, -6, -7 by reading); focus move from collapsing content not built (AC-MOD-EXP-5 unverified) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` (dimensions) | meets: no padding, gap, border or radius, as in the table |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (Expander) | exists |
| tess-ui | `tess-ui:src/tess_ui/views/` accordion views | not applicable: see [[Accordion]] |
| tre | `reveals` and transition support used by the shell | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific reveal primitive; [[Accordion]] covers the disclosure with a header | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Duration 200 ms standard easing | a desktop control change is at most 200 ms | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WAI-ARIA Authoring Practices, disclosure pattern: https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ (button with `aria-expanded`, Enter and Space toggle).
- Motion values: [[Motion]] (mapping of the shell tokens to MD3 `short4`).
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `tess-shell:docs/guide/modules.md#expander`.
