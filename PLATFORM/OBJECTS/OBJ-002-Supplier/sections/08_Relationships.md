# 08 — Relationships

---

# Overview

The Supplier Business Object does not operate in isolation.

It participates in a network of governed business relationships that connect procurement, finance, operations, projects, contracts and sales throughout the Swissbay Nexus platform.

Relationships define how suppliers interact with other Business Objects while maintaining clear ownership and avoiding duplication of business information.

Every relationship documented in this section is considered a governed enterprise relationship.

---

# Purpose

The Relationship Model exists to:

- define business dependencies
- eliminate duplicated information
- support enterprise navigation
- enable AI reasoning
- improve impact analysis
- simplify integrations
- support Knowledge Graph generation

Relationships describe business meaning rather than technical implementation.

---

# Relationship Principles

The Supplier Business Object follows these principles:

- Suppliers own supplier information.
- Related Business Objects reference the Supplier.
- Business information is never duplicated.
- Every relationship has a defined purpose.
- Every relationship is governed.

---

# Relationship Map

```text
Supplier
│
├── Products
├── Contracts
├── Purchase Requests
├── Purchase Orders
├── Projects
├── Assets
├── Warehouses
├── Sales Orders
├── Invoices
├── Payments
└── AI Agents
```

The Supplier Business Object remains the authoritative source for supplier information.

---

# Parent Relationships

The Supplier Business Object has no parent Business Objects.

It is classified as a Master Business Object.

---

# Child Relationships

Supplier directly supports the following Business Objects.

| Business Object | Relationship |
|-----------------|--------------|
| Product | Supplies Products |
| Contract | Supplier Agreement |
| Purchase Request | Potential Supplier |
| Purchase Order | Fulfils Order |
| Project | Supplies Project |
| Asset | Supplies Asset |
| Warehouse | Delivers Inventory |
| Sales Order | Indirect Supply Chain Support |

---

# Product Relationship

Supplier provides one or more Products.

Relationship Type

```
Supplier

1

↓

Many

↓

Products
```

Products reference Suppliers.

Suppliers do not contain Product information.

---

# Contract Relationship

Every Supplier may have zero or more Contracts.

Relationship Type

```
Supplier

1

↓

Many

↓

Contracts
```

Contract ownership belongs to the Contract Business Object.

---

# Purchase Request Relationship

Purchase Requests may identify one or more preferred Suppliers.

Relationship

```
Purchase Request

↓

Supplier Recommendation

↓

Supplier
```

Supplier evaluation occurs before procurement.

---

# Purchase Order Relationship

Purchase Orders reference the approved Supplier responsible for fulfilment.

Relationship

```
Supplier

↓

Fulfils

↓

Purchase Order
```

Purchase Orders remain independent Business Objects.

---

# Project Relationship

Projects may consume products or services from multiple Suppliers.

Relationship

```
Project

↓

Uses

↓

Supplier
```

Projects do not own Supplier information.

---

# Asset Relationship

Assets may originate from Suppliers.

Relationship

```
Supplier

↓

Supplied

↓

Asset
```

Asset ownership belongs to the Asset Business Object.

---

# Warehouse Relationship

Warehouses receive inventory from Suppliers.

Relationship

```
Supplier

↓

Delivers

↓

Warehouse
```

Warehouse operations remain governed independently.

---

# Invoice Relationship

Supplier Invoices reference the Supplier.

Relationship

```
Supplier

↓

Issues

↓

Invoice
```

Invoices belong to Finance.

---

# Payment Relationship

Payments reference Suppliers.

Relationship

```
Supplier

↓

Receives

↓

Payment
```

Payment processing belongs to Finance.

---

# Customer Relationship

There is no direct ownership relationship between Suppliers and Customers.

Any connection occurs through Products, Projects or Sales Orders.

Example

```
Supplier

↓

Product

↓

Sales Order

↓

Customer
```

This separation prevents unnecessary coupling between procurement and customer management.

---

# AI Relationships

Artificial Intelligence interacts with the Supplier Business Object to:

- analyse supplier performance
- recommend preferred suppliers
- predict procurement risks
- identify duplicate suppliers
- monitor supplier compliance
- generate executive summaries

AI consumes Supplier information but never owns it.

---

# Workflow Relationships

The Supplier Business Object participates in the following workflows:

- Supplier Onboarding
- Supplier Qualification
- Supplier Approval
- Purchase Request
- Purchase Order
- Contract Management
- Supplier Review
- Supplier Offboarding

Each workflow references the Supplier through its unique identifier.

---

# Dashboard Relationships

Supplier information contributes to:

- Procurement Dashboard
- Executive Dashboard
- Supplier Performance Dashboard
- Spend Analysis Dashboard
- Risk Dashboard

Dashboards consume Supplier information but never modify it.

---

# KPI Relationships

Supplier contributes to KPIs including:

- Supplier Performance Score
- Preferred Supplier Percentage
- Supplier Risk Rating
- On-Time Delivery
- Procurement Cycle Time
- Supplier Compliance Rate

KPIs are calculated using governed supplier data.

---

# Security Relationships

Supplier security inherits the Swissbay Security Standard.

Permissions determine:

- who may view suppliers
- who may update suppliers
- who may approve suppliers
- who may archive suppliers

Security relationships are enforced by platform governance.

---

# Knowledge Graph Representation

Within the Swissbay Knowledge Graph, the Supplier Business Object is represented as a central procurement node.

Example

```text
Supplier

├── supplies → Product
├── signs → Contract
├── fulfils → Purchase Order
├── supports → Project
├── delivers → Warehouse
├── invoices → Finance
└── evaluated by → Procurement
```

This representation enables semantic search, dependency analysis and AI reasoning.

---

# Relationship Ownership

| Relationship | Owner |
|--------------|-------|
| Product | Procurement |
| Contract | Legal |
| Purchase Order | Procurement |
| Project | PMO |
| Warehouse | Operations |
| Invoice | Finance |
| Payment | Finance |

Ownership determines governance responsibility.

---

# Relationship Validation

Every relationship should verify that:

- referenced Business Object exists
- identifiers are valid
- ownership is defined
- duplicate relationships do not exist
- lifecycle compatibility is maintained

Relationship integrity is continuously monitored.

---

# Relationship Summary

The Supplier Business Object serves as the procurement hub within the Swissbay Nexus platform.

By defining clear, governed relationships with Products, Contracts, Purchase Orders, Projects, Assets, Warehouses and Finance, the Supplier Business Object creates a connected enterprise model that supports governance, analytics, automation and Artificial Intelligence.

Relationships transform isolated business records into an intelligent business network.