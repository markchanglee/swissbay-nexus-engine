# 08 — Relationships

---

# Overview

The Project Business Object is the enterprise execution hub within Swissbay Nexus.

Unlike master Business Objects that primarily store information, Projects coordinate work across Customers, Contracts, Employees, Assets, Suppliers, Products and Sales Orders.

This document defines the governed relationships between the Project Business Object and other Business Objects.

All relationships are maintained using permanent Business Object identifiers.

---

# Purpose

The Relationship Model exists to:

- establish accountability
- coordinate enterprise work
- support governance
- enable reporting
- improve traceability
- enable Artificial Intelligence
- simplify integrations

Projects orchestrate work across multiple business domains.

---

# Relationship Principles

Project relationships are:

- governed
- auditable
- reusable
- technology independent
- business-focused
- lifecycle aware

Relationships describe business meaning rather than technical implementation.

---

# Relationship Categories

Project relationships include:

- Customer Relationships
- Contract Relationships
- Employee Relationships
- Supplier Relationships
- Product Relationships
- Asset Relationships
- Opportunity Relationships
- Sales Relationships
- Governance Relationships
- AI Relationships

---

# Customer Relationships

Projects may be initiated on behalf of Customers.

Relationship

```text
Customer

↓

Owns Requirement

↓

Project
```

Purpose

Links delivery activities to customer commitments.

---

# Contract Relationships

Every commercial project should reference its governing Contract.

Relationship

```text
Contract

↓

Authorises

↓

Project
```

Purpose

Ensures legal and commercial governance.

---

# Employee Relationships

Projects reference Employees for:

- Project Sponsor
- Business Owner
- Project Manager
- Team Members
- Subject Matter Experts

Relationship

```text
Employee

↓

Assigned To

↓

Project
```

---

# Supplier Relationships

Suppliers may contribute goods or services.

Relationship

```text
Supplier

↓

Supports

↓

Project
```

---

# Product Relationships

Projects may create, enhance or deploy Products.

Relationship

```text
Project

↓

Delivers

↓

Product
```

---

# Asset Relationships

Projects may create, acquire or modify Assets.

Relationship

```text
Project

↓

Creates / Updates

↓

Asset
```

---

# Opportunity Relationships

Projects frequently originate from Opportunities.

Relationship

```text
Opportunity

↓

Converted To

↓

Project
```

Purpose

Maintains traceability from pipeline to delivery.

---

# Sales Order Relationships

Projects may fulfil Sales Orders.

Relationship

```text
Sales Order

↓

Executed By

↓

Project
```

---

# Programme Relationships

Projects may belong to Programmes.

```text
Programme

↓

Contains

↓

Project
```

Projects remain independently governed.

---

# Portfolio Relationships

Projects may contribute to strategic portfolios.

```text
Portfolio

↓

Contains

↓

Project
```

Portfolio management remains outside the individual Project Business Object.

---

# Workflow Relationships

Projects participate in enterprise workflows.

Examples include:

- Project Approval
- Budget Approval
- Change Control
- Stage Gate Review
- Project Closure

---

# Knowledge Graph Relationships

Within the Swissbay Knowledge Graph, Projects become highly connected nodes.

Example

```text
Project

├── owned by → Employee
├── governed by → Contract
├── serves → Customer
├── fulfils → Sales Order
├── creates → Asset
├── delivers → Product
├── supported by → Supplier
├── originated from → Opportunity
└── analysed by → AI
```

These relationships enable semantic search, impact analysis and explainable AI.

---

# Cardinality

| Relationship | Cardinality |
|--------------|-------------|
| Customer → Project | One : Many |
| Contract → Project | One : Many |
| Employee → Project | Many : Many |
| Supplier → Project | Many : Many |
| Product → Project | Many : Many |
| Asset → Project | Many : Many |
| Opportunity → Project | One : Many |
| Sales Order → Project | One : Many |

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

Artificial Intelligence interprets Project relationships to:

- understand project context
- identify dependencies
- analyse delivery risk
- recommend resources
- forecast outcomes

AI must never infer unauthorised relationships.

---

# Relationship Summary

The Project Relationship Model establishes how Projects connect strategic planning, operational delivery and enterprise governance across Swissbay Nexus.

By governing relationships between Customers, Contracts, Employees, Assets, Products, Suppliers, Opportunities and Sales Orders, Projects become the execution layer that transforms strategy into measurable business outcomes.