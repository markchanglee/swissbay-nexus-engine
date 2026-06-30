# 08 — Relationships

---

# Overview

The Customer Business Object does not exist in isolation.

It sits at the centre of the Swissbay Nexus platform and serves as the primary relationship hub for nearly every commercial activity performed by the organisation.

Rather than storing all information internally, the Customer object connects to specialised Business Objects through governed relationships.

This approach eliminates duplication, improves data quality and allows every Business Object to remain focused on its own responsibilities.

The Relationships defined in this document establish how information flows throughout Swissbay Nexus.

---

# Relationship Philosophy

Swissbay Nexus follows one fundamental principle.

> Every Business Object owns its own information.

Business Objects communicate by creating relationships.

They do not duplicate information.

This philosophy allows the platform to scale without introducing conflicting versions of the same data.

---

# Customer Relationship Model

```
                              Customer
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
     Contacts                 Opportunities             Meetings
        │                         │                         │
        ▼                         ▼                         ▼
     Quotes ----------------> Sales Orders ---------> Invoices
        │
        ▼
     Products
        │
        ▼
     Deliveries

        │
        ▼

     Complaints

        │
        ▼

     Customer Success

        │
        ▼

     AI Agents

        │
        ▼

 Executive Dashboards
```

The Customer object acts as the central node connecting operational, financial and strategic information.

---

# Relationship Types

Swissbay recognises four primary relationship types.

## Ownership

The Customer owns information directly related to its identity.

Examples include:

- Customer ID
- Legal Name
- Customer Status
- Customer Type
- Industry
- Account Owner

---

## Reference

The Customer references other Business Objects without owning their internal data.

Examples include:

- Products
- Quotes
- Sales Orders
- Invoices
- Contracts

---

## Dependency

Some Business Objects cannot exist without a Customer.

Examples include:

- Quote
- Sales Order
- Invoice

These objects are considered dependent relationships.

---

## Association

Some Business Objects may exist independently but become associated with a Customer.

Examples include:

- Meeting
- Task
- Project
- Complaint
- Document

---

# Customer Relationships

---

## Customer → Contact

Relationship Type

One-to-Many

Description

A Customer may have many Contacts.

Contacts include:

- Executive
- Procurement
- Finance
- Operations
- Receiving
- Technical

The Contact Business Object owns detailed contact information.

---

## Customer → Opportunity

Relationship Type

One-to-Many

Description

A Customer may have multiple Opportunities over time.

Each Opportunity belongs to one Customer.

---

## Customer → Quote

Relationship Type

One-to-Many

Description

A Customer may receive many Quotations.

Each Quote belongs to one Customer.

Quotes represent proposed commercial agreements.

---

## Customer → Sales Order

Relationship Type

One-to-Many

Description

A Customer may place many Sales Orders.

Sales Orders represent confirmed commercial commitments.

---

## Customer → Invoice

Relationship Type

One-to-Many

Description

Invoices are issued to Customers following delivery or completion of agreed work.

Invoices cannot exist without a Customer.

---

## Customer → Product

Relationship Type

Many-to-Many

Description

Customers purchase many Products.

Products may be purchased by many Customers.

This relationship forms the basis for:

- purchasing history
- recommendation engines
- AI suggestions
- sales analytics

---

## Customer → Contract

Relationship Type

One-to-Many

Description

Customers may operate under one or more Contracts.

Contracts define commercial obligations.

---

## Customer → Delivery Address

Relationship Type

One-to-Many

Description

Customers may operate multiple delivery locations.

Examples include:

- warehouses
- mines
- schools
- factories
- offices

---

## Customer → Meeting

Relationship Type

One-to-Many

Description

Meetings provide relationship history.

Meetings support:

- account reviews
- opportunity discussions
- complaint resolution
- strategic planning

---

## Customer → Task

Relationship Type

One-to-Many

Description

Tasks represent actions required to support the Customer relationship.

Examples include:

- follow-up calls
- quotations
- site visits
- collections
- executive reviews

---

## Customer → Complaint

Relationship Type

One-to-Many

Description

Complaints provide insight into customer satisfaction and operational performance.

Complaint history contributes to Customer Health.

---

## Customer → AI Agent

Relationship Type

Many-to-Many

Description

Multiple AI Agents may consume Customer information.

Examples include:

- Sales AI
- CEO AI
- Finance AI
- Procurement AI
- Customer Success AI

AI Agents never own Customer information.

They consume governed Customer data.

---

## Customer → Dashboard

Relationship Type

Many-to-Many

Description

Customer information appears in multiple dashboards.

Examples include:

- CEO Dashboard
- Sales Dashboard
- Finance Dashboard
- Procurement Dashboard
- Customer Success Dashboard

---

# Relationship Rules

The following rules govern Customer relationships.

## Rule 1

Every relationship must reference a valid Business Object.

---

## Rule 2

Relationships should use Business Object IDs rather than names wherever possible.

Example

```
CUSTOMER-000245

↓

QUOTE-001284
```

instead of

```
ABC Mining

↓

Quote 25
```

---

## Rule 3

Relationships must never duplicate information already owned by another Business Object.

---

## Rule 4

Deleting a relationship must never delete the related Business Object unless explicitly authorised.

---

## Rule 5

Historical relationships must remain available for reporting and auditing.

---

# Relationship Cardinality

| Relationship | Cardinality |
|--------------|-------------|
| Customer → Contact | One-to-Many |
| Customer → Opportunity | One-to-Many |
| Customer → Quote | One-to-Many |
| Customer → Sales Order | One-to-Many |
| Customer → Invoice | One-to-Many |
| Customer → Product | Many-to-Many |
| Customer → Meeting | One-to-Many |
| Customer → Task | One-to-Many |
| Customer → Complaint | One-to-Many |
| Customer → Contract | One-to-Many |
| Customer → AI Agent | Many-to-Many |
| Customer → Dashboard | Many-to-Many |

---

# Knowledge Graph Perspective

Within the Swissbay Knowledge Graph, the Customer object functions as one of the highest-degree nodes.

Example:

```
Customer
│
├── buys ─────────────► Product
├── receives ─────────► Quote
├── confirms ─────────► Sales Order
├── pays ─────────────► Invoice
├── signs ────────────► Contract
├── attends ──────────► Meeting
├── generates ─────────► Task
├── reports ──────────► Complaint
├── analysed by ──────► AI Agent
└── displayed on ─────► Dashboard
```

This graph enables Nexus to answer questions such as:

- Which customers have not received a quote in six months?
- Which products are most commonly purchased by mining customers?
- Which customers have unresolved complaints?
- Which AI Agents use customer payment terms?
- Which dashboards will be affected if Customer Status changes?

---

# Future Relationships

Future versions of the Customer object may include relationships to:

- Marketing Campaigns
- Support Tickets
- Service Requests
- Warehouse Deliveries
- Site Inspections
- Compliance Audits
- Sustainability Metrics
- ESG Reporting
- IoT Devices
- Digital Customer Twins

The relationship model has therefore been designed to expand without changing the core Customer definition.

---

# Relationships Summary

The Customer Business Object is the relationship hub of Swissbay Nexus.

Rather than storing every piece of customer-related information internally, it creates governed connections to specialised Business Objects.

This architecture enables Swissbay to build a scalable, modular and AI-ready operating platform where information is connected through relationships instead of duplicated across systems.

The Relationship Model defined here forms the foundation of the Swissbay Knowledge Graph and will support future automation, analytics, artificial intelligence and enterprise-scale decision making.