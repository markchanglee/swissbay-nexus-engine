# 02 — Data Principles

## Principle 1 — Names Are Not IDs

Names can change. IDs should remain stable.

Example:

A customer may change its trading name, but its Customer ID must remain the same.

## Principle 2 — Data Must Have an Owner

Every important data field should have a responsible owner.

Example:

Finance owns payment terms. Sales may view them, but should not change them without approval.

## Principle 3 — Use Controlled Values Where Possible

Statuses, categories and types should use controlled lists instead of free text.

## Principle 4 — Separate Facts From Notes

A field such as `payment_terms` is a fact. A field such as `finance_notes` is a note.

AI and reporting should rely more heavily on facts than informal notes.

## Principle 5 — Data Must Be Fit for Use

Do not collect data only because it is possible. Collect data because it supports a workflow, report, decision, automation or compliance requirement.

## Principle 6 — Capture Once, Reuse Many Times

The same data should not be manually re-entered in many places unless there is a strong reason.

## Principle 7 — Human Readable and Machine Usable

Data should be readable by staff and structured enough for automation, dashboards and AI agents.
