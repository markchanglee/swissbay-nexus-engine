---
feature_id: NX-003
title: Roadmap Command
status: ready_for_test
version: 0.1.2
branch: feature/NX-003-roadmap-command
depends_on:
  - NX-002-registry-command
---

# NX-003 — Roadmap Command

## Purpose

Adds a `roadmap` command to the Nexus Engine.

## Business Value

The roadmap command helps Mark see what exists, what is completed, and what is next without opening YAML files manually.

## Files Changed

- `python/engine/roadmap.py`
- `nexus.py`
- `docs/features/NX-003-roadmap-command.md`
- `docs/releases/CHANGELOG.md`

## Test Command

```powershell
python nexus.py roadmap
```

## Expected Result

The command should print:

- Project details
- Progress summary
- Next planned items
- Completion by section
- `Roadmap Loaded Successfully`

## Acceptance Criteria

- [ ] `python nexus.py roadmap` runs without crashing.
- [ ] Reads `config/registry.yaml`.
- [ ] Displays project name and version.
- [ ] Displays item count.
- [ ] Displays progress.
- [ ] Displays next planned items.
- [ ] Displays completion by section.
- [ ] Returns success exit code.
