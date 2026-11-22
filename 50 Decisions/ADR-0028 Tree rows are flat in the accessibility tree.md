---
title: ADR-0028 Tree rows are flat in the accessibility tree
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Tree]]", "[[Tree Node]]", "[[Selection]]", "[[List]]", "[[14 Accessibility Basics]]"]
depends_on: []
---

# ADR-0028 Tree rows are flat in the accessibility tree

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-22, so that tess-ui's flat Tree can merge. Two claims stay UNVERIFIED until the owner has made a real screen-reader pass (Orca on KDE) over one flat tree (open owner check): that a flat tree reads as well as a nested one, and that tre exposes level, set size and position in set to the screen reader. They come from the WAI-ARIA text and the APG tree pattern and from the tre notes, not from a test with a screen reader (the vault records no screen-reader run, [[14 Accessibility Basics]]). If the pass shows a loss, this ADR is reopened.

## Context

[[Tree]] (AC-TRE-10) puts the children of each open branch inside an element of role `group`. tess-ui's multi-selection on the Tree needs one container of visible rows: the engine's container selection ranges over the direct children of one container, and a nested tree would need the engine to select across descendants in tree order.

## Options

1. Flat accessibility tree: the visible rows are direct children of the tree, each with `aria-level`, `aria-setsize` and `aria-posinset`; no `group` wrapper (chosen)
2. Nested tree with `group` wrappers, and the engine selects across descendants in tree order

## Decision

- The visible rows of a tree are direct children of the node with role `tree`. The children of an open branch follow it in tree order; the children of a closed branch are not in the tree.
- Every row has role `treeitem`, `aria-level` (1 for roots, plus 1 per depth), `aria-setsize` and `aria-posinset` (the number of siblings under the same parent and the position among them, not the count of all visible rows), `aria-expanded` on branches only, and `aria-selected` on selectable rows.
- No `group` wrapper is required. The APG tree pattern allows this flat form when each treeitem carries level, set size and position in set.

## Consequences

- [[Tree]]: anatomy item 2, the accessibility section, AC-TRE-10 and AC-TRE-12 change, and a deviation row records the choice. [[Tree Node]] changes: `aria-setsize` and `aria-posinset` always, and AC-TRN-14.
- What a screen-reader user loses (inference, not tested): the structural link to the parent (a reader cannot jump to the parent by structure; the Left key still does, AC-TRE-05) and a possible "group" cue on entering a branch. What is kept: level, set size and position are announced from the row attributes.
- Risk: tre must expose level, set size and position in set. The tre adoption note records `level` and no set size or position in set (TRE-009); a later tre release is reported to add them, not re-checked.
- [[Selection]] rule 8 and AC-SLT-7 (range and Select all over visible nodes) need no change; the flat container is the natural form for them.

## Affected notes

- [[Tree]]
- [[Tree Node]]
