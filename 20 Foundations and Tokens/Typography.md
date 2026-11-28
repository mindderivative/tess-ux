---
title: Typography
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [foundation, typography, tokens]
related: ["[[Colour Roles]]", "[[Shape]]", "[[Spacing and Density]]", "[[Text Field]]", "[[Tooltip]]", "[[Existing Tokens]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0029 Desktop density and type scale]]", "[[Owner Feedback 2026-11-20]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# Typography

> [!info] Summary
> The 15 Material Design 3 type roles with size, line height, weight and tracking, the Tesserae rules for text in controls (vertical centring, ellipsis, minimum size) and the mapping of the shell's 5 type roles. Counterpart: [Material 3 typography](https://m3.material.io/styles/typography/type-scale-tokens). Source of truth in code: see Status in code.

## Purpose

One type scale gives every project the same sizes, weights and spacing. Two owner observations bear on it: single-line text in a text field sits at the top of the field and not at its vertical centre (F7), and a path label runs past its container with neither wrapping nor ellipsis (F5), both in [[Owner Feedback 2026-11-20]].

## Tokens

### Type scale

Values from the published Material Web token source [md-sys-typescale v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss) (1 rem = 16 px; the file gives rem values, converted here). Tracking is given in dp, so 0.03125 rem is 0.5 dp. The family is Roboto for the brand and the plain typeface ([md-ref-typeface](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-ref-typeface.scss): brand Roboto, plain Roboto; weights regular 400, medium 500, bold 700). 1 dp = 1 px at scale 1.0.

| Role | Size (dp) | Line height (dp) | Weight | Tracking (dp) | Family |
|---|---|---|---|---|---|
| `display_large` | 57 | 64 | 400 | -0.25 | Roboto |
| `display_medium` | 45 | 52 | 400 | 0 | Roboto |
| `display_small` | 36 | 44 | 400 | 0 | Roboto |
| `headline_large` | 32 | 40 | 400 | 0 | Roboto |
| `headline_medium` | 28 | 36 | 400 | 0 | Roboto |
| `headline_small` | 24 | 32 | 400 | 0 | Roboto |
| `title_large` | 22 | 28 | 400 | 0 | Roboto |
| `title_medium` | 16 | 24 | 500 | 0.15 | Roboto |
| `title_small` | 14 | 20 | 500 | 0.1 | Roboto |
| `body_large` | 16 | 24 | 400 | 0.5 | Roboto |
| `body_medium` | 14 | 20 | 400 | 0.25 | Roboto |
| `body_small` | 12 | 16 | 400 | 0.4 | Roboto |
| `label_large` | 14 | 20 | 500 | 0.1 | Roboto |
| `label_medium` | 12 | 16 | 500 | 0.5 | Roboto |
| `label_small` | 11 | 16 | 500 | 0.5 | Roboto |

### Desktop roles

Four roles added for the `compact` and `dense` density levels ([[ADR-0029 Desktop density and type scale]]). They have no MD3 counterpart; the sizes come from the Researcher's desktop scale and the tracking is a design choice (the nearest MD3 role's value) `#needs-verification`. Family Roboto.

| Role | Size (dp) | Line height (dp) | Weight | Tracking (dp) |
|---|---|---|---|---|
| `body_dense` | 13 | 18 | 400 | 0.25 |
| `title_dense` | 13 | 18 | 500 | 0.1 |
| `page_title_compact` | 20 | 28 | 400 | 0 |
| `page_title_dense` | 18 | 24 | 400 | 0 |

### Type by density

A control or container takes its text role from its density level. The token `density.font_body` holds the body role at `default`, `compact` and `dense`.

| Use | default | compact | dense |
|---|---|---|---|
| Body, field text, row label | `body_large` 16/24 | `body_medium` 14/20 | `body_dense` 13/18 |
| Small text, helper, caption | `body_small` 12/16 | `body_small` 12/16 | `body_small` 12/16 |
| Section title | `title_medium` 16/24/500 | `title_small` 14/20/500 | `title_dense` 13/18/500 |
| Page title | `title_large` 22/28 | `page_title_compact` 20/28 | `page_title_dense` 18/24 |

`default` is the touch size and equals the MD3 roles; the config app uses `compact` with the Files and Structure panels `dense` ([[Config App Layout]]). The component notes still name `body_large` and `body_medium` in their Default column; their `compact` and `dense` columns follow this table.

### Prominent label weight

`label_large` and `label_medium` have a prominent weight of 700 (`label-large-weight-prominent`, `label-medium-weight-prominent` in the same source). It marks a selected or emphasised label.

### Per-role tracking in a text engine

Tracking is applied as extra advance per character in dp. An engine that cannot apply tracking to a node kind renders that kind at 0 and the status table records it.

### Mapping of the tess-shell type roles

tess-shell has 5 roles (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` lines 30 to 34). Its names reuse MD3 words with other meanings; the mapping is documentary ([[ADR-0001 MD3 role names are the specification vocabulary]]).

| Shell role | Size / weight / line height | Nearest MD3 role | Match |
|---|---|---|---|
| `$type.caption` | 12 / 400 / 16 | `body_small` (12 / 400 / 16, tracking 0.4) | exact in size, weight and line height |
| `$type.label` | 13 / 500 / 18 | `title_dense` (13 / 500 / 18, a desktop role above); nearest MD3 role `label_large` (14 / 500 / 20) | exact against `title_dense`; between `label_large` 14 and `label_medium` 12 |
| `$type.body` | 14 / 400 / 20 | `body_medium` (14 / 400 / 20, tracking 0.25) | exact in size, weight and line height |
| `$type.title` | 18 / 500 / 24 | `title_medium` (16 / 500 / 24) | nearest; no MD3 role has size 18 |
| `$type.display` | 28 / 400 / 36 | `headline_medium` (28 / 400 / 36) | exact; the shell name `display` is an MD3 `headline` size |

## Rules

1. Text takes size, line height, weight and tracking from a role by name. A literal size or weight in a view is allowed only for content (user-chosen font) and for icon glyph fonts.
2. Minimum text size is 11 dp (`label_small`). No UI text is smaller.
3. Line height is the value in the table; the line box of a single-line label is its line height. Layout uses the line box, not the glyph ink box.
4. Single-line text in a control is centred vertically in the control: the centre of the line box lies at the centre of the control height at every density ([[Spacing and Density]]). Alignment by padding is allowed only when the padding is derived from control height and line height (`(control height - line height) / 2`). Evidence: F7. For a text field the rule is part of [[Text Field]].
5. Single-line text that is wider than its container ends with an ellipsis ("...") at the container edge and never draws past the container. The full text is available by tooltip on the control ([[Tooltip]]) or by selection. Wrapping is allowed only for body text in a container that sets a maximum number of lines; a label never wraps. Evidence: F5.
6. Tracking uses the table values. A project that cannot apply tracking states it as a deviation.
7. Roboto is the default family. The fallback chain is Roboto, then the desktop UI font, then the platform sans. Missing glyphs fall back per glyph.
8. Text colour comes from an `on_` role ([[Colour Roles]]); text smaller than 24 dp regular meets 4.5:1.
9. Expressive emphasised type styles ([md-sys-typescale-emphasized](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-typescale-emphasized.scss) exists in the latest tokens) are not part of the baseline; a project adopts one only through a named entry in [[Deviations from MD3]].
10. Text size follows the density of its container: the role of each use at `default`, `compact` and `dense` is the density-to-role table. A control reads its body role from `density.font_body`, so a 32 dp field never carries `body_large` and a 28 dp row never carries `body_medium` ([[ADR-0029 Desktop density and type scale]]).

## Acceptance criteria

- [ ] AC-TYP-1: Token test. For each of the 15 roles, the theme returns size, line height and weight equal to the type scale table. Pass: size and weight exact, line height within 0.5 dp (a project that stores line height as a ratio of size passes when the product is within 0.5 dp).
- [ ] AC-TYP-2: Token test. For each of the 15 roles, the tracking equals the table value. Pass: exact match in dp, 15 of 15, or a recorded deviation for the node kind that cannot apply it.
- [ ] AC-TYP-3: Token test (static scan). No view stylesheet or module sets `Font_Size`, `Font_Weight`, `Line_Height` or `Letter_Spacing` to a literal outside the allow-list of Rules 1. Pass: zero hits.
- [ ] AC-TYP-4: Geometry check. In a single-line control at each density (default 40, compact 32, dense 28 dp control height) render the text "Hxg" and measure the line box. Pass: line box centre is within 1 dp of the control centre.
- [ ] AC-TYP-5: Pixel check for F7. Render a single-line text field containing "Hx" at each density and compute the ink bounding box of the text. Pass: the ink box centre is within 1 dp of the field centre, vertically; the ink box is never closer to the top edge than to the bottom edge by more than 2 dp.
- [ ] AC-TYP-6: Geometry check for F5. Place a label whose natural width is 3 times the container width. Pass: the rendered text ends with an ellipsis, its right edge is at or inside the container's right edge, and it has one line.
- [ ] AC-TYP-7: Scripted input. Hover the truncated label of AC-TYP-6 for 500 ms. Pass: a tooltip on that label shows the full text ([[Tooltip]] rules).
- [ ] AC-TYP-8: Token test. The smallest size in the theme is 11 dp. Pass: no role below 11.
- [ ] AC-TYP-9: Review. Each text role in a component spec names an MD3 role from the table. Pass: reviewer finds none that uses a literal size.
- [ ] AC-TYP-10: Static scan and geometry check. In a container at `compact` or `dense` density no text node takes `body_large`, `title_medium` or `title_large`; the body role of a compact container is `body_medium` and of a dense container `body_dense`. Pass: zero hits in the stylesheets and in a rendered config app (compact application, dense Files and Structure panels).
- [ ] AC-TYP-11: Token test. The four desktop roles return the sizes, line heights, weights and tracking of the desktop roles table ([[ADR-0029 Desktop density and type scale]]). Pass: exact match; `body_dense` is 13/18/400 and no role below 11 dp (AC-TYP-8).

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`TYPE_SCALE`, `MD3_TRACKING`); `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`; `tess-ui:src/tess_ui/composed.py` | Partly meets. AC-TYP-1 meets: sizes and weights equal the table; line heights are ratios whose products differ from the table by at most 0.2 dp (for example 63.84 for 64). AC-TYP-2 fails: tracking is 0 for all 15 roles; `MD3_TRACKING` holds the table values for 9 roles and is not applied. AC-TYP-3 fails: tooltips use literal Roboto 12 and 14/500 (`composed.py` lines 813 to 819), so a theme `Typography` override does not reach them. AC-TYP-4 and AC-TYP-5 partly meet: a single-line config text field is 32 dp high with 7 dp top and bottom padding and no engine vertical-align, so centring is by padding, which holds only for an 18 dp line box (32 minus 2 times 7) and leaves a taller line box off-centre [INFERENCE from the padding values]. AC-TYP-6 meets in the config app tree (label Min_Width 0 with ellipsis) and not in the toolkit default tree row. |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Partly meets. 5 roles map as in the mapping table; AC-TYP-1 not applicable to the 15-role form. No tracking token. Font family: Roboto fallback and the desktop `font-name` family. `Line_Height` in the shell is a pixel value (tre takes a multiple of the font size): the shell binder converts px to the multiplier once tess-shell fixes it; the specification states line heights in sp. |
| tre | `tre:docs/reference/properties.md` (Text); `tre:crates/engine-py/src/window_events.rs` | Not applicable as a scale: the engine has no roles. Default text font Roboto 400 at 16 px; `letter_spacing` and `line_height` exist on the text node only (not on `text_input`), so AC-TYP-2 cannot be met for text inputs; bundled faces Roboto Regular and Medium (weight 700 for the prominent label weight has no bundled face #needs-verification). |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| tess-ui applies tracking 0 for all roles | Engine and theme defaults predate the tracking table; flagged as a gap to close, not a design choice | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Dimensions in dp equal px at scale 1.0 | Projects scale by the window scale factor | [[ADR-0002 Desktop density levels and target sizes]] |
| The 5 shell type roles map to the nearest MD3 role | Shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Single-line text vertical centring and ellipsis rules | Desktop controls; owner feedback F5 and F7 | [[ADR-0002 Desktop density levels and target sizes]] |
| Four desktop roles (`body_dense` 13/18, `title_dense` 13/18/500, `page_title_compact` 20/28, `page_title_dense` 18/24) and a density-to-role table | MD3 has one type scale for touch; at 32 and 28 dp controls the 16 and 14 dp body text reads large beside the control (owner feedback on the config app, 2026-11-28) | [[ADR-0029 Desktop density and type scale]] |
