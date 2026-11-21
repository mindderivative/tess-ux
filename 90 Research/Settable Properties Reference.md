---
title: Settable Properties Reference
type: research
status: research
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [research, settable, tre, tess-ui, tess-shell, adr-0020]
related: ["[[Scrollbar and Scroll Container]]", "[[Focus Ring]]", "[[State Layers]]", "[[Motion]]", "[[Elevation]]", "[[Tooltip]]"]
depends_on: []
---

# Settable Properties Reference

The lookup table for note authors. Owner principle (ADR-0020, in the Decisions folder of the engineering branch; not in this branch): tre never blocks a design change; every visual element and parameter of tre is adjustable from Python through properties, tokens or declarative hooks, with no per-frame Python; tess-ui and tess-shell own the look. Every default in a component note records whether it is settable from Python in tess-ui, tess-shell and tre; this note gives the answer per parameter class.

Vocabulary of the cells: `yes` (a property, named), `via <name>` (a stylesheet key, token or other indirect route), `hardcoded in tre` (file and constant), `no hook` (neither settable nor hardcoded in the engine because the project layer does not expose it), `n/a: <reason>`. Paths cite the project repositories: `tre:crates/...`, `tess-ui:src/...`, `tess-shell:...`. Read from tre docs and code, tess-ui spec, views and interaction code, and tess-shell schema and styling guide; nothing was run. Items not verified in code are marked `[INFERENCE]`. tess-re's own audit of tre hardcodes was not waited for (see the open questions).

Reading hints. In tre a property is set with `node.set(name=value)` or `window.create(kind, name=value)` and the engine paints it itself; per-frame Python is never needed. tess-ui builds nodes from a widget spec with a style (snake-case keys, for example `corner_radius`) and a theme of roles and tokens (`tess-ui:src/tess_ui/spec/build.py`, `default_theme.tdl`). tess-shell exposes only the keys in `tess-shell:docs/guide/styling.md` (style key table, generated from `tess-shell:src/tess_shell/schema/blocks.py`) plus theme tokens in the groups color, type, shape, space, elevation, motion.

## Table

| Parameter class | tre | tess-ui | tess-shell | Notes |
|---|---|---|---|---|
| Height and size | yes: `width`, `height` (px, auto, %, calc) (`tre:docs/reference/properties.md`) | yes: style `width`, `height` (`tess-ui:src/tess_ui/spec/build.py`) | yes: block keys `Width`, `Height` (`tess-shell:src/tess_shell/schema/blocks.py`) | Control heights (40, 48 dp) are widget defaults in tess-ui, not engine values. |
| Min width and min height | yes: `min_width`, `min_height`, `max_width`, `max_height` | yes: style `min_width`, `min_height`, `max_width`, `max_height` (`tess-ui:src/tess_ui/spec/build.py`) | yes: `Min_Width`, `Min_Height` (`tess-shell:src/tess_shell/schema/blocks.py`) | Touch-target minimum (48) is a widget default, not an engine rule. |
| Padding | yes: `padding`, `padding_top/right/bottom/left` | yes: style `padding` | yes: `Padding` on Box, FlexBox, Text, TextField (via token `space.*`) | tre text nodes lay content inside padding. |
| Margin | yes: `margin`, `margin_*` | yes: style `margin` | yes: `Margin` on 9 block types | |
| Gap | yes: `gap`, `row_gap`, `column_gap` | yes: style `gap`, `row_gap`, `column_gap` | yes: `Spacing` on FlexBox (via token `space.*`) | shell has no separate row and column gap. [INFERENCE] |
| Border width | yes: `border_width` (animatable) | yes: style `border_width` | yes: `Border_Width` (7 block types) | |
| Border colour | yes: `border_color` (animatable); gradient `border_gradient` | yes: style `border_color` | yes: `Border_Color` (token `color.*`) | |
| Corner radius (per corner) | yes: `corner_radius`; per corner through a four-value radius (`tre:crates/engine-core/src/node.rs`, `corner_radii_override`) | yes: style `corner_radius`; default values per component in `Components {}` of `tess-ui:src/tess_ui/spec/default_theme.tdl` | yes: `Corner_Radius` one number or four from top-left clockwise (via token `shape.*`) | Per-corner exposure in tess-ui style: `[INFERENCE]` follows tre. |
| Font family and size | yes: `font_family`, `font_size` | via text role in the theme type scale; text keys on a widget (`tess-ui:src/tess_ui/spec/build.py`) | yes: `Font_Family`, `Font_Size` (tokens `type.*.font_size`, `type.system.font_family`) | |
| Font weight | yes: `font_weight` 1 to 1000 | via type role (`tess-ui:src/tess_ui/spec/build.py`) | yes: `Font_Weight` (token `type.*.font_weight`) | |
| Line height | yes: `line_height` (multiple of font size, text only) | via type role (`role_style`) | yes: `Line_Height` (px; token `type.*.line_height`) | tre takes a multiple, shell takes px: unit differs. |
| Letter spacing | yes: `letter_spacing` (px, text only) | yes: `text.letter_spacing`, default from role tracking (`tess-ui:src/tess_ui/spec/build.py`) | no hook | |
| Text colour | yes: `fill` (animatable) | via theme role (`on_surface` and others), widget `foreground` | yes: `Foreground` | |
| Icon size and icon colour | yes: `width`, `height` of an `svg` or `path` node, `fill` | via widget `icon` size and `foreground` (`tess-ui:src/tess_ui/spec/build.py`) | yes: `Width`, `Height` of SVG block; `Foreground` (`currentColor` follows it) | |
| Fill and background colour | yes: `background` (animatable), `gradient` | yes: style `background` | yes: `Background` (Box, FlexBox, TextField), `Fill` (Rectangle, Circle, Path) | |
| Opacity | yes: `opacity` (animatable) | yes: style `opacity` | yes: `Opacity` | |
| Elevation and shadow (list, spread, colour) | yes: `shadows` list with colour, offset_x, offset_y, blur, spread (`tre:crates/engine-core/src/node.rs` `Shadow`) | yes: style `elevation` (level) and shadow list with `spread` (`tess-ui:docs/schema/tess-ui-stylesheet-schema.json`); level defaults in theme | yes: `Elevation` percent, `Shadows` list; token `elevation.max`, `elevation.reach` | shell scales one maximum shadow; it has no five-level scale. |
| Blur | yes: `blur`, `backdrop_blur` (animatable) | yes: style `blur`, `backdrop_blur`, `blur_behind` | no hook | |
| Focus ring (colour, width, offset, shape) | hardcoded in tre: no, tre draws no focus ring (`tre:docs/guide/events-and-input.md`); ring is a node the project draws | via `RING_WIDTH` 3.0, `RING_OFFSET` 2.0 module constants and ring colour argument (`tess-ui:src/tess_ui/interaction.py`); `App(focus_ring=)` chooses solid or gradient | via `Shadows` on the block (the `ScrollBox` takes shadows for the ring, `tess-shell:src/tess_shell/schema/blocks.py`); no ring key | In tess-ui the widths are Python constants, not settable from a stylesheet or token: `no hook` for stylesheet use. See [[Focus Ring]]. |
| State layer colours and opacities | n/a: tre has no state layer; a child node with `background` and `opacity` draws it | via `HOVERED, FOCUSED, PRESSED, DRAGGED = 0.08, 0.10, 0.10, 0.16` and `interaction_tint` (`tess-ui:src/tess_ui/interaction.py`, `spec/build.py`) | no hook: no state layer in the key table; hover feedback only by a Transition on keys | The tess-ui opacities are module constants: `no hook` for theme or stylesheet. See [[State Layers]]. |
| Ripple (colour, duration, easing) | n/a: tre has no ripple; tess-ui draws it with a shader node (`tre:docs/reference/shader.md`) | via `PRESS_GROW_MS` 450, `PRESS_FADE_IN_MS` 105, `MINIMUM_PRESS_MS` 225, `RELEASE_FADE_MS` 375, `INITIAL_SCALE` 0.2, `STANDARD` curve (`tess-ui:src/tess_ui/ripple.py`, `interaction.py`); colour is the tint | no hook | Constants, no stylesheet key. |
| Hover and press timings | n/a: tre has no hover state; `animate(...)` takes a duration | via `HOVER_MS` 15 (`tess-ui:src/tess_ui/interaction.py`), scaled by `motion.duration` | via `Transition`, `Duration`, `Easing` keys on 12 block types | |
| Animation duration and easing | yes: `animate(name, to, duration, easing)` and transitions (`tre:docs/guide/animation.md`) | via style `transition` list and `duration`, `easing` (`tess-ui:docs/schema/tess-ui-stylesheet-schema.json`); reduced motion in `tess-ui:src/tess_ui/motion.py` | via `Transition`, `Duration`, `Easing` and tokens `motion.duration.short/medium/long`, `motion.easing.*` | See [[Motion]]. |
| Scrollbar thumb thickness | yes: `scrollbar_width` on a scroll view (`tre:docs/reference/paint.md`); default hardcoded: `SCROLLBAR_THICKNESS` 4.0 (`tre:crates/engine-core/src/node.rs`) | no hook: not set in `_scroll_props` (`tess-ui:src/tess_ui/spec/build.py`) | no hook | ADR-0012 asks 12 dp hit area: thickness alone is settable, hit area not (see Engine hardcodes). See [[Scrollbar and Scroll Container]]. |
| Scrollbar thumb radius | hardcoded in tre: `SCROLLBAR_THUMB_RADIUS` 2.0 (`tre:crates/engine-render/src/lib.rs`) | no hook | no hook | Not settable even from tre Python. |
| Scrollbar thumb colour and opacity | yes: `scrollbar_fill` (colour with alpha); default hardcoded: `DEFAULT_SCROLLBAR_FILL` 0xCAC4D0 at alpha 0x8C (about 55 percent) (`tre:crates/engine-render/src/lib.rs`) | via role `outline`: `scrollbar_fill=_role(ctx, "outline")` (`tess-ui:src/tess_ui/spec/build.py`) | no hook | No hover or drag colour state in tre: one fill. [INFERENCE] |
| Scrollbar track | hardcoded in tre: no track is painted [INFERENCE: no track constant found] | no hook | no hook | |
| Scrollbar margin | hardcoded in tre: `SCROLLBAR_MARGIN` 2.0 (`tre:crates/engine-core/src/node.rs`) | no hook | no hook | |
| Scrollbar gutter | hardcoded in tre: no gutter; the thumb overlays content [INFERENCE] | no hook | no hook | |
| Scrollbar show policy | hardcoded in tre: shown whenever content overflows; no auto-hide property found [INFERENCE] | no hook | no hook | |
| Scrollbar min length and grab slop | hardcoded in tre: `SCROLLBAR_MIN_LENGTH` 32.0, `SCROLLBAR_GRAB_SLOP` 6.0 (`tre:crates/engine-core/src/node.rs`) | no hook | no hook | |
| Wheel step | hardcoded in tre: `WHEEL_LINE_PX` 20.0 (`tre:crates/engine-py/src/listeners.rs`); keyboard line `KEY_SCROLL_LINE` 40.0 (`tre:crates/engine-core/src/tree/scroll.rs`) | no hook | no hook | |
| Scroll snap | yes: `scroll_snap`, per child `snap_align`; settle `SNAP_SETTLE` 120 ms and `SNAP_DURATION` 200 ms hardcoded (`tre:crates/engine-core/src/tree/scroll.rs`) | yes: style `snap_align`; `scroll_snap` start, center, end, none in `_scroll_props` | no hook: `Scroll_Snap` is not built (`tess-shell:src/tess_shell/schema/blocks.py`) | Fling constants `FLING_TAU`, `FLING_STOP`, `FLING_MIN` hardcoded. |
| Tooltip delay and placement | n/a: tre has no tooltip; `anchor`, `placement`, `offset` place a node | via `TIP_DELAY` 500, `TIP_WIDTH` 200, `TIP_GRACE` 150 class constants of the compositor (`tess-ui:src/tess_ui/composed.py`); a per-widget `tooltip` mapping, placement through the engine `placement` | via block key `Tooltip` (a flag on a Popup) and `Tooltip_When_Disabled`; no delay, no placement key | Delay is a Python constant in tess-ui: `no hook` for stylesheet. See [[Tooltip]]. |
| Vertical alignment of text | n/a: tre has no vertical text alignment property; centre with `align_items` or `justify_content` on the parent | via `align_items` on the parent and `align_self` | via `Align_Items` on the FlexBox parent | |
| Horizontal alignment of text | yes: `text_align` start, center, end | yes: `text.text_align` | yes: `Text_Align` (Text only) | A TextField has none in tess-ui (`tess-ui:src/tess_ui/spec/build.py`). |
| Ellipsis | yes: `overflow` clip or ellipsis, `max_lines` | yes: text `overflow`, `max_lines` | yes: `Overflow` CLIP or ELLIPSIS (a TextField also SCROLL); `Max_Lines` on a text-input-length key only | |
| Wrapping | yes: `wrap` word or none | yes: text `wrap` | no hook | |
| Text selection colour | yes: `selection_fill`; default hardcoded: text colour at 30 percent (`tre:docs/reference/paint.md`) | no hook: only `selectable` is set (`tess-ui:src/tess_ui/spec/build.py`) | no hook | |
| Caret colour | yes: `caret_color` (animatable) | via role `primary` in `TextInput` build (`tess-ui:src/tess_ui/spec/build.py`) | no hook | |
| Caret width | yes: `caret_width`; default 1.5 (`tre:crates/engine-core/src/node.rs`) | no hook | no hook | |
| Caret blink | yes: `caret_blink` ms; default 0 (steady) (`tre:crates/engine-core/src/node.rs`) | yes: widget option `caret_blink` (`tess-ui:src/tess_ui/spec/builtin_widgets.py`, `typing_effects.py` `BLINK_MS`) | no hook | |
| Caret shape | yes: `caret_shape` bar, block, underline | no hook | no hook | |
| Cursor shape | yes: `cursor` (23 shapes or an image) (`tre:docs/reference/node.md`) | yes: style `cursor` | no hook | |
| Clip radius | yes: `clip_children` clips to the rounded box; `mask` circle, rounded, path | yes: style `clip_children` | no hook | Clip radius follows `corner_radius`; no separate value. |
| Layout gap and alignment | yes: `gap`, `align_items`, `justify_content`, `align_self`, grid keys | yes: same names in style | yes: `Spacing`, `Align_Items`, `Flex` (FlexBox) | |
| Z-order and layer | yes: `z_index`; layers `layer_placement` and layer windows (`tre:docs/reference/layers.md`, `layer-window.md`) | yes: style `z_index` | yes: `Z_Index`; `Layer` (TOP, BOTTOM, OVERLAY) on Bar and Panel | |
| Window decorations | yes: `Window(decorations=)`, `resize_border`, `window_region` (`tre:docs/guide/custom-title-bars.md`) | yes: `App(borderless=)` sets `decorations`, `resize_border` (`tess-ui:src/tess_ui/app.py`); title bar spec `tess-ui:src/tess_ui/spec/title_bar.py` | n/a: the shell draws layer-shell bars and panels, which have no window decorations | |

## Engine hardcodes

Visual values fixed in tre that the specification would need to change. The proposed property is a proposal only. Values read from code; every row `[INFERENCE]` about intent only.

| Name | Current value | File | Proposed property |
|---|---|---|---|
| `SCROLLBAR_THICKNESS` | 4.0 px (settable as `scrollbar_width`; the constant is the default) | `tre:crates/engine-core/src/node.rs` | already `scrollbar_width`; default from a theme hook |
| `SCROLLBAR_MARGIN` | 2.0 px | `tre:crates/engine-core/src/node.rs` | `scrollbar_margin` |
| `SCROLLBAR_MIN_LENGTH` | 32.0 px | `tre:crates/engine-core/src/node.rs` | `scrollbar_min_length` |
| `SCROLLBAR_GRAB_SLOP` | 6.0 px each side of the thumb (hit area 4 + 12 = 16) | `tre:crates/engine-core/src/node.rs` | `scrollbar_hit_slop` (needed for ADR-0012: 12 dp hit area) |
| `SCROLLBAR_THUMB_RADIUS` | 2.0 px | `tre:crates/engine-render/src/lib.rs` | `scrollbar_radius` |
| `DEFAULT_SCROLLBAR_FILL` | 0xCAC4D0 at alpha 0x8C (outline variant at 55 percent) | `tre:crates/engine-render/src/lib.rs` | none needed: `scrollbar_fill` exists; add `scrollbar_fill_hover`, `scrollbar_fill_drag` for ADR-0012 opacities 0.60, 0.80, 1.00 |
| Scrollbar track and show policy | no track; always shown on overflow [INFERENCE] | `tre:crates/engine-render/src/lib.rs` | `scrollbar_track`, `scrollbar_visibility` (auto, always, never) |
| `WHEEL_LINE_PX` | 20.0 px per wheel line | `tre:crates/engine-py/src/listeners.rs` | `wheel_step` on the window or scroll view |
| `KEY_SCROLL_LINE` | 40.0 px per arrow key | `tre:crates/engine-core/src/tree/scroll.rs` | `key_scroll_step` |
| `SNAP_SETTLE` | 120 ms | `tre:crates/engine-core/src/tree/scroll.rs` | `scroll_snap_settle` |
| `SNAP_DURATION` | 200 ms | `tre:crates/engine-core/src/tree/scroll.rs` | `scroll_snap_duration` and `scroll_snap_easing` |
| `FLING_TAU`, `FLING_STOP`, `FLING_MIN` | 0.35, 30.0, 150.0 | `tre:crates/engine-core/src/tree/scroll.rs` | `fling_friction` |
| `VELOCITY_WINDOW` | 100 ms | `tre:crates/engine-core/src/gesture.rs` | none (gesture internals) [INFERENCE] |
| Default selection fill | text colour at 30 percent | `tre:crates/engine-render/src/lib.rs` [INFERENCE: file] | already `selection_fill`; document the default |
| Default caret width | 1.5 px (settable as `caret_width`) | `tre:crates/engine-core/src/node.rs` | already settable |
| `CODE_EDITOR_LINE_HEIGHT_RATIO`, `CODE_EDITOR_CHAR_WIDTH_RATIO` | 1.35, 0.6 | `tre:crates/engine-core/src/tree/mod.rs` | `line_height` already settable; ratios are layout estimates [INFERENCE] |
| `FIT_CONTENT_SLACK` | 2.0 px | `tre:crates/engine-core/src/tree/layout.rs` | none [INFERENCE] |
| `INITIAL_COLOR` | 0xFF6750A4 | `tre:crates/engine-render/src/lib.rs` | the window clear colour; theme hook if not already `Window(background=)` [INFERENCE] |
| Debug overlay colours | magenta and orange overlays | `tre:crates/engine-render/src/window_renderer.rs` | none (debug only) |
| `PADDING`, `GAP` (16.0 each) | layout of imperative factory windows | `tre:crates/engine-py/src/window.rs` [INFERENCE: purpose] | none if the factory is unused by tess-ui |
| MD3 catalog factory defaults (heights, radii as formula over height or size) | formulas in the imperative `add_button` and friends | `tre:crates/engine-py/src/window_factory.rs` (named in `tess-ui:src/tess_ui/spec/default_theme.tdl`; file not read) | shape and elevation are settable through the theme `Components` block; others `[INFERENCE]` |

Count: 21 rows (counting the three-constant fling row as one).

## Open questions for tess-re

1. Is there a scrollbar track, a gutter or an auto-hide policy in the renderer that this reading missed? The table assumes none.
2. Which defaults does the engine apply to text selection (30 percent of the text colour) and where, and can the caret's default colour be set without a role?
3. Are there per-corner radius values exposed in the Python API (`corner_radii_override`) by name?
4. Does tre draw any hover, press or disabled feedback itself? The reading found none.
5. What are the hardcoded hit sizes of window resize borders and title-bar regions (`resize_border` default) and of slider and checkbox kinds listed in the default theme?
6. Which of the `window_factory.rs` constants remain reachable from tess-ui, and which are shadowed by the theme `Components` block?
7. Do tess-ui style keys for shadow `spread` and per-corner radii reach tre unchanged?
