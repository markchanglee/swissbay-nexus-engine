---
feature_id: NX-006.1
title: Object Builder Core
status: ready_for_test
version: 0.2.0
branch: feature/NX-006-1-object-builder-core
depends_on:
  - NX-005-review-command
---

# NX-006.1 — Object Builder Core

## Purpose

Adds the first `create` command to the Nexus Engine.

## Business Value

This command creates a Business Object markdown file from registry metadata, making future Nexus object creation more consistent.

## Files Changed

- `python/engine/object_builder.py`
- `nexus.py`
- `docs/features/NX-006-1-object-builder-core.md`
- `docs/releases/CHANGELOG.md`

## Test Command

```powershell
python nexus.py create Customer_Object
```

## Expected Result

The command should create:

```text
vault/03_BUSINESS_OBJECTS/01_Customer_Object.md
```

## Acceptance Criteria

- [ ] `python nexus.py create Customer_Object` runs without crashing.
- [ ] Reads `config/registry.yaml`.
- [ ] Finds `Customer_Object`.
- [ ] Creates the correct folder if missing.
- [ ] Creates the object Markdown file.
- [ ] Does not overwrite an existing object file.
- [ ] Adds basic metadata and required headings.
