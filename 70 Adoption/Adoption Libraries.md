---
title: Adoption Libraries
type: adoption
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adoption, libraries, tess-dl, tess-el, tess-utils]
related: ["[[70 Adoption]]", "[[Adoption tre]]", "[[Audit Template]]", "[[Test Method]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[Shape]]", "[[Image]]", "[[17 Conformance]]", "[[Existing Tokens]]"]
depends_on: ["[[17 Conformance]]", "[[Test Method]]"]
---

# Adoption Libraries

> [!info] Summary
> What the specification requires of the three shared libraries tess-dl, tess-el and tess-utils. tess-dl and tess-el: nothing that changes their code. tess-utils: one addition that the specification needs and no project has yet (a contrast helper), one small optional addition (colour to hex), and one criterion set that its image decoder already meets. Read from the vault notes and from the libraries' source and documentation (tess-utils 0.2.2, tess-dl 0.2.0, tess-el 0.2.0); no test was run and no criterion is recorded as `pass` by this note.

## Scope and method

The vault has no "Status in code" column for the libraries: they are not toolkit or shell. This note reads (1) every vault note that names them (the [[Inventory]] rows for TDL, TEL, colour parsing, sides, radius and image decoding; [[Existing Tokens]]; the research note of gaps) and (2) the criteria whose test needs a computation that a library could own. Severity as in [[Adoption tre]]: high (needs a library feature for a MUST criterion), medium (the criterion fails or cannot be run today, and application code can supply it), low (a SHOULD or a convenience).

## tess-dl

TDL is structure only: blocks, properties and values; it "does not know what a bar, a monitor or a colour is" (`tess-dl:docs/language.md`). It carries no visual or style schema, no token, no role and no unit; keys, units, colours and slots belong to the reading program (tess-ui, tess-shell).

| ID | Severity | Requirement | AC ids | Evidence path | Result |
|---|---|---|---|---|---|
| LIB-001 | none | The specification asks nothing of tess-dl. Colour literals in a stylesheet (AC-COL-5), the corner scale (AC-SHP-4) and the spacing set (AC-DEN-1) are scanned in the project's own stylesheet files by a project lint; the scan may read the files with tess-dl, but needs no new feature. | AC-COL-5, AC-SHP-4, AC-DEN-1 (project lint, not library) | `tess-dl:docs/language.md`, `tess-dl:docs/api.md` | nothing applies |
| LIB-002 | none | Writing rules ([[15 Writing]]) cover interface text; the library's errors are developer messages. They are already plain sentences a screen reader reads whole, with `file:line:column` in text and no colour or symbol (`tess-dl:docs/api.md`, Accessibility). | none | `tess-dl:docs/api.md` (Accessibility) | nothing applies |

## tess-el

TEL evaluates expressions, conditions and repeaters (`tess-el:docs/language.md`); it holds no visual value. The vault names it only as a pattern in the [[Inventory]] ("TEL expression bindings", not yet specified).

| ID | Severity | Requirement | AC ids | Evidence path | Result |
|---|---|---|---|---|---|
| LIB-003 | none | The specification asks nothing of tess-el. Reduced motion, scheme and density are signals the toolkit and shell read from tre and expose to expressions as names; which names exist is the host's schema, not the library's. | none | `tess-el:docs/language.md` | nothing applies |

## tess-utils

Admission rule of the package (`tess-utils:README.md`): a function is added when at least two projects use it, it is a few lines, it imports no Tesserae package, has no dependency and no UI or schema meaning, and has tests. Today: `parse_color` (hex, 148 names, `rgb`, `hsl`, CSS Color 4 wide gamut clipped into sRGB), `expand_sides`, `to_tre_order`, `expand_radius`, `to_tre_word`, `decode_image`, `decode_image_file`. Both tess-ui and tess-shell depend on `tesserae-utils` (`>=0.2.2` and `>=0.2.1`).

| ID | Severity | Requirement | AC ids | Evidence path | Suggested change | Spec note |
|---|---|---|---|---|---|---|
| LIB-004 | medium | The contrast script of [[Test Method]] (WCAG 2.2 relative luminance, ratio `(L1 + 0.05) / (L2 + 0.05)`, alpha composited over the real background before measuring) is "new" and exists in neither tess-ui nor tess-shell (no luminance or ratio function in either source tree; tess-shell has only an sRGB-to-linear step in `tess-shell:src/tess_shell/surfaces/frame_shader.py`). Both projects need it for the same criteria. It is pure arithmetic on the 8-bit RGBA tuple `parse_color` returns, so it meets the admission rule. | AC-COL-3, AC-COL-4, AC-COL-9, AC-SCB-09, AC-FOC-4, AC-RAD-9, AC-BLK-TRM-4, AC-STB-8, AC-IMG-10 | `tess-utils:src/tess_utils/color.py`, `tess-utils:src/tess_utils/gamut.py` (has `_srgb_to_lin`, private) | add `relative_luminance(color)`, `composite(fg, bg)` and `contrast_ratio(fg, bg)` (alpha composited over `bg`, which must be opaque); state the rounding of the composite to 8 bits once (the existing alpha rule rounds half up, 0.38 gives 97); the script, its table output and the non-zero exit stay in each project's `tests/` | [[Test Method]] (Contrast script specification), [[Colour Roles]] |
| LIB-005 | low | Token tests compare a resolved role to a hex string (AC-COL-2 "exact 24-bit match, alpha 255", AC-SCB-01 and the tables write `#RRGGBB`). `parse_color` reads hex; nothing writes it back. A colour-to-hex helper would keep the test messages readable and the comparison in one place. A colour-role-to-hex helper does not belong here: roles are toolkit and shell schema (tess-ui theme, shell Default theme), which the package's rule excludes. | AC-COL-2, AC-COL-1 | `tess-utils:src/tess_utils/color.py` | optional: `to_hex(color)` returning `#RRGGBB` or `#RRGGBBAA` (lowercase, alpha last, as `parse_color` reads) | [[Colour Roles]] |
| LIB-006 | none | Image decoding: the criteria of [[Image]] on size, orientation and animation are met by `decode_image` as documented: a side over `max_side` (default 4096) is refused from the header (a 4097 side gives an error, AC-IMG-8), EXIF orientation is applied (`ImageOps.exif_transpose`), an animated GIF or WebP gives its first frame, output is straight-alpha RGBA8 as the tre `image` node takes. One caution: `decode_image_file` has no limit unless given, so a consumer must pass `max_side=4096` to meet the criterion. Whether it does is a tess-ui audit row, not a library change. | AC-IMG-8 | `tess-utils:src/tess_utils/image.py`, `tess-utils:docs/reference.md` (Images) | none; the consumer passes the limit | [[Image]], [[Bitmap]] |
| LIB-007 | none | Density tokens (the three levels, 40/32/28 dp and the spacing set), size classes (`width_class`, `height_class`, AC-DEN-10) and the corner scale tokens are design values with UI meaning; they live in tess-ui `tokens.py` and the shell look model. They fail the package's rule (UI meaning) and need no library. `width_class` is implemented in tess-ui; if tess-shell needs the same function it should be a project decision, not a library one. | AC-DEN-1 to AC-DEN-11, AC-SHP-1 | `tess-ui:src/tess_ui/tokens.py` | none | [[Spacing and Density]], [[Shape]] |
| LIB-008 | none | Scale factor: 1 dp is 1 px at scale 1.0 and projects multiply by the window scale factor, which tre reports (`scale_factor`, `dpi_scaling`). The geometry criteria are read in dp from the layout tree; no conversion helper is required. `expand_sides`, `to_tre_order` and `expand_radius` give the four-value forms tre takes and no criterion constrains them (the nested-radius rule of [[Shape]], inner = outer minus padding, is one subtraction in the toolkit). | AC-DEN-2 to AC-DEN-9, AC-SHP-2 | `tess-utils:src/tess_utils/sides.py`, `tess-utils:src/tess_utils/radius.py` | none | [[Spacing and Density]], [[Shape]] |
| LIB-009 | none | Wide-gamut and HDR: the engine is 8-bit sRGB; `parse_color` clips wide-gamut input into sRGB, as the colour chapter assumes. No criterion asks for more. | AC-COL-2 | `tess-utils:src/tess_utils/gamut.py` | none | [[Colour Roles]] |

## Counts

| Library | Requirements that change code | Optional | Nothing applies |
|---|---|---|---|
| tess-dl | 0 | 0 | 2 (LIB-001, LIB-002) |
| tess-el | 0 | 0 | 1 (LIB-003) |
| tess-utils | 1 (LIB-004, medium) | 1 (LIB-005, low) | 5 (LIB-006 to LIB-009; LIB-006 is met by the library) |

## Proposed requests

No request note exists for the libraries; the owner of tess-utils decides on the admission rule.

| Title | Findings |
|---|---|
| tess-utils: WCAG contrast helpers (`relative_luminance`, `composite`, `contrast_ratio`) | LIB-004 |
| tess-utils: colour to hex (optional) | LIB-005 |

## Questions

1. For the tess-utils bot: does a contrast helper meet the admission rule (two consumers, no UI meaning) given that the vault specifies the script but keeps it in each project's `tests/`? If the helper sits in the library, may a test-only import of `tess_utils` be used (the consumers carry it compiled in `_vendor/` per the README)?
2. For the tess-utils bot: the compiled `.so` copy in `_vendor/`: do the consumers' test environments import the same version as the installed package, so a contrast test and a runtime parse agree?
3. For the tess-ui and tess-shell bots (not libraries): who owns the contrast script run over the shipped themes (AC-COL-4), and where does the table of each run go for the audit?

Back to [[70 Adoption]].
