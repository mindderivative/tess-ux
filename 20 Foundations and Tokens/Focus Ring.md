---
title: Focus Ring
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, focus, accessibility, tokens]
related: ["[[State Layers]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[Scrollbar and Scroll Container]]", "[[Text Field]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[ADR-0009 State layer percentages]]", "[[Existing Tokens]]"]
depends_on: ["[[ADR-0009 State layer percentages]]", "[[Colour Roles]]"]
---

# Focus Ring

> [!info] Summary
> The visible indicator of keyboard focus: a 3 dp ring in the role `secondary`, offset 2 dp from the control, shown for keyboard focus, and for pointer focus in text inputs. It is never clipped by a scroll container. MD3 counterpart: the focus indicator of Material Web (`md-focus-ring`).

Decision: [[ADR-0009 State layer percentages]]. The 10 percent focus state layer is in [[State Layers]].

## Geometry and colour

| Property | Value | Verified source |
|---|---|---|
| Width | 3 dp | `md.comp.focus-ring.width` 3px |
| Offset | 2 dp outside the control's border box (outward) | `md.comp.focus-ring.outward-offset` 2px |
| Inward variant | offset 0 dp, ring drawn inside the border box, 3 dp wide | `md.comp.focus-ring.inward-offset` 0px |
| Corner radius | the control's radius plus the offset (outward); the control's radius minus the offset (inward) | `_focus-ring.scss` |
| Colour | role `secondary` | `--md-focus-ring-color: var(--md-sys-color-secondary)` |
| Layout effect | none: the ring does not move or resize any sibling | Tesserae rule |
| Animation | MD3 animates the ring width to 8 dp and back over the `long4` duration (Material Web); Tesserae draws the ring at full width in the first frame (no animation) | `active-width` 8px, `duration` long4 |

Dp values equal px at scale factor 1.0 ([[Spacing and Density]]).

## When the ring is visible

| Situation | Ring |
|---|---|
| Keyboard focus arrives (Tab, Shift+Tab, arrow key moves, access key) | shown |
| Pointer click moves focus to a button, switch, list row, tree row or other non-text control | not shown (`focus_visible` false) |
| Pointer click or keyboard focus in a text input (Text Field, Spin Box, Search Bar) | shown or replaced by the field's own focus indicator of at least the same contrast; pointer users need to see where the caret is |
| Focus arrives by assistive technology | shown (the engine reports `focus_visible` true for AT focus, `tre:docs/guide/events-and-input.md`) |
| After a key press following a pointer click | shown (the next keyboard interaction turns visible focus on) |
| Window loses focus | hidden; shown again when the window regains focus and the last input was a key |
| Control disabled | not focusable, no ring ([[State Layers]]) |

The rule follows the CSS `:focus-visible` heuristic that Material Web uses (https://github.com/material-components/material-web/blob/main/focus/internal/focus-ring.ts) #needs-verification for the text-input pointer case, which is a Tesserae rule.

## Contrast

The ring against the adjacent surface meets 3 to 1 (WCAG 2.2 SC 1.4.11 Non-text Contrast: user interface components and states need 3:1 against adjacent colours). A contrast script computes the ratio of `secondary` against the surface role of the parent in light and dark schemes and in each shipped theme. For the MD3 baseline scheme this is expected to pass with margin (light secondary against surface about 6 to 1, dark about 10.9 to 1, computed from the baseline hex values, which are not re-verified here #needs-verification). A theme that fails sets a different ring colour in its high-contrast variant; the default stays `secondary`.

## The ring is never clipped by a scroll container

A ring is drawn outside the control by 2 dp plus 3 dp width, that is up to 5 dp beyond the border box. A clipping ancestor (a scroll container, a panel that clips its children) cuts it when the control sits at the clip edge. Rules:

1. A scroll container reserves content padding of at least 5 dp on every side where a focusable child can touch the clip edge. At default level the container padding is at least `space.3` (8 dp), which meets this.
2. A control that must touch the clip edge (a full-width row in a list, a tree row at the container edge) uses the inward ring (3 dp inside the border box, offset 0).
3. A ring is clipped only by the window, never by a clipping ancestor, unless rule 2 applies.
4. When the focused control scrolls into view, the scroll position also reveals the whole ring, so the scroll-into-view target is the border box grown by 5 dp, limited to the scrollable extent.

Evidence: owner feedback shows content clipped and unreachable in scroll containers ([[Owner Feedback 2026-11-20]] F5 and F6).

## Other rules

- A resized focused node keeps ring and node aligned: the ring is recomputed when the node's bounds change. tess-ui places the ring when focus arrives and keeps the old ring after a resize (`tess-ui:docs/guide/interaction.md`, "Not yet covered"), which fails AC-FOC-6.
- The ring is not obscured by a sticky bar, overlay or popup when focus arrives: WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum) requires that the focused component is not entirely hidden by author-created content.
- The optional gradient ring of tess-ui (`App(focus_ring="gradient")`, a sweep through `secondary`, `primary` and `tertiary`, one turn per 3000 ms) is a Tesserae extension, off by default; it is static (a single colour `secondary`) under reduced motion.
- A control with no border box shape (a text run, a link) gets a ring around its text box, with the same offset.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/interaction.py` (RING_WIDTH 3, RING_OFFSET 2), `tess-ui:src/tess_ui/controls.py` line 89 (colour `secondary`), `tess-ui:src/tess_ui/focusring.py` | partly meets: AC-FOC-1, AC-FOC-2, AC-FOC-3 (non-text controls) meet by constants and doc; AC-FOC-3 for text inputs and AC-FOC-5 (clip) not verified in code; AC-FOC-6 fails (ring not recomputed on resize) |
| tess-shell | `tess-shell:src/tess_shell/model/look.py` lines 140 to 163 | partly meets: the binder draws a ring of 2 px in `color.primary` (fallback `#5B97C9`), spread, no offset; fails AC-FOC-1 (width 2, colour `primary`, offset 0) and AC-FOC-2 |
| tre | `tre:docs/guide/events-and-input.md` | not applicable: the engine draws no focus ring; it reports `focus_visible` on focus events |

Source facts: [[Existing Tokens]] (focus ring tables of tess-ui and the shell).

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No ring animation (MD3 grows the ring to 8 dp and shrinks it) | animation adds nothing for desktop use; keeps the ring testable in one frame | [[ADR-0009 State layer percentages]] |
| Ring also shown for pointer focus in text inputs | the caret may be hidden when the window is not active; pointer users need to see which field has focus | [[ADR-0009 State layer percentages]] |
| Inward ring where the control touches a clip edge | prevents clipping in scroll containers | [[ADR-0009 State layer percentages]] |
| Optional gradient ring | Tesserae identity option | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Acceptance criteria

- [ ] AC-FOC-1 (token test): ring width is 3, offset is 2, colour role is `secondary` in the project's tokens or constants. Pass: values equal exactly.
- [ ] AC-FOC-2 (pixel check): a focused Button at scale 1.0 shows a ring whose outer edge is 5 dp and inner edge 2 dp outside the border box on all four sides, with corner radius equal to the control's radius plus 2 dp, in the `secondary` colour (tolerance 1 per 8-bit channel, 1 px of antialiasing).
- [ ] AC-FOC-3 (scripted input): Tab to a Button shows the ring; clicking a Button with the mouse does not show it; clicking in a Text Field shows a focus indicator; Tab after a click shows the ring on the next control.
- [ ] AC-FOC-4 (contrast script): the ratio of `secondary` against the parent surface is at least 3.0 in light and dark for every shipped theme. Pass: all ratios at least 3.0.
- [ ] AC-FOC-5 (pixel check): a focusable control inside a scroll container, at each of the four container edges, shows 100 percent of its ring pixels (outward in container padding at least 5 dp, or inward at the edge); no ring pixel is transparent or cut by the clip.
- [ ] AC-FOC-6 (geometry check): after the focused control is resized by 10 dp, the ring bounds equal the new border box grown by 2 dp in the next frame.
- [ ] AC-FOC-7 (scripted input): the ring appears in the same frame as the focus change (no growth animation); under reduced motion the optional gradient ring is static.
- [ ] AC-FOC-8 (scripted input): focus moved by Tab to a control below the visible area of a scroll container scrolls the container so that the control and its ring are fully visible (AC-LAY-14).
- [ ] AC-FOC-9 (AT tree assertion): the focused node in the accessibility tree is the node that shows the ring, and focus set by assistive technology shows the ring.

## Sources

- Focus ring tokens (width 3px, outward-offset 2px, inward-offset 0px, active-width 8px, duration long4): https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-focus-ring.scss (verified 2026-11-21).
- Ring colour `--md-sys-color-secondary` and width 3px: https://github.com/material-components/material-web/blob/main/docs/components/focus-ring.md (verified).
- Ring geometry and animation: https://github.com/material-components/material-web/blob/main/focus/internal/_focus-ring.scss (verified).
- WCAG 2.2 SC 1.4.11 Non-text Contrast, 3:1: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html (verified). SC 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/TR/WCAG22/ (title verified; wording not quoted).
- MD3 page https://m3.material.io/foundations/interaction/states is unreadable by tools; the 3 dp and 2 dp values come from the Material Web tokens.
