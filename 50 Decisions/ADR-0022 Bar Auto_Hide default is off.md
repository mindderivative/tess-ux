---
title: ADR-0022 Bar Auto_Hide default is off
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Auto Hide]]", "[[Bar]]", "[[ADR-0021 Shortcut Mode reveals a hidden Bar]]"]
depends_on: []
---

# ADR-0022 Bar Auto_Hide default is off

> [!important] Status
> `accepted`: decided by the owner on 2026-11-21, recorded by bot:Orchestrator. It supersedes the default of the owner's decision of 2026-10-27 ("auto-hide on by default, opt out with `Auto_Hide: false`").

## Context

The Bar specification of 2026-10-27 made auto-hide the default: a Bar written without `Auto_Hide` hid itself after the pointer left it. The feature is not built yet. Auto-hide hides a surface that carries status the user may need ([[Auto Hide]]), needs the Shortcut Mode reveal of [[ADR-0021 Shortcut Mode reveals a hidden Bar]] to stay keyboard reachable, and surprises an application author who wrote a plain Bar.

## Options

1. `Auto_Hide` is off by default and an application opts in with `Auto_Hide: true` (chosen)
2. On by default with `Auto_Hide: false` to opt out (the 2026-10-27 default)

## Decision

The Bar `Auto_Hide` default is `false`. A Bar written without `Auto_Hide` is always shown, as today. An application opts in with `Auto_Hide: true`. The other defaults are unchanged: `Auto_Hide_Delay` 1000 ms (proposed), `Reveal_Key` none, `Visible` true. ADR-0021 applies to a Bar that has opted in.

## Consequences

- The shell default does not change behaviour while `Auto_Hide` is not built; building it adds no surprise for existing configurations.
- AC-AHD-1 checks the new default; AC-AHD-2 checks both the default and the opt-in; AC-AHD-3 to AC-AHD-21 assume a Bar with `Auto_Hide: true`.
- The Auto Hide and Bar notes, the deviation register and the shell adoption worklist (TSH-010, TSH-050) carry the change; Shortcut Mode must still reveal a Bar that opted in.

## Affected notes

- [[Auto Hide]]
- [[Bar]]
- [[Adoption tess-shell]]
