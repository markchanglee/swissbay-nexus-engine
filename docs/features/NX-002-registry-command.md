---
feature_id: NX-002
title: Registry Command
status: ready_for_test
version: 0.1.2
branch: feature/NX-002-registry-command
depends_on:
  - NX-001-doctor-command
---

# NX-002 — Registry Command

## Purpose

Adds a `registry` command to the Nexus Engine.

## Business Value

The registry is the source of truth for what Nexus knows must be built.

## Files Changed

- `config/registry.yaml`
- `python/engine/registry.py`
- `nexus.py`
- `docs/features/NX-002-registry-command.md`
- `docs/releases/CHANGELOG.md`

## Test Command

```powershell
python nexus.py registry
```

## Expected Result

The command should print project details, registered objects, departments, agents, workflows, dashboards, standards, and statistics.

## Acceptance Criteria

- [ ] `python nexus.py registry` runs without crashing.
- [ ] Reads `config/registry.yaml`.
- [ ] Displays project name and version.
- [ ] Displays Business Objects.
- [ ] Displays Departments.
- [ ] Displays AI Agents.
- [ ] Displays Workflows.
- [ ] Displays Dashboards.
- [ ] Displays Standards.
- [ ] Shows statistics.
- [ ] Handles empty sections without crashing.
