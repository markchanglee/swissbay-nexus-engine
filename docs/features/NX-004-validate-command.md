---
feature_id: NX-004
title: Validate Command
status: ready_for_test
version: 0.1.2
branch: feature/NX-004-validate-command
depends_on:
  - NX-003-roadmap-command
---

# NX-004 — Validate Command

## Purpose

Adds a `validate` command to the Nexus Engine.

## Business Value

The validate command checks whether Markdown files follow the Nexus File Standard.

It helps prevent the vault from becoming messy as more files are created.

## Files Changed

- `python/engine/validate_command.py`
- `nexus.py`
- `docs/features/NX-004-validate-command.md`
- `docs/releases/CHANGELOG.md`

## Test Commands

```powershell
python nexus.py validate
```

Optional:

```powershell
python nexus.py validate --path outputs
python nexus.py validate --path vault --path outputs
```

## Expected Result

The command should print:

- Scan paths
- Number of Markdown files found
- Validation results
- Summary
- Passed/warning count

## Acceptance Criteria

- [ ] `python nexus.py validate` runs without crashing.
- [ ] Reads required sections from `config/config.yaml`.
- [ ] Scans `vault` and `outputs` by default.
- [ ] Supports optional `--path`.
- [ ] Reports missing required sections.
- [ ] Returns success exit code even when warnings exist.
