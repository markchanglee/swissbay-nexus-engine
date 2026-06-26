---
feature_id: NX-006.4
title: AI Assisted Object Build
status: ready_for_test
version: 0.2.0
branch: feature/NX-006-4-ai-assisted-object-build
depends_on:
  - NX-006-3-auto-linking
---

# NX-006.4 — AI Assisted Object Build

## Purpose

Adds optional AI-assisted content generation to the Object Builder.

## Test Commands

```powershell
python nexus.py create Customer_Object --force
python nexus.py create Customer_Object --force --ai
python nexus.py validate --path vault/03_BUSINESS_OBJECTS/01_Customer_Object.md
```

## Acceptance Criteria

- Template mode still works.
- AI mode runs without crashing.
- AI mode uses project context.
- Business Objects index still updates.
