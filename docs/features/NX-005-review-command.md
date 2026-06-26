---
feature_id: NX-005
title: Review Command
status: ready_for_test
version: 0.1.2
branch: feature/NX-005-review-command
depends_on:
  - NX-004-validate-command
---

# NX-005 — Review Command

## Purpose

Adds a `review` command to the Nexus Engine.

## Business Value

The review command creates a structured report for a generated draft before Mark approves, revises, or rejects it.

## Files Changed

- `python/engine/review.py`
- `nexus.py`
- `docs/features/NX-005-review-command.md`
- `docs/releases/CHANGELOG.md`

## Test Command

```powershell
python nexus.py review Customer_Object
```

## Expected Result

The command should create:

```text
outputs/Customer_Object_REVIEW.md
```

The review report should include:

- Target metadata
- Draft path
- Registry status
- Document stats
- Required section check
- Registry dependencies
- Review decision options

## Acceptance Criteria

- [ ] `python nexus.py review Customer_Object` runs without crashing.
- [ ] Finds the draft file from registry metadata.
- [ ] Creates a review report in `outputs/`.
- [ ] Reports missing sections.
- [ ] Shows registry metadata if available.
- [ ] Returns success exit code.
