# 07 — Data Model

---

# Overview

The Sales Order Data Model defines the canonical representation of every commercial sales transaction managed within Swissbay Nexus.

Unlike master Business Objects, which describe long-lived business entities, the Sales Order Data Model represents a governed transactional snapshot.

It captures the commercial agreement exactly as it existed at the time the order was created while maintaining governed references to enterprise master data.

The Sales Order Data Model serves as the authoritative source for operational processing, reporting, Artificial Intelligence, automation and enterprise integrations.

---

# Purpose

The Sales Order Data Model exists to:

- establish one enterprise transaction model
- preserve commercial history
- support fulfilment
- enable financial reporting
- improve customer service
- support automation
- enable Artificial Intelligence

Every Sales Order should conform to this canonical business model.

---

# Business Entity

Business Object

```
Sales Order
```

Primary Identifier

```
SO-2026-000001
```

Identifiers are:

- globally unique
- immutable
- never reused

---

# Entity Structure

```
Sales Order

├── Identity
├── Customer Snapshot
├── Order Lines
├── Commercial
├── Fulfilment
├── Delivery
├── Invoice References
├── Relationships
├── Governance
├── Audit
└── Metadata
```

---

# Identity

| Field | Type | Required |
|---------|------|----------|
| Sales Order Identifier | Identifier | Yes |
| Sales Order Number | Text | Yes |
| Order Date | DateTime | Yes |
| Order Type | Enumeration | Yes |
| Sales Channel | Enumeration | Yes |
| Order Source | Enumeration | No |
| Order Status | Enumeration | Yes |
| Lifecycle Stage | Enumeration | Yes |

Identity uniquely defines the Sales Order transaction.

---

# Customer Snapshot

The Sales Order stores a snapshot of customer information at the time of ordering.

| Field | Type | Required |
|---------|------|----------|
| Customer Identifier | Reference | Yes |
| Customer Name | Text | Yes |
| Billing Address | Address | Yes |
| Delivery Address | Address | Yes |
| Customer Contact | Text | No |
| Customer PO Number | Text | No |

Customer master information remains owned by the Customer Business Object.

Historical Sales Orders are never modified when Customer details change.

---

# Order Lines

A Sales Order contains one or more Order Lines.

Each Order Line contains:

| Field | Type | Required |
|---------|------|----------|
| Line Number | Integer | Yes |
| Product Identifier | Reference | Yes |
| Product Description | Text | Yes |
| Quantity Ordered | Decimal | Yes |
| Unit Price | Currency | Yes |
| Discount | Currency | No |
| Tax | Currency | Yes |
| Extended Amount | Currency | Yes |

Order Lines preserve commercial information exactly as sold.

---

# Commercial Information

| Field | Type | Required |
|---------|------|----------|
| Currency | Currency Code | Yes |
| Payment Terms | Enumeration | Yes |
| Freight Charges | Currency | No |
| Tax Total | Currency | Yes |
| Discount Total | Currency | No |
| Order Subtotal | Currency | Yes |
| Grand Total | Currency | Yes |

Commercial values remain immutable after invoicing unless corrected through governed processes.

---

# Fulfilment

| Field | Type | Required |
|---------|------|----------|
| Warehouse | Reference | Yes |
| Allocation Status | Enumeration | Yes |
| Picking Status | Enumeration | Yes |
| Packing Status | Enumeration | Yes |
| Shipment Status | Enumeration | Yes |
| Delivery Status | Enumeration | Yes |

Warehouse execution belongs to the Warehouse Business Object.

The Sales Order records transactional fulfilment status.

---

# Delivery Information

| Field | Type | Required |
|---------|------|----------|
| Delivery Method | Enumeration | Yes |
| Carrier | Text | No |
| Tracking Number | Text | No |
| Requested Delivery Date | Date | No |
| Actual Delivery Date | Date | No |

Delivery history remains permanently associated with the Sales Order.

---

# Invoice References

The Sales Order references Finance records.

| Field | Type |
|---------|------|
| Invoice Identifier | Reference |
| Invoice Number | Text |
| Invoice Date | Date |
| Invoice Status | Enumeration |

Invoice ownership belongs to Finance.

---

# Relationships

The Sales Order maintains governed references to:

- Customer
- Product
- Warehouse
- Employee
- Contract
- Opportunity
- Project
- Asset

Relationships use permanent Business Object identifiers.

---

# Governance Fields

| Field | Type |
|---------|------|
| Business Owner | User |
| Approval Status | Enumeration |
| Approved By | User |
| Approval Date | DateTime |
| Workflow Identifier | Reference |

Governance supports accountability.

---

# Audit Fields

| Field | Type |
|---------|------|
| Created Date | DateTime |
| Modified Date | DateTime |
| Modified By | User |
| Version | Number |
| Change Reason | Text |

Audit information is mandatory.

---

# Metadata

Every Sales Order contains metadata including:

- Object Identifier
- Version
- Tags
- Search Keywords
- AI Summary
- Related Documents
- Related Business Objects

Metadata improves discoverability and reporting.

---

# Relationship Model

```
Customer

↓

Sales Order

↓

Order Lines

↓

Products

↓

Warehouse

↓

Invoice
```

The Sales Order is the central transaction connecting master data to operational execution.

---

# Data Ownership

| Area | Owner |
|--------|-------|
| Identity | Sales Operations |
| Customer Snapshot | Sales Operations |
| Order Lines | Sales |
| Commercial | Finance |
| Fulfilment Status | Warehouse |
| Delivery | Logistics |
| Governance | Sales Operations |
| Audit | Platform |

Ownership defines accountability while preserving clear business boundaries.

---

# Validation

The Sales Order Data Model validates:

- Customer Reference
- Product References
- Order Lines
- Pricing
- Currency
- Payment Terms
- Lifecycle Stage
- Commercial Totals

Detailed validation rules are governed separately.

---

# AI Usage

Artificial Intelligence uses the Sales Order Data Model to:

- forecast revenue
- predict delivery delays
- recommend substitute Products
- detect pricing anomalies
- estimate fulfilment times
- analyse purchasing behaviour

AI consumes governed transactional information only.

---

# Integration

The Sales Order Data Model supports:

- ERP Systems
- CRM Platforms
- Warehouse Management Systems
- Finance Systems
- Shipping Systems
- Microsoft Fabric
- Databricks
- REST APIs
- Knowledge Graph

Technology implementations inherit this canonical business model.

---

# Future Extensions

Future versions may introduce:

- Subscription Orders
- Marketplace Orders
- AI Fulfilment Scores
- Sustainability Metrics
- Carbon Shipping Indicators
- Dynamic Pricing History
- Customer Experience Scores

Extensions should preserve backwards compatibility wherever practical.

---

# Data Model Summary

The Sales Order Data Model establishes the canonical representation of every commercial transaction within Swissbay Nexus.

By preserving transactional snapshots while maintaining governed references to enterprise master data, the model provides a reusable foundation for order management, fulfilment, reporting, Artificial Intelligence, automation and enterprise integrations.

The Sales Order therefore becomes the trusted transactional record supporting the complete Quote-to-Cash process.