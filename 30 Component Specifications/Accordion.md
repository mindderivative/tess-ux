---
title: Accordion
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, accordion, disclosure, motion]
related: ["[[Form Row]]", "[[List Item]]", "[[Tree]]", "[[Scrollbar and Scroll Container]]", "[[Spacing and Density]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Typography]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]"]
---

# Accordion

> [!info] Summary
> A set of sections, each a header button that shows or hides its content. Material Design 3 has no accordion (the tess-ui documentation says the same); this is a Tesserae element built from an MD3 list row with a chevron and the WAI-ARIA accordion pattern (https://www.w3.org/WAI/ARIA/apg/patterns/accordion/). Source of truth in code: the last section.

## Purpose

Let the user show one section at a time (or several) so a long page of settings or help stays scannable, and group form rows under a header with a count of what is set.

## When to use and not

- Use when: content is divided into named sections that are read one at a time.
- Do not use when: the reveal is a single field ([[Form Row]] help line), the hierarchy is deeper than one level ([[Tree]]), or the sections must all stay visible (use headings).

## Anatomy

1. Section: a header and a content region.
2. Header: a full-width button with title, optional leading icon, optional trailing supporting text (a count), and a chevron.
3. Chevron box at the end edge; the glyph points down when closed and up when open.
4. Content region: indented by the header padding, hidden when closed.
5. Divider between sections: 1 dp, `outline_variant`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single | one section open; opening one closes the others | optional "one must stay open": the open header has `aria-disabled` true |
| Multiple | any number open | |
| Group header with count | config forms | trailing supporting text "3 of 12 set" in `label_small` |

## States

State layer role `on_surface` over the header at the percentages of [[ADR-0009 State layer percentages]].

| State | Visual change | Token values |
|---|---|---|
| Collapsed | chevron down, content hidden and not built | none |
| Expanded | chevron up, content visible | none |
| Hover | state layer on the header | 8 percent |
| Focus (keyboard) | layer plus focus ring inset in the header | 10 percent; ring 3 dp `secondary` ([[Focus Ring]]) |
| Pressed | state layer | 10 percent |
| Disabled | title and chevron at 0.38, no toggle, no focus stop | 0.38 |
| Error inside | a section that holds an invalid row shows an error dot in `error` next to the count #needs-verification (design choice) | |

## Tokens used

[[Colour Roles]] (title `on_surface`, chevron and count `on_surface_variant`, divider `outline_variant`), [[Typography]], [[Motion]], [[Spacing and Density]].

## Sizing and density

The header is a list-row sized button, so it uses the single-line row height of the density table ([[ADR-0002 Desktop density levels and target sizes]]). Other values are derived from the table and the spacing steps (0, 2, 4, 8, 12, 16, 24, 32, 48) and are design choices. #needs-verification

| Token | default | compact | dense |
|---|---|---|---|
| Header height | 40 dp | 32 dp | 24 dp |
| Header horizontal padding | 12 dp | 8 dp | 4 dp |
| Gap between header parts | 8 dp | 8 dp | 4 dp |
| Chevron box | 24 dp | 20 dp | 16 dp |
| Title type | `title_medium` 16/24 | `title_small` 14/20 | `title_dense` 13/18 |
| Content padding left, right | 12 dp | 8 dp | 4 dp |
| Content padding bottom | 16 dp | 12 dp | 8 dp |

The header is at least 24 dp tall at every density (WCAG 2.2 SC 2.5.8, [[ADR-0002 Desktop density levels and target sizes]]).

## Dimensions and defaults

The header is a list-row sized button, so its height, padding and gap are the density row values of [[Spacing and Density]]; the content padding, title type and chevron are Tesserae choices #needs-verification-as-design-choice (proposed ADR: accordion dimensions by density level). MD3 has no accordion.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| header | height | `density.row_height` | 40 | 32 | 24 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| header | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] (WCAG 2.2 SC 2.5.8) | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| header | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| header | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| content region | padding | `space.4`, `space.3`, `space.2` | 0 12 16 12 | 0 8 12 8 | 0 4 8 4 | design choice, proposed ADR (accordion dimensions by density); [[Accordion#Sizing and density]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| section | margin | - | N/A: the accordion is 100 percent of the parent width; the parent sets the outer space | N/A: same as default | N/A: same as default | [[Accordion#Layout and overflow]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| divider | border width | `md.comp.divider.thickness` | 1 | 1 | 1 | MD3 [divider tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| divider | border color | `outline_variant` | `outline_variant` | `outline_variant` | `outline_variant` | [[Accordion#Anatomy]], MD3 [divider tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| header | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] (the header is a list-row sized button, like the [[List Item]] container) | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| title | font | `title_medium`, `title_small`, `title_small` | 16/24/500/0.15 | 14/20/500/0.1 | 13/18/500/0.1 | [[Typography]]; design choice, proposed ADR (accordion dimensions by density); compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| count | font | `label_small` | 11/16/500/0.5 | 11/16/500/0.5 | 11/16/500/0.5 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| chevron box | icon size | `density.chevron_box` | 24 | 20 | 16 | [[Spacing and Density]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| header | elevation | `elevation.level_0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

## Layout and overflow

- Width 100 percent of the parent. The title takes the remaining header width with a minimum width of 0 and one line; it truncates with an ellipsis. The chevron and count do not shrink.
- Content is laid out normally and may scroll with the page; an accordion inside a scroll container shows its bars ([[Scrollbar and Scroll Container]]).
- The header text is vertically centred in the header height.

## Behaviour

- Pointer: a press toggles the section. Press on the count or chevron acts as a press on the header.
- Keyboard: Tab and Shift plus Tab move between headers and the focusable content (all of them are in the page Tab order).

| Key | Action |
|---|---|
| Enter, Space | on a collapsed header: expand (single mode: close the others); on an expanded header: collapse (unless one must stay open) |
| Down, Up | optional, supported by Tesserae groups: move focus to the next, previous header |
| Home, End | optional, supported by groups: first, last header |

- Opening a section does not move focus; the focus stays on the header.
- Collapsing a section that contains the focus moves focus to its header.
- Touch: the header is the target, 48 dp in touch contexts.

## Tooltip and overlay behaviour

The header has no tooltip, except that a truncated title shows its full text in a tooltip on the title element only ([[ADR-0004 Tooltip rule]]).

## Motion

- Content height eases from 0 to its measured height in 250 ms (`medium1`) with `easing-emphasized-decelerate` cubic-bezier(0.05, 0.7, 0.1, 1) when opening, and in 200 ms (`short4`) with `easing-standard-accelerate` cubic-bezier(0.3, 0, 1, 1) when closing; the content fades with the height. The chevron turns 180 degrees in 200 ms with `easing-standard` cubic-bezier(0.2, 0, 0, 1) ([[Motion]]). #needs-verification (design choice; MD3 has no accordion motion).
- Reduced motion sets every duration to 0 ms.
- Closed content is not built and takes no focus stop.

## Accessibility

- The header is a `button` with the title as name, `aria-expanded` true or false, and `aria-controls` the content id; each header is inside a heading of the right level (WAI-ARIA accordion pattern). Where the native heading cannot be expressed, the header carries the heading level.
- The content has role `region` and is labelled by its header; the role is omitted when an accordion has more than about 6 open panels (APG).
- Closed content is hidden from assistive technology.
- When a section cannot be collapsed (single mode, one must stay open) the header has `aria-disabled` true.
- Contrast: title on the surface 4.5 to 1, chevron 3 to 1.

## Dark and light

Roles only ([[Theme Following the System]]).

## Defaults

Single mode, all sections closed, dividers on, `default` density unless the project sets a level.

## Acceptance criteria

- [ ] AC-ACC-01: Token test. Header height, padding, gap, chevron box and content padding equal the sizing table for the three densities.
- [ ] AC-ACC-02: Geometry check. Header heights are 40, 32 and 24 dp at `default`, `compact`, `dense`; the title text line box is centred within 0.5 dp.
- [ ] AC-ACC-03: Geometry check. A 300-character title ends in an ellipsis, the chevron stays inside the header and the header has no horizontal overflow.
- [ ] AC-ACC-04: Scripted input. Enter and Space on a collapsed header expand it and on an expanded header collapse it; focus stays on the header; in single mode opening a section closes the others.
- [ ] AC-ACC-05: Scripted input. With groups, Down, Up, Home and End move focus between headers without toggling.
- [ ] AC-ACC-06: AT tree assertion. Each header has role `button`, a name equal to the title, `aria-expanded` matching the state and `aria-controls` naming the content; closed content is absent from the accessibility tree.
- [ ] AC-ACC-07: AT tree assertion. The content has role `region` named by its header (accordions with at most 6 expandable panels).
- [ ] AC-ACC-08: Scripted input. In single mode with one-must-stay-open, the open header exposes `aria-disabled` true and Enter on it does nothing.
- [ ] AC-ACC-09: Pixel check. The content height reaches its measured height in 250 ms on open and 0 in 200 ms on close, sampled at 0, 50 percent and 100 percent of the duration (within 1 frame); 0 ms with reduced motion.
- [ ] AC-ACC-10: Pixel check. The chevron is rotated 0 degrees closed and 180 degrees open, reaching it in 200 ms.
- [ ] AC-ACC-11: Scripted input. Closed content takes no Tab stop: Tab from a header moves to the next header.
- [ ] AC-ACC-12: Scripted input. Collapsing a section that holds the focus moves focus to its header.
- [ ] AC-ACC-13: Pixel check. Hover shows an 8 percent `on_surface` layer, pressed and keyboard focus 10 percent; keyboard focus draws the 3 dp ring inset; a mouse click does not.
- [ ] AC-ACC-14: Contrast script. Title on the surface at least 4.5 to 1, chevron at least 3 to 1, in light and dark baseline schemes.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Accordion_View.tdl`, `Accordion_Stylesheet.tdl`, `AccordionGroup_View.tdl`, `tess-ui:docs/components/accordions.md` | partly meets. Header 56 px (spec 40 at default: fails AC-ACC-01, 02), padding 16 (spec 12), gap 12 (spec 8), chevron 24, title `title_medium` with ellipsis (AC-ACC-03 meets as designed); Enter, Space or press toggles and `Expanded` is two-way (AC-ACC-04 meets); group Up, Down, Home, End (AC-ACC-05 meets); header role button with `Expanded` and `Controls: content` (AC-ACC-06 meets in part: heading level absent); content role `group`, not `region` (AC-ACC-07 fails); closed content not built (AC-ACC-11 meets); no height easing (AC-ACC-09 fails: the engine cannot ease a height to `auto`); chevron 200 ms (turns 180 degrees, AC-ACC-10 meets); single-mode one-must-stay-open absent (AC-ACC-08) |
| tess-ui (config app) | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`group_header`) | partly meets. A hand-built Container button: chevron 20 in `primary`, `label_large` title in `primary`, count `label_small`, vertical padding 4, no horizontal padding, gap 4; role button with `Expanded` and a description "n of m keys set". Computed height about 28 dp (20 chevron + 8 padding, not measured), against `compact` 32 (fails AC-ACC-01, 02); no height easing; colour `primary` for the title where this note specifies `on_surface` (fails the token check) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` | partly meets. The Expander eases height and opacity over the theme medium duration (200 ms) and respects reduced motion (meets AC-ACC-09 in part: duration 200 ms for opening, spec 250 ms); it has no header and no keys of its own; the controlling Button (`Expandable: true`) carries `expanded` and toggles on Enter and Space (AC-ACC-04, 06 by composition) |
| tre | none | not applicable (no accordion; layout animation of a pixel height is available) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | settings grouping | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Header heights 40, 32, 24 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Open and close use different durations and easings | decelerate in, accelerate out is the MD3 pattern for enter and exit; applied by analogy | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |

## Sources

- WAI-ARIA Authoring Practices, Accordion pattern (keyboard Enter or Space, Tab, optional Down, Up, Home, End; header `button` inside a heading with `aria-level`, `aria-expanded`, `aria-controls`, optional `region`, `aria-disabled` when it cannot collapse): https://www.w3.org/WAI/ARIA/apg/patterns/accordion/ (read 2026-11-21).
- Motion tokens (short4 200 ms, medium1 250 ms; standard, standard-accelerate, emphasized-decelerate curves): https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-motion.scss.
- MD3 has no accordion: tess-ui:docs/components/accordions.md says so; also no accordion in the Material Web repository tree. #needs-verification against m3.material.io.
- Code: `tess-ui:src/tess_ui/views/Accordion_View.tdl`, `Accordion_Stylesheet.tdl`, `AccordionGroup_View.tdl` (origin/main c7117cb), `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl`.
