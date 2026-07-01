# 16 — Security

---

# Overview

The Contract Security Model defines how contract information is protected throughout its lifecycle.

Contracts contain confidential legal, commercial, financial and strategic information and must be secured accordingly.

---

# Security Principles

- least privilege
- need-to-know
- legal confidentiality
- segregation of duties
- audit by default
- encryption by default
- human accountability

---

# Data Classification

Contracts are Confidential by default.

Some Contracts may be Restricted, including strategic agreements, employment agreements, litigation-related agreements, major supplier contracts and commercially sensitive customer agreements.

---

# Access Control

| Role | Read | Create | Update | Approve | Archive |
|---|:---:|:---:|:---:|:---:|:---:|
| Legal | ✓ | ✓ | ✓ | ✓ | ✓ |
| Contract Owner | ✓ | ✓ | Limited | Limited | |
| Procurement | Limited | ✓ | Limited | Limited | |
| Sales | Limited | ✓ | Limited | Limited | |
| Finance | Limited | | Limited | ✓ | |
| Executive | ✓ | | | Strategic | |
| AI Agent | Governed Read | | | ✗ | ✗ |

---

# Attribute-Level Security

Sensitive fields include contract value, liability caps, pricing terms, legal risk comments, negotiation history and confidential clauses.

---

# Authentication and Authorisation

All access requires authenticated users and authorised roles.

---

# Audit Logging

Every significant Contract action must record user, timestamp, action, previous value, new value, source system and reason.

---

# Encryption

Contracts must be encrypted at rest and in transit.

---

# AI Security

AI must inherit user permissions, protect confidential information, respect legal privilege and provide explainable outputs. AI may not expose confidential clauses to unauthorised users.

---

# API and Integration Security

Contract APIs must use authentication, authorisation, encryption, input validation, rate limiting and audit logging.

---

# Security Monitoring

Monitor unusual downloads, access to restricted contracts, approval anomalies, privilege changes, AI access and integration failures.

---

# Security Summary

The Contract Security Model protects legal and commercial agreements through layered access controls, encryption, audit logging and AI governance.
