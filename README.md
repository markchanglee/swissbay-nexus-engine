# Swissbay Nexus Engine v0.1.0

This is the first local engine for Swissbay Nexus.

Flow:

```text
Python
  ↓
Context Engine
  ↓
OpenAI
  ↓
Markdown Draft
  ↓
Review
  ↓
Approve / Revise / Reject
```

## What it does now

- Loads project context from `vault/00_CONTEXT`
- Uses `context_registry.yaml` to decide what context belongs to each file
- Builds a complete AI prompt
- Calls OpenAI
- Writes draft Markdown into `outputs/`
- Validates required Markdown sections

## What it does not do yet

- It does not auto-commit to Git.
- It does not create PRs yet.
- It does not modify approved vault files automatically.
- It does not run in the background.

That is intentional. You stay in control.

## First command to try

```powershell
python nexus.py build Customer_Object
```

Draft output:

```text
outputs/Customer_Object_DRAFT.md
```
