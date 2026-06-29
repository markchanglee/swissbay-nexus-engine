# 05 — Relationships

## Purpose

Relationships explain how business objects connect.

## Relationship Examples

```text
Customer has many Quotes
Quote belongs to one Customer
Quote contains many Products
Invoice belongs to one Sales Order
Supplier supplies many Products
```

## Relationship Rules

Relationships must be explicit.

Do not rely on assumptions.

## Relationship Types

| Relationship | Meaning |
|---|---|
| one-to-one | One object connects to one object |
| one-to-many | One object connects to many objects |
| many-to-many | Many objects connect to many objects |
| parent-child | One object owns or governs another |
| reference | One object refers to another |

## Obsidian Linking

Where possible, use Obsidian links:

```markdown
[[OBJ-001-Customer]]
[[OBJ-002-Supplier]]
[[OBJ-003-Product]]
```

## AI Usage

AI agents should use defined relationships instead of inventing connections.
