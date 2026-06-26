# Setup Guide

## 1. Extract the ZIP

Extract this folder somewhere like:

```text
C:\Users\<you>\Documents\Swissbay-Nexus
```

## 2. Open in Cursor

Open the full folder in Cursor.

## 3. Open vault in Obsidian

Open this folder as your Obsidian vault:

```text
Swissbay-Nexus\vault
```

## 4. Install Python packages

In PowerShell:

```powershell
./setup.ps1
```

## 5. Add API key

Open `.env` and add:

```text
OPENAI_API_KEY=your_key_here
```

Do not commit `.env`.

## 6. Build first draft

```powershell
python nexus.py build Customer_Object
```

## 7. Review

Open:

```text
outputs/Customer_Object_DRAFT.md
```

Then choose:

- Approve
- Revise
- Reject
