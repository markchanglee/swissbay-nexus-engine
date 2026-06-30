# Swissbay Nexus Business Object Index

---

# Purpose

The Business Object Index provides the authoritative catalogue of every Business Object defined within the Swissbay Nexus platform.

It enables architects, developers, business users, AI Agents and governance teams to quickly discover Business Objects, understand ownership and navigate the enterprise business model.

The index acts as the primary entry point into the Business Object repository.

---

# Business Object Catalogue

| Object ID | Business Object | Domain | Business Owner | Status | Version |
|-----------|-----------------|--------|----------------|--------|---------|
| OBJ-001 | Customer | Sales | Sales | Draft | 1.0.0 |
| OBJ-002 | Supplier | Procurement | Procurement | Draft | 1.0.0 |
| OBJ-003 | Product | Operations | Operations | Draft | 1.0.0 |
| OBJ-004 | Employee | Human Resources | Human Resources | Planned | - |
| OBJ-005 | Contract | Legal | Legal | Planned | - |
| OBJ-006 | Project | Project Management | PMO | Planned | - |
| OBJ-007 | Asset | Asset Management | Operations | Planned | - |
| OBJ-008 | Warehouse | Logistics | Operations | Planned | - |
| OBJ-009 | Opportunity | Sales | Sales | Planned | - |
| OBJ-010 | Sales Order | Sales Operations | Sales | Planned | - |

---

# Business Object Relationship Overview

```text
Customer
    ▲
    │
Sales Order
    ▲
    │
Product
 ▲      ▲
 │      │
Supplier Asset
    │
Warehouse

Employee

Project

Contract

Opportunity
```

The relationships above represent the primary interactions between the initial core Business Objects.

---

# Business Domains

| Domain | Business Objects |
|---------|------------------|
| Sales | Customer, Opportunity, Sales Order |
| Procurement | Supplier |
| Operations | Product, Asset, Warehouse |
| Human Resources | Employee |
| Legal | Contract |
| Project Management | Project |

Business Objects are grouped by their primary business domain while remaining reusable across the enterprise.

---

# Object Lifecycle

Every Business Object follows the same lifecycle.

```text
Planned

↓

Draft

↓

Review

↓

Approved

↓

Released

↓

Operational

↓

Revised

↓

Retired

↓

Archived
```

Lifecycle governance is defined in OBJ-000.

---

# Foundation Standards

Every Business Object inherits the following standards:

- NX-000 Constitution
- OBJ-000 Business Object Standard
- DATA-000 Data Standard
- WF-000 Workflow Standard
- KPI-000 KPI Standard
- DASH-000 Dashboard Standard
- VALID-000 Validation Standard
- SEC-000 Security Standard
- AUTO-000 Automation Standard
- AI-000 AI Operating Standard

---

# Governance

Every Business Object within this index is governed through the Swissbay Nexus Governance Framework.

Changes to object status, ownership or structure require governance approval and must be reflected within this index.

---

# Version

| Version | Date | Summary |
|---------|------|---------|
| 1.0.0 | 2026-06-30 | Initial Business Object Index |