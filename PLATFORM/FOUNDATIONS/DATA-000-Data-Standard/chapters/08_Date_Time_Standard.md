# 08 — Date and Time Standard

## Purpose

Dates and times must be represented consistently.

## Date Format

Use ISO date format:

```text
YYYY-MM-DD
```

Example:

```text
2026-06-26
```

## Datetime Format

Use ISO datetime where needed:

```text
YYYY-MM-DDTHH:MM:SS
```

## Timezone

Default timezone for Swissbay operations:

```text
Africa/Johannesburg
```

## Rules

- Use dates for business events such as invoice date, quote date and delivery date.
- Use datetimes for events that require a specific time, such as meetings or system logs.
- Avoid ambiguous formats like `06/07/26`.
