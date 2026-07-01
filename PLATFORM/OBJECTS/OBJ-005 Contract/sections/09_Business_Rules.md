# 09 — Business Rules

---

# Overview

Business Rules define the governance, legal, commercial and operational constraints that control the Contract Business Object.

---

# Rule Categories

- Identity Rules
- Counterparty Rules
- Approval Rules
- Lifecycle Rules
- Obligation Rules
- Amendment Rules
- Renewal Rules
- Security Rules
- AI Rules
- Audit Rules

---

# Identity Rules

## BR-CON-001

Every Contract must have one unique Contract Identifier.

## BR-CON-002

Contract Identifiers cannot be changed or reused.

## BR-CON-003

Every Contract must have a Contract Name, Contract Type, Contract Owner, Counterparty, Effective Date and Contract Status.

---

# Counterparty Rules

## BR-CON-004

Every Contract must have at least one valid Counterparty.

## BR-CON-005

Counterparty references must point to governed Business Objects where applicable.

---

# Approval Rules

## BR-CON-006

Contracts may not be executed until all required approvals are completed.

## BR-CON-007

Approval requirements may depend on contract value, risk rating, contract type, counterparty and deviation from standard terms.

## BR-CON-008

AI may recommend approval but may never approve Contracts.

---

# Lifecycle Rules

## BR-CON-009

Every Contract must exist in one lifecycle stage at a time.

## BR-CON-010

Executed Contracts cannot return to Draft status.

---

# Obligation Rules

## BR-CON-011

Material obligations must have an owner.

## BR-CON-012

Overdue obligations must trigger review.

---

# Amendment Rules

## BR-CON-013

Executed Contracts may only be changed through a governed amendment process.

---

# Renewal Rules

## BR-CON-014

Contracts with expiry dates must be reviewed before expiry.

## BR-CON-015

Auto-renewal clauses must be explicitly identified.

---

# Security Rules

## BR-CON-016

Contracts are confidential by default.

## BR-CON-017

Sensitive clauses and financial terms require restricted access.

---

# AI Rules

## BR-CON-018

AI may summarise, extract obligations, compare clauses and identify risks.

## BR-CON-019

AI may not execute, amend, terminate, approve or provide final legal advice.

---

# Audit Rules

## BR-CON-020

Every significant Contract action must record user, timestamp, previous value, new value, reason and workflow.

---

# Rule Summary

These Business Rules establish the official contract governance logic for Swissbay Nexus.
