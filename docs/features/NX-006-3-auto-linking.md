---
feature_id: NX-006.3
title: Auto Linking
status: ready_for_test
version: 0.2.0
branch: feature/NX-006-3-auto-linking
depends_on:
  - NX-006-2-smart-metadata
---

# NX-006.3 — Auto Linking

## Purpose

Improves the Object Builder by adding Obsidian-style links and automatically creating a Business Objects index.

## Test Commands

```powershell
python nexus.py create Customer_Object --force
python nexus.py validate --path vault/03_BUSINESS_OBJECTS
```

## Expected Result

Creates or updates:

```text
vault/03_BUSINESS_OBJECTS/01_Customer_Object.md
vault/03_BUSINESS_OBJECTS/00_Business_Objects_Index.md
```
