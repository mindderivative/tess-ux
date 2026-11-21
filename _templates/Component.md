---
title: Component Name
type: component
status: draft
owner: phil
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [component]
related: []
depends_on: []
---

# Component Name

> [!info] Summary
> One sentence: what the element is and the Material Design 3 counterpart (link). Status in code: see the section near the end.

## Purpose

What problem the element solves for the user.

## When to use and not

- Use when: ...
- Do not use when: ... (name the element to use instead, as a wikilink)

## Anatomy

Numbered parts (container, label, icon, indicator, ...). A Mermaid diagram only if it adds information.

## Variants

| Variant | Use | Differences |
|---|---|---|

## States

Rest, hover, focus, pressed, dragged, selected, disabled, error, loading, empty. For each state: state layer opacity, container and content colour roles, and what else changes.

| State | Visual change | Token values |
|---|---|---|

## Tokens used

Link to [[Colour Roles]], [[Typography]], [[Shape]], [[Elevation]], [[Motion]], [[Spacing and Density]]. List the role per part; do not repeat values defined there.

## Sizing and density

Minimum target size (dp), height and padding per density (default, compact, dense), icon size, window size class behaviour.

## Dimensions and defaults

Mandatory. One row per visual part and property; every cell holds a value or `N/A: <reason>`, never a blank. The columns and the property names are fixed so that tools can read the table (`tools/lint_vault.py` checks it, `tools/defaults_matrix.py` collects it into [[Defaults Matrix]]).

| Part | Property | Token | Default | Compact | Dense | Source |
|---|---|---|---|---|---|---|
| component | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]] |
| component | padding | `space.*` | 0 24 0 24 | 0 16 0 16 | 0 12 0 12 | design choice, [[ADR-0002 Desktop density levels and target sizes]] |
| component | margin | - | N/A: the parent container sets the outer space | N/A: same | N/A: same | [[Spacing and Density]] |
| component | gap | `space.2` | 8 | 8 | 4 | [[Spacing and Density]] |
| component | border width | - | 0 | 0 | 0 | MD3 token file URL |
| component | border color | - | N/A: no border | N/A: no border | N/A: no border | MD3 token file URL |
| component | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] |
| component | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 12/16/500/0.5 | [[Typography]] |
| component | icon size | `density.icon` | 18 | 18 | 16 | [[Iconography]] |
| component | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] |

Rules:
- Properties (exact names): `height`, `min width`, `min height`, `padding`, `margin`, `gap`, `border width`, `border color`, `corner radius`, `font`, `icon size`, `elevation`. The ten properties `height`, `padding`, `margin`, `gap`, `border width`, `border color`, `corner radius`, `font`, `icon size` and `elevation` appear at least once in every component note; add `min width` and `min height` where they exist and extra rows for parts that differ.
- Units: dp for lengths, written as numbers without the unit; `padding` is four numbers in the order top right bottom left (CSS order); `font` is size/line height/weight/tracking in sp, dp, weight and sp; `border color` and colour rows name a role; `elevation` is the level 0 to 5. Percentages and ratios carry their unit.
- The Token column names the token or `-`. The Source column links the foundation note, the MD3 token file or a project path. A Tesserae design choice names its ADR or a proposed ADR and carries `#needs-verification-as-design-choice` in the note text.
- `N/A: <reason>` needs a reason of at least 8 characters. A blank cell, `-` in a value column or `TBD` fails the lint.

## Layout and overflow

Alignment, baseline, truncation (ellipsis rule), wrapping, scrolling (scrollbar rule), minimum and maximum width, behaviour when space runs out.

## Behaviour

- Pointer: ...
- Keyboard: key sequences and focus order.
- Touch: ...

## Tooltip and overlay behaviour

Which part shows a tooltip, delay in ms, dismiss rules, which overlay the element opens, focus handling on open and close.

## Motion

Durations (ms), easing, what animates; reduced-motion behaviour.

## Accessibility

Role, accessible name source, keys, announcements, contrast ratios, target sizes, focus indicator.

## Dark and light

Differences between the themes and how the theme is chosen.

## Defaults

The values a project gets without configuration.

## Acceptance criteria

Each criterion passes or fails by a test, a measurement or a review.

- [ ] AC-1: ...

## Status in code

Per project: the paths that implement the element and whether the code meets the criteria above (meets, partly meets with the failing criterion ids, absent, not applicable).

| Project | Path | Status |
|---|---|---|

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|

## Sources

Links to the sources of every verified value (Material Web tokens, WCAG, WAI-ARIA, project code).
