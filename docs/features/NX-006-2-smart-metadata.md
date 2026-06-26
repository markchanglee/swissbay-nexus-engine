---
feature_id: NX-006.2
title: Smart Metadata
status: ready_for_test
version: 0.2.0
branch: feature/NX-006-2-smart-metadata
depends_on:
  - NX-006-1-object-builder-core
---

# NX-006.2 — Smart Metadata

## Purpose

Improves the Object Builder by adding richer frontmatter metadata to generated Business Object files.

## Business Value

Smart metadata allows Nexus to later filter, review, validate, approve, report and automate files more reliably.

## Files Changed

- `python/engine/object_builder.py`
- `nexus.py`
- `docs/features/NX-006-2-smart-metadata.md`
- `docs/releases/CHANGELOG.md`

## Test Commands

```powershell
python nexus.py create Customer_Object --force
python nexus.py validate --path vault/03_BUSINESS_OBJECTS/01_Customer_Object.md
```

## Expected Result

The Customer Object file should include frontmatter fields such as:

- id
- key
- name
- type
- object_type
- status
- lifecycle_stage
- version
- owner
- source_registry
- output_path
- review_status
- approval_status
- depends_on
- related_departments
- related_ai_agents
- tags

## Acceptance Criteria

- [ ] `python nexus.py create Customer_Object --force` runs without crashing.
- [ ] Existing file is overwritten only when `--force` is used.
- [ ] Frontmatter includes smart metadata.
- [ ] Required standard headings are present.
- [ ] Validation runs after file creation.
