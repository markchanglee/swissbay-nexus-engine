# 08 — Relationships

---

# Overview

The Product Business Object exists at the centre of the Swissbay Nexus business ecosystem.

Every Product participates in a governed network of business relationships that connect procurement, warehousing, projects, finance, sales and customer operations.

Rather than embedding duplicate information, the Product Business Object maintains governed relationships with other Business Objects through permanent identifiers.

Relationships represent business meaning rather than database joins.

---

# Purpose

The Relationship Model exists to:

- define enterprise dependencies
- eliminate duplicated information
- support semantic search
- enable AI reasoning
- improve impact analysis
- support automation
- generate the Swissbay Knowledge Graph

Relationships provide context to business information.

---

# Relationship Principles

The Product Business Object follows these principles:

- Products own product information.
- Related Business Objects reference Products.
- Product information is never duplicated.
- Every relationship has business meaning.
- Every relationship is governed.
- Relationships remain technology independent.

---

# Relationship Map

```text
                     Customer
                         ▲
                         │
                  Purchased Through
                         │
                   Sales Order
                         ▲
                         │
Supplier ─── Supplies ── Product ─── Stored In ── Warehouse
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
      Project         Contract       Asset
          │
          ▼
     Opportunity
```

The Product Business Object acts as the commercial bridge between operational and commercial processes.

---

# Parent Relationships

The Product Business Object has no parent Business Objects.

It is classified as a Master Business Object.

---

# Child Relationships

The Product Business Object directly supports:

| Business Object | Relationship |
|-----------------|--------------|
| Warehouse | Stores Product |
| Sales Order | Contains Product |
| Asset | Created From Product |
| Project | Consumes Product |
| Contract | Defines Commercial Terms |
| Opportunity | References Proposed Products |

---

# Supplier Relationship

Products are supplied by one or more Suppliers.

Relationship

```text
Supplier

1

↓

Many

↓

Products
```

Suppliers own supplier information.

Products reference Suppliers through Supplier Identifiers.

---

# Customer Relationship

Customers purchase Products through Sales Orders.

Relationship

```text
Customer

↓

Sales Order

↓

Product
```

The Product Business Object does not own Customer information.

---

# Warehouse Relationship

Warehouses store Products.

Relationship

```text
Warehouse

↓

Stores

↓

Product
```

Warehouse ownership includes:

- stock quantities
- locations
- movements
- replenishment

The Product Business Object owns only the product definition.

---

# Sales Order Relationship

Sales Orders reference Products.

Relationship

```text
Sales Order

↓

Contains

↓

Product
```

Sales Orders determine:

- quantity
- selling price
- discounts
- fulfilment

The Product Business Object owns none of these transactional values.

---

# Project Relationship

Projects consume Products.

Relationship

```text
Project

↓

Uses

↓

Product
```

Projects reference Products for:

- planning
- budgeting
- procurement
- execution

---

# Asset Relationship

Assets may originate from Products.

Relationship

```text
Product

↓

Becomes

↓

Asset
```

Example

```
Laptop Product

↓

Issued

↓

Employee Laptop Asset
```

Asset ownership belongs to the Asset Business Object.

---

# Contract Relationship

Contracts define commercial agreements relating to Products.

Relationship

```text
Contract

↓

Defines

↓

Product
```

Contracts may specify:

- pricing
- warranty
- support
- delivery terms

The Product Business Object references Contracts but does not own them.

---

# Opportunity Relationship

Sales Opportunities may reference Products before a sale exists.

Relationship

```text
Opportunity

↓

Proposes

↓

Product
```

This supports forecasting and pipeline analysis.

---

# AI Relationships

Artificial Intelligence interacts with Products by:

- classifying Products
- recommending alternatives
- forecasting demand
- identifying duplicate Products
- predicting inventory shortages
- analysing profitability
- generating summaries

AI consumes Product information but never owns it.

---

# Workflow Relationships

Products participate in:

- Product Creation
- Product Approval
- Procurement
- Inventory Management
- Sales
- Manufacturing
- Asset Registration
- Product Retirement

Each workflow references the Product Business Object through its permanent Product Identifier.

---

# Dashboard Relationships

Product information contributes to:

- Product Dashboard
- Inventory Dashboard
- Sales Dashboard
- Executive Dashboard
- Procurement Dashboard
- Warehouse Dashboard
- AI Insights Dashboard

Dashboards consume Product information but never modify it.

---

# KPI Relationships

Products contribute to:

- Product Profitability
- Inventory Turnover
- Product Availability
- Sales Volume
- Gross Margin
- Product Lifecycle Duration
- Stock Accuracy

KPIs are calculated using governed Product information.

---

# Security Relationships

Product security follows the Swissbay Security Standard.

Permissions determine:

- who may create Products
- who may modify Products
- who may approve Products
- who may retire Products

Security relationships are enforced through platform governance.

---

# Knowledge Graph Representation

Within the Swissbay Knowledge Graph, the Product Business Object acts as a central operational node.

Example

```text
Product

├── supplied by → Supplier
├── stored in → Warehouse
├── sold through → Sales Order
├── purchased by → Customer
├── consumed by → Project
├── governed by → Contract
├── converted into → Asset
└── analysed by → AI
```

This representation enables enterprise navigation, semantic search and intelligent dependency analysis.

---

# Relationship Ownership

| Relationship | Owner |
|--------------|-------|
| Supplier | Procurement |
| Warehouse | Operations |
| Sales Order | Sales |
| Customer | Sales |
| Project | PMO |
| Asset | Operations |
| Contract | Legal |
| Opportunity | Sales |

Ownership determines governance responsibility.

---

# Relationship Validation

Every Product relationship should verify that:

- referenced Business Object exists
- identifiers are valid
- relationship type is permitted
- duplicate relationships do not exist
- lifecycle compatibility is maintained

Relationship integrity is continuously monitored.

---

# Relationship Summary

The Product Business Object is the central commercial hub within Swissbay Nexus.

By maintaining governed relationships with Suppliers, Warehouses, Sales Orders, Customers, Projects, Assets, Contracts and Opportunities, the Product Business Object creates a connected enterprise model that supports governance, automation, reporting and Artificial Intelligence.

Relationships transform Products from isolated catalogue entries into intelligent enterprise knowledge.