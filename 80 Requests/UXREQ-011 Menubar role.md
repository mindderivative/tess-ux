---
title: UXREQ-011 Menubar role
type: request
status: proposed
owner: phil
created: 2026-11-28
updated: 2026-11-28
tags: [request, uxreq, accessibility]
related: ["[[Menu Bar]]", "[[Menu]]", "[[Menu Item]]", "[[Toolbar]]", "[[UXREQ-004 Accessibility roles]]", "[[Accessibility Tree]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: ["[[UXREQ-004 Accessibility roles]]"]
---

# UXREQ-011 Menubar role

> [!important] Status
> `proposed`. Owner project: tess-re (tre). Consumer: tess-ui (the configuration application, [[Config App Layout]]) and later tess-shell. Routed through bot:Orchestrator; the vault does not contact tess-re.

## Principle

[[ADR-0020 The engine never blocks the design]]: the role is a node property set from Python (`role`), a closed vocabulary extended in the engine, with no per-frame Python. Same form as [[UXREQ-004 Accessibility roles]].

## Need

The desktop [[Menu Bar]] has the structure `menubar` containing `menuitem` titles, each opening a `menu` of `menuitem`, `menuitemcheckbox` and `menuitemradio` entries ([[Menu Bar]] AC-MBR-2; WAI-ARIA Authoring Practices menubar pattern). The tre role list (`tre:docs/reference/node.md`, read at `origin/main`) has `menu` and `menuitem` and, since 0.6.11, `toolbar`, but not `menubar`. Without it the bar is a `group`, which a screen reader announces as a plain group and not as an application menu bar, and a user cannot jump to it by the menu bar landmark of the platform.

## Request

1. Add the role `menubar` to the vocabulary and map it to the platform role (AccessKit has a menu bar role). An unknown name keeps raising the existing error.
2. Confirm that `menuitemcheckbox` and `menuitemradio` exist or add them (the list in `node.md` shows `menuitem` only; check items need `checked`). If they exist under other names, say which.
3. Confirm the menu items can expose a popup flag and `expanded`, which the bar titles need (`haspopup`, `expanded`); if `expanded` already exists on a node ([[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]), a statement is enough.

Not requested: the engine already has a settable `active_descendant` on any node (TRE-REQ-023, `tre:LOG.md`). The menu can use it to expose the highlighted item without moving focus. One open point is a check, not a feature: the log says AccessKit 0.25 sends the focused state moving between rows and not an `ActiveDescendantChanged` event, and that the result was not tried with Orca or NVDA. A pass with Orca on the configuration application's menus settles it ([[Accessibility Tree]]).

## Acceptance

[[Menu Bar]] AC-MBR-2 and [[Config App Layout]] AC-CFG-9: a node created with the role `menubar` appears in the accessibility tree with that role, its `menuitem` children carry the popup flag and `expanded`, and a check or radio entry carries `checked`. A tre-level test passes when the role maps and an AT-SPI probe lists a menu bar.

## Out of scope

The bar's keys, mnemonics and Alt activation (framework code: [[Menu Bar]] and the tess-behavior candidate in SPEC 2.5c); which role the toolkit sets (tess-ui code).

Back to [[80 Requests]].
