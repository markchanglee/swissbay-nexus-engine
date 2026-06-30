# 07 — Data Model

---

# Overview

The Customer Data Model defines the official structure of customer information within Swissbay Nexus.

It specifies the information required to uniquely identify, manage, analyse and grow customer relationships.

The objective of the Data Model is to ensure that every application, workflow, integration and AI Agent uses a consistent representation of a Customer.

This model is technology-independent.

It defines the business structure first.

Individual databases, APIs and software platforms should implement this model rather than redefine it.

---

# Data Model Principles

The Customer Data Model follows the following principles.

## Principle 1 — One Customer, One Record

Every Customer has one authoritative business record.

Duplicate customer records are prohibited.

---

## Principle 2 — Unique Identification

Every Customer receives a unique Customer Identifier that never changes.

Customer names may change.

Customer IDs never do.

---

## Principle 3 — Business Before Technology

The data model represents the business relationship.

It is not designed around any CRM, ERP or database.

---

## Principle 4 — Structured Information

Information should be stored in structured fields wherever possible.

Avoid storing important business information inside free-text notes.

---

## Principle 5 — Relationships Over Duplication

Customer information should reference other Business Objects instead of copying them.

---

# Customer Entity

The Customer Business Object consists of several logical groups.

---

# 1. Identification

These fields uniquely identify the Customer.

| Field | Required | Description |
|---------|----------|-------------|
| Customer ID | Yes | Permanent unique identifier |
| Legal Name | Yes | Registered company name |
| Trading Name | No | Operating name |
| Company Registration Number | No | Official registration number |
| VAT Number | No | Tax registration |
| Customer Type | Yes | Business classification |
| Industry | Yes | Primary industry |
| Status | Yes | Current lifecycle stage |

---

# 2. Account Ownership

Defines who owns the relationship.

| Field | Required |
|---------|----------|
| Account Owner | Yes |
| Sales Representative | Yes |
| Customer Success Manager | No |
| Business Unit | Yes |
| Territory | Yes |

---

# 3. Contact Information

A Customer may have multiple contacts.

Primary Contact

Finance Contact

Procurement Contact

Operations Contact

Executive Contact

Each Contact should eventually become its own Business Object.

The Customer stores relationships only.

---

# 4. Commercial Information

Commercial information defines how Swissbay trades with the Customer.

Fields include:

- Payment Terms
- Credit Status
- Credit Limit
- Preferred Currency
- Pricing Tier
- Customer Segment
- Strategic Account Indicator
- Preferred Supplier Agreements

---

# 5. Financial Information

Finance owns these attributes.

Examples include:

- Outstanding Balance
- Average Days to Pay
- Total Revenue
- Annual Spend
- Lifetime Revenue
- Gross Margin
- Credit Risk Rating

---

# 6. Operational Information

Operations requires:

- Billing Address
- Delivery Address
- Delivery Instructions
- Delivery Constraints
- Receiving Hours
- Site Access Requirements

---

# 7. Relationship Information

The Customer object references:

- Opportunities
- Quotes
- Orders
- Invoices
- Meetings
- Complaints
- Tasks
- Contracts
- Projects
- Products Purchased

These are relationships, not embedded data.

---

# 8. Customer Intelligence

Swissbay records strategic information.

Examples include:

- Preferred Product Categories
- Buying Behaviour
- Decision Process
- Purchasing Frequency
- Seasonal Demand
- Expansion Opportunities
- Customer Health Score
- Strategic Importance

---

# 9. Artificial Intelligence Context

Approved AI Agents may access:

- Customer Summary
- Recent Activity
- Open Opportunities
- Outstanding Risks
- Account Health
- Product Recommendations
- Meeting History
- Preferred Communication Style

AI Context must comply with AI-000.

---

# Customer Identifier Standard

Customer IDs follow a consistent format.

Example

```text
CUSTOMER-000001
CUSTOMER-000002
CUSTOMER-000003
```

Rules

- IDs are generated automatically.
- IDs are never reused.
- IDs never change.
- IDs remain valid after archival.

---

# Required Fields

A Customer cannot exist without:

- Customer ID
- Legal Name
- Customer Type
- Industry
- Status
- Account Owner
- Primary Contact
- Payment Terms
- Billing Address

---

# Optional Fields

Examples include:

- Trading Name
- Credit Limit
- Preferred Currency
- Customer Health
- Website
- LinkedIn
- Annual Revenue
- Notes

Optional information should enhance decision-making without preventing customer creation.

---

# Controlled Values

The following fields must use approved values.

Customer Type

- Corporate
- Government
- Municipality
- School
- University
- Hospital
- Mining Company
- Distributor
- Retail
- Manufacturer
- Other

Status

- Prospect
- Lead
- Qualified Lead
- Customer
- Active Customer
- Preferred Customer
- Dormant Customer
- Archived Customer

Payment Terms

- COD
- 7 Days
- 14 Days
- 30 Days
- 60 Days
- Custom

---

# Relationships

The Customer object owns relationships with:

```
Customer
│
├── Contact
├── Opportunity
├── Quote
├── Sales Order
├── Invoice
├── Complaint
├── Meeting
├── Task
├── Product
├── Project
└── Contract
```

---

# Data Ownership

| Information | Owner |
|-------------|-------|
| Customer Identity | Sales |
| Financial Information | Finance |
| Delivery Information | Operations |
| Procurement Information | Procurement |
| AI Summary | AI Agent |
| Customer Health | Customer Success |

Ownership determines who is responsible for maintaining data quality.

---

# Data Quality Rules

Customer information should always be:

- Complete
- Accurate
- Consistent
- Current
- Auditable
- Secure

Incomplete information should be flagged for review.

---

# Future Expansion

The Customer Data Model has been designed to support future capabilities including:

- Multiple Companies
- Multi-Currency
- International Customers
- Parent-Child Organisations
- CRM Synchronisation
- ERP Synchronisation
- API Exposure
- Data Warehouse Integration
- Knowledge Graph Integration
- AI Memory
- Digital Customer Twins

---

# Data Model Summary

The Customer Data Model provides the canonical representation of every Customer within Swissbay Nexus.

It establishes one consistent structure that can be implemented across software platforms, integrations and Artificial Intelligence while remaining independent of any specific technology.

By governing customer information through a shared business model, Swissbay ensures that every decision is made using trusted, consistent and reusable data.