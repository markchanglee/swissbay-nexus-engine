# 08 — Relationships

---

# Overview

The Sales Order Business Object is the primary commercial transaction within the Swissbay Nexus platform.

It connects Customers, Products, Warehouses, Finance, Logistics, Contracts and Projects into a governed business transaction that represents the complete lifecycle of a customer purchase.

Rather than duplicating master data, the Sales Order maintains governed relationships through permanent Business Object identifiers.

Relationships describe business meaning rather than database joins.

---

# Purpose

The Relationship Model exists to:

- define commercial dependencies
- connect enterprise Business Objects
- eliminate duplicated information
- support AI reasoning
- improve impact analysis
- support automation
- generate the Swissbay Knowledge Graph

Relationships provide business context for every Sales Order.

---

# Relationship Principles

The Sales Order Business Object follows these principles:

- Sales Orders own transactional information.
- Master Business Objects own master information.
- Relationships reference Business Objects rather than duplicate them.
- Every relationship has business meaning.
- Every relationship is governed.
- Relationships remain technology independent.

---

# Relationship Map

```text
                    Opportunity
                         │
                         ▼
Customer ───── Places ─── Sales Order ───── Contains ─── Product
                             │                     │
                             │                     ▼
                             │                Warehouse
                             │
                             ▼
                         Contract
                             │
                             ▼
                          Invoice
                             │
                             ▼
                           Payment

                 Employee
                     │
                     ▼
            Processes Sales Order
```

The Sales Order Business Object acts as the commercial hub connecting enterprise master data with operational execution.

---

# Parent Relationships

The Sales Order references the following parent Business Objects:

| Business Object | Relationship |
|-----------------|--------------|
| Customer | Places Sales Order |
| Opportunity | Converts Into Sales Order |
| Contract | Governs Commercial Terms |

These Business Objects remain independently governed.

---

# Child Relationships

The Sales Order directly owns:

| Child Entity | Relationship |
|--------------|--------------|
| Order Lines | Contains |
| Shipment Events | Tracks |
| Status History | Records |
| Approval History | Maintains |
| Audit History | Maintains |

Child entities cannot exist independently of a Sales Order.

---

# Customer Relationship

Customers create Sales Orders.

Relationship

```text
Customer

1

↓

Many

↓

Sales Orders
```

Customer ownership remains within OBJ-001.

The Sales Order stores a transactional snapshot of customer information.

---

# Product Relationship

Products are purchased through Sales Orders.

Relationship

```text
Sales Order

↓

Contains

↓

Products
```

Each Product is referenced using its permanent Product Identifier.

The Sales Order stores transactional pricing and quantity.

The Product Business Object remains the Product Master.

---

# Warehouse Relationship

Warehouses fulfil Sales Orders.

Relationship

```text
Warehouse

↓

Allocates

↓

Sales Order
```

Warehouse ownership includes:

- inventory
- picking
- packing
- storage
- stock movements

The Sales Order tracks fulfilment status only.

---

# Contract Relationship

Contracts may govern commercial terms.

Relationship

```text
Contract

↓

Applies To

↓

Sales Order
```

Contracts may define:

- pricing
- payment terms
- discounts
- service levels

Contracts remain independent Business Objects.

---

# Opportunity Relationship

Sales Opportunities may convert into Sales Orders.

Relationship

```text
Opportunity

↓

Converted To

↓

Sales Order
```

This relationship supports pipeline reporting and conversion analysis.

---

# Employee Relationship

Employees interact with Sales Orders.

Examples include:

- Sales Representative
- Customer Service Agent
- Warehouse Operator
- Finance Officer

Relationship

```text
Employee

↓

Processes

↓

Sales Order
```

Employees remain governed by the Employee Business Object.

---

# Invoice Relationship

Invoices are generated from Sales Orders.

Relationship

```text
Sales Order

↓

Generates

↓

Invoice
```

Invoice ownership belongs to the Finance domain.

The Sales Order stores only invoice references.

---

# Payment Relationship

Payments settle Sales Orders.

Relationship

```text
Invoice

↓

Settled By

↓

Payment
```

Payment ownership belongs to Finance.

Sales Orders reference payment status but do not own financial transactions.

---

# Project Relationship

Projects may consume Sales Orders.

Relationship

```text
Project

↓

Requests

↓

Sales Order
```

This supports project-based procurement and customer delivery.

---

# Asset Relationship

Delivered Products may become Assets.

Relationship

```text
Sales Order

↓

Supplies

↓

Asset
```

Asset registration occurs after fulfilment.

The Asset Business Object owns asset lifecycle management.

---

# AI Relationships

Artificial Intelligence interacts with Sales Orders by:

- forecasting revenue
- predicting fulfilment delays
- analysing purchasing behaviour
- detecting pricing anomalies
- identifying fraud indicators
- recommending substitute Products
- estimating customer lifetime value

AI consumes Sales Order information but never owns it.

---

# Workflow Relationships

Sales Orders participate in:

- Opportunity Conversion
- Order Creation
- Order Approval
- Inventory Allocation
- Picking
- Packing
- Shipping
- Delivery
- Invoicing
- Returns
- Order Closure

Each workflow references the Sales Order Business Object through its permanent identifier.

---

# Dashboard Relationships

Sales Order information contributes to:

- Sales Dashboard
- Revenue Dashboard
- Fulfilment Dashboard
- Customer Dashboard
- Executive Dashboard
- AI Insights Dashboard

Dashboards consume Sales Order information but never modify it.

---

# KPI Relationships

Sales Orders contribute to:

- Revenue
- Gross Margin
- Order Cycle Time
- Fulfilment Rate
- Customer Satisfaction
- On-Time Delivery
- Return Rate
- Cancellation Rate

KPIs are calculated using governed Sales Order information.

---

# Security Relationships

Sales Order security follows the Swissbay Security Standard.

Permissions determine:

- who may create Sales Orders
- who may approve Sales Orders
- who may modify commercial values
- who may cancel Sales Orders
- who may access financial information

Security relationships are enforced through platform governance.

---

# Knowledge Graph Representation

Within the Swissbay Knowledge Graph, the Sales Order Business Object acts as the primary commercial transaction node.

Example

```text
Sales Order

├── placed by → Customer
├── contains → Product
├── fulfilled by → Warehouse
├── governed by → Contract
├── generated from → Opportunity
├── processed by → Employee
├── generates → Invoice
├── settled by → Payment
├── supplies → Asset
└── analysed by → AI
```

This semantic representation enables enterprise search, AI reasoning and dependency analysis.

---

# Relationship Ownership

| Relationship | Owner |
|--------------|-------|
| Customer | Sales |
| Product | Sales Operations |
| Warehouse | Operations |
| Contract | Legal |
| Opportunity | Sales |
| Employee | Human Resources |
| Invoice | Finance |
| Payment | Finance |
| Asset | Operations |

Ownership defines governance responsibility.

---

# Relationship Validation

Every Sales Order relationship should verify:

- referenced Business Object exists
- identifiers are valid
- relationship type is permitted
- lifecycle compatibility is maintained
- duplicate relationships do not exist

Relationship integrity is continuously monitored.

---

# Relationship Summary

The Sales Order Business Object is the transactional centre of the Swissbay Nexus commercial operating model.

By maintaining governed relationships with Customers, Products, Warehouses, Contracts, Opportunities, Employees, Invoices and Payments, the Sales Order creates a connected enterprise transaction model that supports fulfilment, reporting, automation, governance and Artificial Intelligence.

Relationships transform Sales Orders from isolated ERP records into intelligent enterprise transactions.
