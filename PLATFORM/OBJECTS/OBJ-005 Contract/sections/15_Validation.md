# 15 — Validation

---

# Overview

The Contract Validation Model ensures every Contract record is complete, accurate, authorised and governed before it progresses through lifecycle stages.

---

# Validation Categories

- Identity Validation
- Counterparty Validation
- Date Validation
- Commercial Validation
- Legal Validation
- Obligation Validation
- Approval Validation
- Security Validation
- AI Validation

---

# Identity Validation

Every Contract must contain Contract Identifier, Contract Name, Contract Type, Contract Status and Contract Owner.

Identifiers must be unique and immutable.

---

# Counterparty Validation

Every Contract must have at least one valid Counterparty. Counterparty references must point to governed Business Objects where applicable.

---

# Date Validation

Effective Date must be valid. Expiry Date must not be before Effective Date unless contract type allows no expiry. Renewal Notice Date must occur before Expiry Date.

---

# Commercial Validation

Contract Value, Currency, Payment Terms and Pricing Terms must be valid where applicable.

---

# Legal Validation

High-risk Contract Types must require Legal review. Non-standard clauses must require approval.

---

# Obligation Validation

Material obligations must have owner, due date where applicable, status and evidence requirements.

---

# Approval Validation

Contracts may not move to Executed unless required approvals are complete.

---

# Security Validation

Access to Contract information must follow confidentiality classification and role permissions.

---

# AI Validation

AI outputs must cite supporting clauses, confidence score and related rules.

---

# Validation Severity

| Severity | Meaning |
|---|---|
| Critical | Contract blocked |
| High | Workflow blocked |
| Medium | Warning issued |
| Low | Advisory only |

---

# Validation Summary

Contract validation protects legal integrity, commercial accuracy and governance throughout the Contract lifecycle.
