# 05 — Definitions

---

# Overview

This document establishes the official enterprise vocabulary for the Contract Business Object.

These definitions ensure that Legal, Sales, Procurement, Finance, Operations, Compliance, Executive Management, Artificial Intelligence and enterprise systems interpret contractual information consistently.

These definitions are authoritative throughout Swissbay Nexus.

---

# Core Definitions

## Contract

A legally binding agreement between two or more parties that establishes enforceable commercial, legal, financial and operational commitments.

Every Contract is uniquely represented by one Contract Business Object.

---

## Contract Identifier

The permanent globally unique identifier assigned to every Contract.

Example

```text
CON-000847
```

Contract Identifiers:

- never change
- are never reused
- uniquely identify a Contract

---

## Contract Number

The externally recognised business reference for a Contract.

Example

```text
MSA-2026-014
```

Unlike the Contract Identifier, the Contract Number may follow business-specific numbering conventions.

---

## Contract Type

The business classification describing the purpose of the agreement.

Examples include:

- Master Service Agreement
- Statement of Work
- Purchase Agreement
- Sales Agreement
- Supplier Agreement
- Offtake Agreement
- NDA
- Lease Agreement
- Partnership Agreement

---

## Contract Owner

The employee accountable for managing the Contract throughout its lifecycle.

The Contract Owner ensures contractual obligations are fulfilled and governance is maintained.

---

## Contract Party

A legal entity participating in the agreement.

Examples include:

- Customer
- Supplier
- Partner
- Government Entity
- Subsidiary

---

## Effective Date

The date on which contractual obligations become legally enforceable.

---

## Expiry Date

The planned date on which the Contract concludes unless renewed or terminated earlier.

---

## Renewal

The governed process by which an existing Contract is extended or replaced.

Renewals preserve commercial continuity while maintaining governance.

---

## Amendment

A formally approved modification to an existing Contract.

Every Amendment forms part of the Contract's permanent audit history.

---

## Obligation

A contractual commitment that must be fulfilled by one or more Contract Parties.

Examples include:

- Deliver products
- Provide services
- Make payment
- Maintain insurance
- Meet service levels

---

## Milestone

A significant contractual event used to measure progress or trigger obligations.

Examples include:

- Contract Signature
- Project Start
- Payment Due
- Delivery Acceptance
- Renewal Review

---

## Service Level Agreement (SLA)

A measurable commitment defining expected service performance between contracting parties.

---

## Compliance

The ongoing process of ensuring that contractual obligations, policies and regulatory requirements are satisfied.

---

## Artificial Intelligence

Artificial Intelligence refers to governed capabilities that analyse Contract information to generate recommendations, identify risks, monitor obligations and support enterprise decision-making.

AI supports human experts but never replaces legal authority.

---

# Approved Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| CLM | Contract Lifecycle Management |
| SLA | Service Level Agreement |
| NDA | Non-Disclosure Agreement |
| MSA | Master Service Agreement |
| SOW | Statement of Work |
| KPI | Key Performance Indicator |
| AI | Artificial Intelligence |
| API | Application Programming Interface |

---

# Terminology Rules

Throughout the Contract Business Object:

- Use **Contract Identifier** rather than Contract ID.
- Use **Contract Party** instead of Participant.
- Use **Contract Owner** for enterprise accountability.
- Use **Obligation** for enforceable commitments.
- Use **Amendment** for approved contractual changes.

Terminology remains consistent across documentation, APIs and AI models.

---

# AI Interpretation

Artificial Intelligence must interpret Contract terminology according to this document.

Where ambiguity exists, these definitions take precedence over external terminology or vendor-specific contract management systems.

---

# Definition Governance

Changes to Contract terminology require:

- Legal Review
- Enterprise Architecture Review
- Governance Approval
- Version Update

Terminology changes should be carefully managed because they affect enterprise integrations and AI reasoning.

---

# Definitions Summary

This document establishes the official enterprise vocabulary for the Contract Business Object.

By defining consistent terminology for legal agreements, commercial commitments, operational obligations and enterprise governance, Swissbay Nexus ensures that people, systems and Artificial Intelligence operate from a shared understanding of every Contract.