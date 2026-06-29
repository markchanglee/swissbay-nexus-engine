# 06 — Status Standards

## Purpose

Statuses define where something is in its lifecycle.

## General Status Values

- draft
- active
- inactive
- review
- approved
- rejected
- archived
- deprecated

## Customer Status Example

- prospect
- lead
- active_customer
- preferred_customer
- dormant_customer
- archived_customer

## Quote Status Example

- draft
- sent
- followed_up
- accepted
- rejected
- expired
- cancelled

## Rule

Statuses must be controlled values.

Avoid free-text statuses such as:

```text
waiting maybe
kind of done
nearly there
old one
```

## Future Automation

Status changes can trigger workflows such as reminders, approvals, follow-ups and dashboard updates.
