---
title: ADR-0025 Shell outline and high contrast status colours, accent never text
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Colour Roles]]", "[[Adoption tess-shell]]"]
depends_on: []
---

# ADR-0025 Shell outline and high contrast status colours, accent never text

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-22. The owner can overturn it. Raised by tess-shell's contrast test (tess-shell PR 148).

## Context

The shell's contrast test found four groups of findings against [[Colour Roles]]: Dark `outline` on `surface_raised` measures 2.69 to 1 (Button border and card edge need 3 to 1 as non-text); in High_Contrast on a Light scheme `error`, `warning` and `success` stay at their Light values and measure 3.21, 3.54 and 3.27 to 1 on the black surface (4.5 needed, 7 at the high level); and `accent` as text measures 4.38 on `surface` and 3.90 on `surface_raised` (Dark), 3.82 and 4.11 (Light), below 4.5. Nothing in `shipped/` uses `accent` as text, and as a pictogram or border (3 to 1) it passes everywhere.

## Options

1. Fix the theme colours (raise Dark `outline`, add three High_Contrast colours) and forbid `accent` as text (recommended, chosen)
2. Relax the specification to what the shell measures
3. Change `accent` until it passes as text

## Decision

- Dark `$color.outline` is `#5F7188`: 3.61 to 1 on `surface` and 3.21 to 1 on `surface_raised` (the smallest step that clears 3 to 1 on both with margin). Light `outline` stays `#7A8896` (3.37 and 3.63).
- High_Contrast sets `error` `#F2958C`, `warning` `#E6BB6A` and `success` `#8CCB9A` explicitly (the Dark values, 9.45, 11.68 and 11.12 to 1 on black) so the block no longer inherits the Light values.
- The `accent` colour is never used for text; text uses `primary` or `on_surface`. It stays valid as a pictogram or border colour (3 to 1). The specification states the rule as [[Colour Roles]] rule 12 and AC-COL-12; the token keeps its measured text ratios as a known violation entry in `tools/known_violations.json`, so the check stays green and the token is listed.

## Consequences

- tess-shell changes three theme values ([[Adoption tess-shell]] TSH-090, TSH-091) and its test list uses these values.
- The shell mapping table in [[Colour Roles]] carries the values; the Menu Item note's dark `on_surface` on `outline` ratio falls to 4.12 to 1, which is one more reason the specification uses a state layer and not an `outline` fill.

## Affected notes

- [[Colour Roles]]
- [[Adoption tess-shell]]
- [[Menu Item]]
