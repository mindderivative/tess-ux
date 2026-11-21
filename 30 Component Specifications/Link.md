---
title: Link
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, text, tesserae-specific]
related: ["[[Text]]", "[[Rich Text]]", "[[Rich Text Span]]", "[[Button]]", "[[Text Selection]]", "[[Text Truncation]]", "[[Tooltip]]", "[[Form Row]]", "[[Keyboard Navigation]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Text]]", "[[Colour Roles]]", "[[Focus Ring]]", "[[Spacing and Density]]"]
---

# Link

> [!info] Summary
> Text that takes keyboard focus and that a click or Enter activates: it opens a web or mail address, or runs a handler that goes somewhere else in the app. MD3 defines no link component; its text colour role for interactive text is `primary` ([type and colour roles](https://m3.material.io/styles/color/roles)). Source of truth in code: see the last section.

## Purpose

A link takes the user to a different place: a documentation page, a mail composer, another page of the app. It reads as text, not as a button, because it moves the user rather than doing a thing in place.

## When to use and not

- Use when: the action is navigation (open a URL, go to a related page, open a section elsewhere) and the label is a phrase that names the destination.
- Do not use when: the action changes data or state in place (use [[Button]]), a toggle (use [[Switch]]), or the target is inside a longer sentence (use a `link` run of [[Rich Text]]; the standalone Link is for a whole line).
- Link text names the destination ("Read the docs", not "click here"); the same destination uses the same text everywhere.

## Anatomy

1. Text: the link's words, in a type role.
2. Underline: drawn while the pointer is over it or keyboard focus is on it by default, or always, or never.
3. Focus ring: 3 dp around the text box when keyboard focus is on it.
4. Trailing external-link glyph (optional): `open_in_new` at 16 dp for a link that leaves the app; the project decides, tess-ui draws none.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Standalone link | a line of its own (help line, footer) | `Link` element; underline on hover and focus by default |
| Inline link | inside a sentence | a `link` run of [[Rich Text]]; underlined always so that colour is not the only cue ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)) |
| Visited | a link that was followed | `secondary` colour; set by opening its `Href` |
| External | opens the browser or the mail program | `Href` with `http`, `https`, `mailto` or `tel` |
| Internal | goes elsewhere in the app | no `Href`, only a handler |

## States

State layers do not apply to text; a link changes colour, underline and focus ring ([[State Layers]] defines layers for containers).

| State | Visual change | Token values |
|---|---|---|
| Rest | text `primary`, underline per `Underline` (hover: none) | `tess-ui:src/tess_ui/views/Link_Stylesheet.tdl` |
| Hover | underline drawn; pointer is a hand | `Underline: hover` default |
| Focus (keyboard) | underline drawn and focus ring 3 dp `secondary`, offset 2 dp, around the text box | [[Focus Ring]] |
| Pressed | text colour `primary` unchanged; the underline stays; no layer | design choice, review |
| Visited | text `secondary` (`State: visited`) | `Link_Stylesheet.tdl` |
| Disabled | text `on_surface` at 38 percent, out of the Tab order, no pointer response, no underline | `Link_Stylesheet.tdl`, [[State Layers]] |
| Truncated | ends with `…`; tooltip on the link shows the full text | [[10 Layout Overflow and Scrolling]] |

## Tokens used

- Colour: `primary` (rest), `secondary` (visited), `on_surface` at 38 percent (disabled) ([[Colour Roles]]).
- Type: `body_large` by default at default density (tess-ui `body_large`, 16 on 24 dp), `body_medium` at compact and dense; any role by `Typography_Role` ([[Typography]]).
- Focus: [[Focus Ring]].
- Spacing and density: [[Spacing and Density]].

## Sizing and density

| Level | Type role | Text box height | Hit area |
|---|---|---|---|
| default | `body_large` | 24 dp | 24 dp high, the text width |
| compact | `body_medium` | 20 dp, extended to 24 dp hit area | 24 dp high |
| dense | `body_medium` | 20 dp, extended to 24 dp hit area | 24 dp high |

- tess-ui sizes the Python `link` widget 24 dp high (`tess-ui:src/tess_ui/widgets/structural.py`); the view is as high as its text line.
- A standalone link meets the 24 by 24 dp target minimum by extending its hit area above and below the 20 dp line box at compact and dense (WCAG 2.2 SC 2.5.8, [target size](https://www.w3.org/TR/WCAG22/#target-size-minimum)); the width is the text width, which is at least 24 dp for any link text of 3 characters or more; a one or two-character link pads its hit area to 24 dp wide. Inline links are exempt from the minimum (the same criterion, inline exception).
- Vertical centring by construction, as [[Text]]; the hit area is centred on the line box.

## Layout and overflow

- A standalone link is one line by default (`Wrap: none`, `Overflow: ellipsis` in the Python widget; the view default is `Wrap: word`, `Overflow: clip`, so a project sets `ellipsis` explicitly, [[Text]] AC-TXT-14). A link that can exceed its box truncates with `…` and shows its full text in a tooltip ([[10 Layout Overflow and Scrolling]], [[ADR-0004 Tooltip rule]]).
- A link in a flex row has `Min_Width 0` so it truncates before it pushes its siblings out ([[10 Layout Overflow and Scrolling]]).
- A wrapping link (`Wrap: word`) has the focus ring around each line fragment as one outline of the text box; the hit area is the union of the line boxes.
- `Text_Align`, `Max_Lines` and `Letter_Spacing` apply as in [[Text]].

## Behaviour

- Pointer: a press and release on the link activates it; a press that leaves the link before release does not; the pointer is a hand over it; the text is not selected by a click (a drag on a selectable text selects, a plain click activates).
- Keyboard: the link is a Tab stop; Enter activates; Space does not activate a link (a link is not a button; the platform convention is Enter only, [WAI-ARIA link pattern](https://www.w3.org/WAI/ARIA/apg/patterns/link/)). Shift+F10 or the Menu key opens a context menu only if the project provides one (Copy link address).

| Keys | Result |
|---|---|
| Tab, Shift+Tab | move focus to the next or previous focusable control |
| Enter | activate: open `Href`, then run `On_Click` |
| Space | no action on a link |

- Activation: `Href` is opened in the OS's browser or mail program; only `http`, `https`, `mailto` and `tel` are opened, anything else is refused with a warning logged and nothing opened. Opening sets a bound `Visited`. `On_Click` runs as well as the `Href` opens; a link without `Href` runs its handler only (`tess-ui:docs/components/links.md`).
- Confirmation for external destinations: a link that leaves the app does not ask first; a link that sends data (a `mailto` with a body, a `tel`) is the platform's to confirm.
- Touch: a tap activates; the hit area is 48 by 48 dp in a touch context ([[Spacing and Density]]).
- IME: not applicable.
- Validation hooks: not applicable (a link holds no value). A link to a rule or to help from an error message is a standalone or inline link inside the message ([[Validation]], [[Forms and Settings]]).

## Tooltip and overlay behaviour

The link carries the tooltip when its text is truncated, or when the destination differs from the label and the project chooses to show it (the destination URL): the tooltip is on the link, never on a group ([[ADR-0004 Tooltip rule]], [[Tooltip]]). A link opens no overlay of its own; a context menu is a [[Menu]] under the pointer. Showing the full address of an external link as its tooltip is recommended so that the user sees the destination before leaving the app.

## Motion

None; the underline appears at once. Reduced motion changes nothing ([[14 Accessibility Basics]]).

## Accessibility

- Role: `link` ([WAI-ARIA link](https://www.w3.org/TR/wai-aria-1.2/#link)), name from the link's text (`Text`); the Python widget sets `role="link"` (`tess-ui:src/tess_ui/widgets/structural.py`). A link inside rich text is a `link` node holding its run and its URL (`tre:docs/guide/accessibility.md`, "Text, selection and links"); its `click` action fires the text node's `link` event.
- The name states the destination or purpose out of context ([WCAG 2.4.4](https://www.w3.org/TR/WCAG22/#link-purpose-in-context)); two links with the same name go to the same place ([WCAG 3.2.4](https://www.w3.org/TR/WCAG22/#consistent-identification)).
- States exposed: `disabled`, `visited` (where the platform has it), focused.
- Colour is not the only cue: inline links are underlined always; a standalone link's underline appears on hover and focus, and its colour has a contrast of at least 3 to 1 against the surrounding text colour or an always-on underline ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)). In the Tesserae roles `primary` on `surface` is 4.5 to 1 or more; against `on_surface` body text the 3 to 1 difference is not guaranteed, so inline links use the underline #needs-verification: contrast between `primary` and `on_surface` is to be measured by the contrast script.
- Focus ring: 3 dp `secondary` ring with 3 to 1 contrast against the surface ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); never clipped by a scroll container ([[Focus Ring]]).
- Contrast: link text 4.5 to 1 on its container in rest, visited and focus; disabled is exempt.
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

The colours are roles; the scheme recomputes them ([[Theme Following the System]]). AC-LNK-8 checks contrast in both.

## Defaults

- `body_large` text (default density), `primary`, `Underline: hover`, not visited, enabled.
- No `Href` (handler only) unless given.
- Python widget: 24 dp high, `Wrap: none`, `Overflow: ellipsis`.

## Acceptance criteria

- [ ] AC-LNK-1 (token test): the rest colour is the role `primary`, visited `secondary`, disabled `on_surface` at 38 percent; the stylesheet holds no literal colour. Pass: every colour property is a role reference with these roles.
- [ ] AC-LNK-2 (scripted input): Tab focuses the link; Enter activates it once: the `Href` is passed to the OS opener once for `https://example.com`, `mailto:a@b.c` and `tel:+1555`, `On_Click` runs once, and a bound `Visited` becomes true. Space does nothing. Pass: opener calls, handler calls and `Visited` equal.
- [ ] AC-LNK-3 (scripted input): a link with `Href` `file:///etc/passwd`, `javascript:alert(1)` or `ftp://x` opens nothing and logs one warning; the handler still runs if one is set. Pass: opener call count 0, warning count 1.
- [ ] AC-LNK-4 (scripted input): a pointer press and release on the link activates it once; a press on the link with release outside does not; a disabled link takes no focus, no Tab stop, no click and does not open its `Href`. Pass: activation counts equal.
- [ ] AC-LNK-5 (pixel check): with `Underline: hover` no underline pixels in the rest state; underline pixels exist under the text while hovered and while keyboard-focused; with `always` they exist in all states; with `never` in none; inline link runs are underlined in all states. Pass: underline row coloured pixels count zero or above 80 percent of the text width as stated.
- [ ] AC-LNK-6 (geometry check): the hit area of a standalone link is at least 24 by 24 dp at default, compact and dense (48 by 48 dp in a touch context); a one-character link has a hit area 24 dp wide; the text is centred vertically in its hit area within 0.5 dp. Pass: sizes at or above the limits.
- [ ] AC-LNK-7 (geometry check and scripted input): a link 3 times wider than its box with `Wrap: none` ends with `…`, no pixel lies outside the box, and the tooltip shows the full text; a short link shows no tooltip beyond the destination option. Pass: ellipsis, zero overflow pixels, tooltip text equal.
- [ ] AC-LNK-8 (contrast script): in light and dark, `primary`, `secondary` (visited) and the focus ring against `surface` and `surface_container` meet 4.5 to 1 for text and 3 to 1 for the ring; the contrast between `primary` and `on_surface` is reported and, where it is below 3 to 1, inline links are underlined always. Pass: ratios at or above the limits and the underline rule holds.
- [ ] AC-LNK-9 (AT tree assertion): the link node has role `link`, a non-empty name equal to its text, `disabled` set when disabled; a link run in rich text has a `link` node with its URL as value and its `click` action fires the `link` event with `href`. Pass: all properties equal.
- [ ] AC-LNK-10 (pixel check): the focus ring is 3 dp wide, 2 dp offset, role `secondary`, and is not clipped by a scroll container ancestor. Pass: ring pixels complete on all sides.
- [ ] AC-LNK-11 (geometry check): hover over a link for 600 ms shows a tooltip only when the text is truncated or the project enables the destination tooltip; hover over a group of links shows none ([[ADR-0004 Tooltip rule]]). Pass: tooltip count per case equal.
- [ ] AC-LNK-12 (review): within one project two links with the same text have the same destination, and no link text is "click here", "here" or "more" alone. Pass: reviewer finds none.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Link_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/structural.py` (`link`), `tess-ui:docs/components/links.md`, `tess-ui:docs/guide/rich-text.md` | partly meets: `primary`, `secondary` visited, disabled `on_surface` at 0.38 opacity (AC-LNK-1 meets as the stylesheet reads: opacity 0.38 on `on_surface`), `Href` allow-list of `http`, `https`, `mailto`, `tel` (AC-LNK-3 meets as documented), `Visited`, `Underline` hover, always, never, Tab stop and Enter (AC-LNK-2, AC-LNK-4, AC-LNK-5 meet as documented, unmeasured), `role="link"` in the Python widget; no density setting, 24 dp high widget (AC-LNK-6 partly meets; compact and dense hit area not specified); the view default `Overflow: clip` (AC-LNK-7 fails unless set); inline link runs are underlined by default; no external-link glyph; Space handling and destination tooltip not documented; no app or example uses `Link` (Inventory), so unmeasured in context |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (`On_Link` on `Text`), `shell-vault:41 TDL Reference/Block Reference.md` | partly meets: link spans inside `Text` with `On_Link`; no standalone Link block (AC-LNK-2, AC-LNK-5, AC-LNK-6 absent for a standalone link) |
| tre | `tre:docs/guide/text.md` (links), `tre:docs/guide/accessibility.md` | meets as the primitive: a span with a `link` fires a `link` event with `href`, hand cursor, accessible `link` node with its URL and a `click` action; the engine opens nothing and draws no underline or colour by itself |

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Link_Stylesheet.tdl`, `tess-ui:docs/components/links.md` | exists, partial |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` | link spans only |
| tre | `tre:docs/guide/text.md` | engine primitive |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no link component | text that navigates is needed in help, about and settings | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Space does not activate a link, only Enter | link keyboard convention (WAI-ARIA link pattern) | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Underline on hover and focus for a standalone link; always for inline | colour must not be the only cue | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hit area extended to 24 dp at compact and dense | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- tess-ui link documentation: `tess-ui:docs/components/links.md`, `tess-ui:docs/guide/rich-text.md`.
- tre links and accessibility: `tre:docs/guide/text.md`, `tre:docs/guide/accessibility.md`.
- [WAI-ARIA APG link pattern](https://www.w3.org/WAI/ARIA/apg/patterns/link/): role link, Enter activates.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.1, 1.4.3, 1.4.11, 2.4.4, 2.5.8, 3.2.4.
- [Material Design 3 colour roles](https://m3.material.io/styles/color/roles): a script-rendered page that the tools could not read; the use of `primary` for links is the tess-ui choice and is marked #needs-verification against MD3.
