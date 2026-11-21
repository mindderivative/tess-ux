---
title: Empty States
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, state, empty]
related: ["[[40 Patterns]]", "[[Loading States]]", "[[Error States]]", "[[List]]", "[[Tree]]", "[[Search]]", "[[Button]]", "[[Spacing and Density]]", "[[Typography]]", "[[Colour Roles]]", "[[14 Accessibility Basics]]", "[[10 Layout Overflow and Scrolling]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]"]
---

# Empty States

> [!info] Summary
> What a container shows when it has nothing to show: a list with no rows, a search with no results, a first run with no data. Material Design 3 has no empty-state component; this pattern is Tesserae's, built from the MD3 typography and colour roles. Source of truth in code: see Status in code.

## Problem

A container with no content draws nothing and reads as broken. Three causes need different answers: there is nothing yet (first use), a query or filter matched nothing, or the content could not be read (that is an [[Error States|error]], not an empty state). The engine draws nothing for a `virtual_list` with `item_count` 0, and a module that hides itself when empty (the shell Battery module) leaves a gap in its bar ([[Gaps and Contradictions]], item 8 of the summary).

## Purpose

Tell the user in one line why the container is empty and, when one exists, give the one action that fills it.

## When to use and not

- Use when: a [[List]], [[Tree]], table, search result view, panel or form group has zero items and the user can act or wait.
- Do not use when: the content is still loading ([[Loading States]]); the load failed ([[Error States]]); the container is decorative or hidden by design (a module with nothing to show in a bar may hide itself, see the decision table).

## Rules

1. The empty state replaces the content region only. The container keeps its role, name, header, toolbar and scroll container; the focus order does not lose a stop that was there ([[14 Accessibility Basics]]).
2. The text says what is missing in the user's words, in one sentence, and never blames the user ("No results for 'abc'", not "You searched wrongly").
3. The optional action is one [[Button]] (text or tonal variant) that creates or fills the content. A second action is a link in the text, not a second button.
4. An empty state is centred in the content region, both axes, and does not scroll; at 1 line of `body_medium` it fits the narrowest container of 160 dp by wrapping at most 3 lines, then ending with an ellipsis ([[10 Layout Overflow and Scrolling]]).
5. A search or filter with no match shows the query in the text and offers "Clear filter" as the action. The result count is announced politely ([[14 Accessibility Basics]]).
6. The empty state appears only after loading ended. It never shows during [[Loading States|loading]] and it is removed in the same frame in which the first row arrives.
7. An empty state is a status message: it is announced once when it appears after a user action (typing a query, deleting the last row), not on first display of a view ([[14 Accessibility Basics]], SC 4.1.3).

## Decision table

| Situation | Show | Text role | Action | Announce |
|---|---|---|---|---|
| First use, nothing created yet, user can create | icon (optional), one-line text, action | `body_medium`, `on_surface_variant` | Create (text button) | no |
| Query or filter matches nothing | text with the query | `body_medium`, `on_surface_variant` | Clear filter | yes, polite, once per query change that ends in zero |
| Last item deleted by the user | text | `body_medium`, `on_surface_variant` | Undo is in the [[Notifications]] snackbar, not here | polite, once |
| Container filled by a source that is currently empty (no devices, no notifications) | text only | `body_medium`, `on_surface_variant` | none | no |
| A bar or panel module with nothing to show | module hides itself, bar reflows | not applicable | not applicable | no |
| Content could not be read | an error state | see [[Error States]] | Retry | polite or assertive per [[Error States]] |

## Examples (short snippets only)

```tdl
Text {
  Name: empty_text
  Text: <| 'No results for "' + query + '"' |>
  Typography_Role: body_medium
  A11y { Live: polite }
  Style { Foreground: on_surface_variant }
}
```

The shipped `SearchView` shows its `Empty` text (default `No results`) when a `Query` has no rows (`tess-ui:docs/components/search.md`).

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | text centred, no container fill | `on_surface_variant`, `body_medium` |
| With action | text above the button, gap `space.4` (12 dp) default, `space.3` (8 dp) compact, `space.2` (4 dp) dense | [[Spacing and Density]] |
| Disabled container | text 38 percent | [[State Layers]] |

## Sizing and density

The empty text uses `body_medium` at every density; only the gap to the action and the container padding scale: padding 16, 12, 8 dp at default, compact, dense (`space.5`, `space.4`, `space.3`). The action button follows the density height 40, 32, 28 dp ([[Button]]). An optional icon is 24 dp at default, 20 dp at compact and dense, role `on_surface_variant`.

## Accessibility

- The empty text is a node inside the container, not a tooltip; it is exposed as the container's description while the container is empty.
- The container keeps role `list`, `tree` or `grid` with zero children; a screen reader hears the name and the empty text.
- The action button is a normal Tab stop reached after the container.
- Colour is not the only carrier: the text states the cause.

## Acceptance criteria

- [ ] AC-EMP-1 (scripted input): a [[List]] with 0 rows after loading shows exactly one empty-state node, and the list container keeps its role, name and header. Pass: the node count is 1 and role and name equal those of a non-empty list.
- [ ] AC-EMP-2 (geometry check): the empty-state text block is centred in the content region (centre within 1 dp on both axes) at all three densities and scale 1.0 and 2.0. Pass: offsets at most 1 dp.
- [ ] AC-EMP-3 (geometry check): a text of 200 characters in a 160 dp wide container wraps to at most 3 lines, ends in an ellipsis, and no glyph pixel lies outside the container. Pass: lines at most 3, zero pixels outside.
- [ ] AC-EMP-4 (token test): the text colour is the role `on_surface_variant`, the type role is `body_medium`, and no colour literal is used. Pass: role references only.
- [ ] AC-EMP-5 (scripted input): while the data source is loading, the empty-state node is absent; the frame after the first row arrives, the node is absent and the row is present. Pass: node presence equals the sequence.
- [ ] AC-EMP-6 (AT tree assertion): typing a query that matches nothing produces exactly one polite announcement containing the query; typing one more character that still matches nothing, without the text changing meaning, produces another only once the result set changes. Pass: announcement count equals 1 per change of result set.
- [ ] AC-EMP-7 (scripted input): the action button of an empty state is reached by Tab, activates with Enter and Space, and activation removes the empty state when the content is created. Pass: focus order and counts equal.
- [ ] AC-EMP-8 (contrast script): the text against the container surface is at least 4.5 to 1 in light and dark. Pass: ratio at or above 4.5.
- [ ] AC-EMP-9 (review): no empty state uses a tooltip as the only carrier of its text, and an unreadable source is shown through [[Error States]], not as empty. Pass: reviewer checklist complete.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/SearchView_View.tdl` (`Empty`), `tess-ui:docs/components/search.md` | partly meets: `SearchView` shows `Empty` text when there is a query and no rows and announces the count politely (AC-EMP-1, AC-EMP-6 partly); no shared empty-state view for `List`, `Tree` or `ListEditor` (AC-EMP-1 fails for them); the text role and colour are not checked by a test (AC-EMP-4 unmeasured) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Battery/`, `tess-shell:src/tess_shell/shipped/List/List_Module.tdl` | partly meets: modules hide when empty (Battery), as the decision table allows; the shipped List has no empty text (AC-EMP-1 fails); Applications launcher "No results" message exists in the shell vault spec but was not measured (`shell-vault:40 Specifications/Modules/Applications Module.md`) |
| tre | `tre:docs/reference/node.md` | not applicable: a `virtual_list` with `item_count` 0 draws nothing; the empty state is framework code |

Request candidate: a shared `EmptyState` view in tess-ui and an `Empty` text param on the shell `List` module, routed through the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A pattern note for a state MD3 specifies only as illustration | desktop containers (lists, trees, result panes) need one rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| `body_medium` text and 24 dp or 20 dp icon, density-scaled gaps | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- MD3 has no empty-state component: checked in the [Material Web component list](https://github.com/material-components/material-web/tree/main/docs/components) and the [Material Components Android component docs](https://github.com/material-components/material-components-android/tree/master/docs/components), 2026-11-21. The m3.material.io guidance on empty states is not readable by tools #needs-verification.
- [WCAG 2.2 SC 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html); [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) roles `list`, `tree`, `status`.
- Code: `tess-ui:docs/components/search.md`; `tre:docs/reference/node.md`; `shell-vault:50 Design System/Standard Modules.md`; gap list [[Gaps and Contradictions]] (summary item 8, evidence "Foundations missing or thin").
