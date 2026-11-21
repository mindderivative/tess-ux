---
title: Badge
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, communication, badge]
related: ["[[Icon Button]]", "[[Button]]", "[[Tooltip]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Anchored Placement]]", "[[Notifications]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Anchored Placement]]"]
---

# Badge

> [!info] Summary
> A small mark on the corner of an element that shows there is news: a dot, or a pill with a short count or text. Counterpart: Material Design 3 [Badges](https://m3.material.io/components/badges/overview). Source of truth in code: see Status in code.

## Purpose

A badge tells the user that an element they can already reach has something new (unread mail, pending updates) without a message. It never carries the only copy of the information: the host element's accessible name carries the count.

## When to use and not

- Use when: a navigation item, icon, tab or tray icon has a count or an unseen state; the count changes while the user is elsewhere.
- Do not use when: the message needs a sentence or an action (use [[Snackbar]] or [[Banner]]); the state is a status of the element itself such as selected or on (use the element's own state); the mark would label a whole list row (use text in the row).

## Anatomy

1. Mark: a pill container in `error`. With no value it is a dot (small badge); with a value it is a large badge.
2. Label (large badge only): the count or a few characters in `label_small`, colour `on_error`.
3. Host: the element the badge sits on (icon, icon button, tab, tray item). The badge is a sibling placed over the host's top end corner ([[Anchored Placement]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Small (dot) | something is new, no number | 6 dp circle, no label |
| Large | a count or at most 4 characters | 16 dp high pill, grows with the label; count above `max` shows `max` and a plus |
| Hidden zero | count 0 | not drawn unless the project asks to show zero |

## States

A badge is not interactive: it has no hover, focus, pressed or dragged layer and takes no focus or pointer events (it must not steal the host's hover or press). It has two visible states, shown and hidden, plus a disabled look when its host is disabled.

| State | Visual change | Token values |
|---|---|---|
| Shown | mark and label drawn | container `error`, label `on_error` |
| Hidden (count 0 or flag off) | not drawn, takes no room | none |
| Host disabled | mark at 38 percent opacity so it reads as inactive | opacity 0.38 ([[State Layers]], disabled content) |

Colour is not the only cue: the dot's presence and the pill's digits carry the meaning ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

| Part | Token | Value | Source |
|---|---|---|---|
| Small container size | `md.comp.badge.size` | 6 dp | [Material Web latest `_md-comp-badge.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-badge.scss) |
| Large container size | `md.comp.badge.large.size` | 16 dp (height and minimum width) | same |
| Container colour (both) | `error` | #B3261E light, #F2B8B5 dark | [[Colour Roles]] |
| Label colour | `on_error` | #FFFFFF light, #601410 dark | [[Colour Roles]] |
| Label type | `label_small` | 11 dp, line 16, weight 500, tracking 0.5 | [[Typography]] |
| Shape | `full` | pill | [[Shape]] |

Contrast of the label on the container, computed for this note from the role values: 6.5 to 1 light and 7.7 to 1 dark, above the 4.5 to 1 text limit ([WCAG 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum)). Contrast of the mark against the page surface is checked per host surface in AC-BDG-6.

## Sizing and density

A badge marks a host; it is not a control row, so its size does not scale with the density level. The host scales ([[Spacing and Density]]); the badge keeps one size at every level so it stays legible and recognisable.

| Level | Small | Large height | Large width | Horizontal padding in a large badge |
|---|---|---|---|---|
| default | 6 | 16 | max(16, label width + 8) | 4 |
| compact | 6 | 16 | same | 4 |
| dense | 6 | 16 | same | 4 |

- A badge is decoration, so it has no pointer target of its own and no 24 dp minimum ([WCAG 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum) applies to controls); it never covers more than the host's corner so the host's hit area stays usable.
- Large width formula: label width plus 8 dp (4 each side), at least 16 dp, so a single digit is a circle. tess-ui approximates the label width as 6 dp per character plus 8.

## Layout and overflow

- Placement is a corner of the host, set by anchored placement and not by flow: the badge takes no room in the host's layout ([[Anchored Placement]]).
- Offsets used by tess-ui, from the Material Design 3 guidance #needs-verification (m3.material.io is unreadable by tools): a small badge's left edge is 4 dp inside the host's right edge and its top is on the host's top edge; a large badge's left edge is 12 dp inside the host's right edge and 4 dp above the host's top edge.
- The badge is clipped by nothing but the window: a host at the window edge keeps the badge inside the window by moving the badge inward, never by clipping the label.
- Overflow of the label: the count above `max` shows `max` plus `+` (default `99+`); text longer than 4 characters is truncated by the caller, not by the badge, and the badge never wraps or scrolls.
- Vertical centring: the label line box (16 dp for `label_small`) is centred in the 16 dp height; the digits sit on the centre within 1 px.

## Behaviour

- Pointer: none. The badge is hit-test transparent; hovering it hovers the host.
- Keyboard: none. The badge is never in the Tab order.
- Touch: none; the host's touch target is unchanged.
- Updates: a changed count replaces the label at once; no count animation.

## Tooltip and overlay behaviour

A badge carries no tooltip ([[ADR-0004 Tooltip rule]]): the tooltip belongs to the host control, and the host's tooltip text includes the count when the count matters ("Inbox, 3 unread"). A badge opens no overlay.

## Motion

Appear and disappear are immediate. A project that wants a 100 ms (`short2`) scale-in uses `standard` easing and no motion under reduced motion ([[Motion]]). Never a looping or pulsing animation: a pulsing badge is auto-moving content ([WCAG 2.2.2](https://www.w3.org/TR/WCAG22/#pause-stop-hide)).

## Accessibility

- Role: none. The badge is hidden from the accessibility tree (decoration).
- Name: not applicable. The host's accessible name or description carries the information: "Mail, 3 unread". The host updates its name when the count changes. The name text starts with the visible label of the host ([WCAG 2.5.3](https://www.w3.org/TR/WCAG22/#label-in-name)).
- Announcement: a changed count is not announced by the badge. If the change matters while the host is not focused, the project raises a polite announcement through [[Notifications]]; the badge adds none.
- A count above `max` is exposed by the host as the true count when known ("1204 unread") or as "more than 99 unread"; the visible `99+` alone is not the accessible text.
- Contrast: label 4.5 to 1; mark 3 to 1 against the surface it sits on ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)).

## Dark and light

Roles only (`error`, `on_error`); the pair keeps at least 4.5 to 1 in both schemes. High contrast uses the high-contrast `error` pair of [[Colour Roles]].

## Defaults

No value means small; `max` 99; zero hidden; not anchored unless the caller anchors it; `label_small`; roles `error` and `on_error`.

## Acceptance criteria

- [ ] AC-BDG-1 (token test): the small badge is 6 by 6 dp with radius `full`; a large badge is 16 dp high with a minimum width of 16 dp, label `label_small` (11 dp), colours `error` and `on_error` (roles, no literals), at all three density levels (same values). Pass: all equal at scale 1.0 and 2.0.
- [ ] AC-BDG-2 (geometry check): a one-character large badge is 16 by 16 dp; a two-character badge is label width plus 8 dp wide (within 0.5 dp); the label line box is centred vertically within 1 px.
- [ ] AC-BDG-3 (geometry check): anchored to a 24 by 24 dp host, a small badge's left edge is 4 dp inside the host's right edge and its top at the host's top; a large badge's left edge is 12 dp inside and its top is 4 dp above (#needs-verification of the source values; the test pins the Tesserae values). Pass: equal within 0.5 dp.
- [ ] AC-BDG-4 (scripted input): with `max` 99 a count of 99 shows `99`, 100 shows `99+`; a count of 0 draws nothing and takes no layout room; with show-zero set it draws `0`. Pass: the drawn text and the host's layout bounds equal.
- [ ] AC-BDG-5 (AT tree assertion): the badge node is hidden from the tree (no role, no name); the host's name contains the count text ("3 unread") and is updated within one frame of the count change. Pass: tree walk finds no badge node and the host name equals the expected string.
- [ ] AC-BDG-6 (contrast script): `on_error` on `error` at least 4.5 to 1 and `error` against each of `surface`, `surface_container` and `surface_container_high` at least 3 to 1, in light, dark and high contrast. Pass: no ratio below the limit (the 3 to 1 mark contrast may fail on some containers: record the exception, #needs-verification).
- [ ] AC-BDG-7 (scripted input): a pointer press on the badge area activates the host exactly once, the badge takes no focus, and Tab never stops on it. Pass: host event count 1 and the Tab sequence excludes the badge.
- [ ] AC-BDG-8 (scripted input): with reduced motion on, and with it off, a count change redraws within one frame and the badge has no running animation. Pass: zero animations on the badge node.
- [ ] AC-BDG-9 (pixel check): with the host disabled the mark is drawn at 38 percent opacity (colour within 2 levels of the composite). Pass: pixel equals.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Badge_View.tdl`, `tess-ui:src/tess_ui/views/Badge_Stylesheet.tdl`, `tess-ui:docs/components/badges.md` | partly meets: 6 dp dot and 16 dp pill in `error` with `on_error` in `label_small`, hidden from the screen reader, anchored offsets as in AC-BDG-3 (AC-BDG-1, AC-BDG-3, AC-BDG-5 meet by reading the sheet, unrun); the default `Limit` is 999 and the pill width is 8 + 6 per character, so AC-BDG-4 and AC-BDG-2 fail; no disabled look (AC-BDG-9 fails); literal corner radii 3 and 8 not the `full` token (AC-BDG-1 partly) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Badge/Badge_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: hidden from assistive technology, `Max` default 99 and `99+` (AC-BDG-4 meets by reading), zero hidden; dot is 8 by 8 and the pill 18 high with 11 px weight 600 text, not 6 and 16 (AC-BDG-1 and AC-BDG-2 fail); the label colour is `on_primary` on an `error` fill, not `on_error` (AC-BDG-6 fails or is unmeasured for the dark scheme); disabled look is opacity 0.5, not 0.38 (AC-BDG-9 fails) |
| tre | none: composed from box and text nodes with absolute placement (`tre:docs/guide/nodes-and-layout.md`, Absolute positioning) | not applicable |

Evidence: [[Gaps and Contradictions]] (shell modules use pixel literals; Badge corner radius a token).

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Badge_View.tdl` | exists |
| tess-shell | `tess-shell:src/tess_shell/shipped/Badge/Badge_Module.tdl` | exists |
| shell vault | `shell-vault:50 Design System/Standard Modules.md` (Badge) | design intent: count, `99+`, dot, hidden zero |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Badge size does not scale with density | a badge is decoration on a host; shrinking it below 6 or 16 dp would lose legibility | [[ADR-0002 Desktop density levels and target sizes]] |
| Default `max` 99 (MD3 gives no limit; Android truncates only when set) | two of three projects and the shell design use 99; the pill stays at most 4 characters wide | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Badge carries no tooltip and no live announcement | the host owns the name, tooltip and announcement | [[ADR-0004 Tooltip rule]] |
| Disabled host dims the badge to 38 percent | state rule of [[State Layers]]; MD3 gives no badge disabled state | [[ADR-0009 State layer percentages]] |

## Sources

- [Material Web badge tokens (latest)](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-badge.scss): `size` 6 px, `large.size` 16 px, colours `error` and `on-error`, label `label-small`, shape `corner-full`. Verified 2026-11-21.
- [Material Components Android BadgeDrawable](https://github.com/material-components/material-components-android/blob/master/docs/components/BadgeDrawable.md): number versus text, `maxNumber`, content description of the host with a number and when the number exceeds the maximum, offsets.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.3, 1.4.11, 2.2.2, 2.5.3, 2.5.8.
- Code: `tess-ui:docs/components/badges.md`, `tess-shell:docs/guide/modules.md` (Badge). The m3.material.io badge page could not be fetched; the placement offsets are tess-ui values #needs-verification.
