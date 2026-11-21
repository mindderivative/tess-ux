---
title: ADR-0008 Publishing flow
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0008 Publishing flow

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-10 in [[Open Questions]].

## Context

Vault changes need review and the repository is public.

## Options

1. One pull request per task to `main` from branch `docs/<task>`, merged by the Orchestrator or the owner, branch deleted after merge (recommended)
2. Direct commits to `main`

## Decision

Each task is one branch `docs/<task>` and one pull request to `main`. Bots never merge. Merged branches are deleted.

## Consequences

No pushes to `main`; Obsidian's checkout stays on `main`.

## Affected notes

- [[Plan]]
