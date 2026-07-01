# 08 — Relationships

---

# Overview

The Asset Business Object is the enterprise resource layer within Swissbay Nexus.

Assets enable Projects, support Operations, consume Procurement, require Maintenance and generate financial value.

This document defines the governed relationships between the Asset Business Object and all related Business Objects.

Every relationship is maintained through permanent Business Object identifiers.

---

# Purpose

The Relationship Model exists to:

- establish ownership
- coordinate enterprise operations
- improve traceability
- support governance
- enable Artificial Intelligence
- simplify integrations

Assets become connected enterprise resources rather than isolated records.

---

# Relationship Principles

Asset relationships are:

- governed
- auditable
- reusable
- lifecycle aware
- technology independent
- business-focused

Relationships describe business meaning rather than database implementation.

---

# Relationship Categories

Assets participate in relationships involving:

- Employees
- Suppliers
- Contracts
- Projects
- Warehouses
- Products
- Sales Orders
- Maintenance
- Artificial Intelligence

---

# Employee Relationships

Employees may interact with Assets as:

- Business Owners
- Custodians
- Operators
- Engineers
- Maintenance Technicians

Relationship

```text
Employee

↓

Assigned To

↓

Asset
```

Purpose

Defines accountability and operational responsibility.

---

# Supplier Relationships

Suppliers provide or maintain Assets.

Relationship

```text
Supplier

↓

Supplies

↓

Asset
```

Purpose

Maintains procurement and warranty traceability.

---

# Contract Relationships

Assets may be governed by:

- Purchase Contracts
- Lease Agreements
- Maintenance Contracts
- Service Agreements

Relationship

```text
Contract

↓

Governs

↓

Asset
```

Purpose

Links commercial obligations to operational resources.

---

# Project Relationships

Projects may:

- acquire Assets
- construct Assets
- upgrade Assets
- deploy Assets
- retire Assets

Relationship

```text
Project

↓

Creates / Uses

↓

Asset
```

Purpose

Maintains traceability between investment and operational capability.

---

# Warehouse Relationships

Warehouses store Assets awaiting deployment or transfer.

Relationship

```text
Warehouse

↓

Stores

↓

Asset
```

Purpose

Tracks asset location and logistics.

---

# Product Relationships

Assets may manufacture, transport or support Products.

Relationship

```text
Asset

↓

Supports

↓

Product
```

Purpose

Links operational capability to business outputs.

---

# Sales Order Relationships

Projects and Assets may fulfil Sales Orders.

Relationship

```text
Sales Order

↓

Fulfilled Using

↓

Asset
```

Purpose

Connects operational resources to commercial execution.

---

# Maintenance Relationships

Assets participate in maintenance activities.

Relationship

```text
Asset

↓

Maintained By

↓

Maintenance Activity
```

Maintenance history remains permanently associated with the Asset.

---

# Knowledge Graph Relationships

Within the Swissbay Knowledge Graph, Assets become highly connected enterprise nodes.

Example

```text
Asset

├── owned by → Employee
├── governed by → Contract
├── supplied by → Supplier
├── created by → Project
├── stored in → Warehouse
├── supports → Product
├── fulfils → Sales Order
└── analysed by → AI
```

These relationships enable semantic search, dependency analysis and explainable AI.

---

# Cardinality

| Relationship | Cardinality |
|--------------|-------------|
| Employee → Asset | One : Many |
| Supplier → Asset | One : Many |
| Contract → Asset | One : Many |
| Project → Asset | Many : Many |
| Warehouse → Asset | One : Many |
| Product → Asset | Many : Many |
| Sales Order → Asset | Many : Many |

---

# Relationship Governance

Relationship changes require:

- validation
- workflow execution
- audit logging
- governance approval where applicable

Critical relationships should never be modified outside approved workflows.

---

# AI Interpretation

Artificial Intelligence interprets Asset relationships to:

- analyse utilisation
- predict maintenance
- identify dependencies
- optimise deployment
- forecast replacement

AI must never infer unauthorised relationships.

---

# Relationship Summary

The Asset Relationship Model establishes how Assets connect enterprise operations, finance, maintenance, projects and commercial activities within Swissbay Nexus.

By governing relationships between Employees, Suppliers, Contracts, Projects, Warehouses, Products and Sales Orders, Assets become trusted enterprise resources that support operational excellence, lifecycle governance and intelligent decision-making.