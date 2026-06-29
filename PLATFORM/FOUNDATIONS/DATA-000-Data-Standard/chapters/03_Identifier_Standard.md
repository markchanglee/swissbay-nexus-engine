# 03 — Identifier Standard

## Purpose

Identifiers allow Nexus to track business entities consistently across files, systems, workflows and reports.

## Identifier Rule

Every major business entity must have a permanent ID.

## Recommended Format

```text
CUSTOMER-000001
SUPPLIER-000001
PRODUCT-000001
LEAD-000001
OPPORTUNITY-000001
QUOTE-000001
ORDER-000001
INVOICE-000001
PURCHASE-ORDER-000001
```

## Identifier Requirements

An ID must be:

- unique
- stable
- human-readable
- system-friendly
- not based only on a name
- not reused after deletion or archiving

## Bad Examples

```text
Clover
Customer1
MarkSchool
QuoteNew
```

## Good Examples

```text
CUSTOMER-000042
QUOTE-2026-000015
PRODUCT-000319
```

## Future Automation

The Nexus Engine may later generate IDs automatically when new objects are created.
