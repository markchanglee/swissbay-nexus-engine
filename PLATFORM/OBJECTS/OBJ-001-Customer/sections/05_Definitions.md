# 04 — Scope

---

# Overview

The purpose of this section is to clearly define the boundaries of the Customer Business Object.

One of the most common causes of poor business systems is unclear ownership of information. When multiple objects attempt to manage the same information, duplication, inconsistency and confusion quickly follow.

The Scope of the Customer object establishes exactly what information belongs to the Customer, what relationships it maintains, and where responsibility passes to other Business Objects.

This section ensures that Swissbay Nexus remains modular, scalable and maintainable as the platform grows.

---

# Scope Statement

The Customer Business Object is responsible for representing the commercial relationship between Swissbay and an external organisation or individual that purchases, or is approved to purchase, products or services.

It defines the identity of the customer, the ownership of the relationship, and the commercial context required for Swissbay to conduct business.

The Customer object does **not** own every piece of information relating to that customer. Instead, it acts as the central reference point that connects specialised Business Objects together.

---

# In Scope

The Customer object is responsible for maintaining the following information.

## Customer Identity

* Customer ID
* Legal Name
* Trading Name
* Company Registration Number
* VAT Number
* Customer Status
* Customer Type
* Industry
* Business Classification

---

## Relationship Ownership

* Account Owner
* Sales Representative
* Customer Success Manager
* Relationship Status
* Strategic Account Indicator

---

## Customer Contacts

The Customer object maintains references to:

* Primary Contact
* Procurement Contact
* Finance Contact
* Operations Contact
* Executive Sponsor

Detailed contact information may eventually be managed through a dedicated Contact Business Object.

---

## Commercial Information

The Customer object references:

* Payment Terms
* Credit Status
* Credit Limit
* Preferred Currency
* Preferred Product Categories
* Preferred Delivery Method

---

## Operational Information

The object maintains references to:

* Billing Addresses
* Delivery Locations
* Receiving Instructions
* Delivery Constraints

---

## Relationship History

The Customer object maintains links to:

* Meetings
* Opportunities
* Quotes
* Sales Orders
* Invoices
* Contracts
* Complaints
* Tasks
* Notes
* AI Summaries

The detailed information remains owned by the respective Business Objects.

---

# Out of Scope

The following information is **not owned** by the Customer object.

---

## Product Information

Products belong to:

```text
OBJ-003 Product
```

The Customer object stores relationships to Products but does not define product specifications.

---

## Supplier Information

Supplier information belongs to:

```text
OBJ-002 Supplier
```

---

## Quote Details

Quotation content belongs to:

```text
OBJ-006 Quote
```

The Customer object only maintains the relationship.

---

## Sales Orders

Sales Orders belong to:

```text
OBJ-007 Sales Order
```

---

## Invoice Details

Invoices belong to:

```text
OBJ-008 Invoice
```

---

## Meetings

Meeting agendas, minutes and actions belong to:

```text
WF-Meeting
```

or the future Meeting Business Object.

---

## Tasks

Tasks belong to the Task workflow or Task Business Object.

---

## AI Decisions

The Customer object provides context for AI.

It does not own AI outputs or AI decisions.

Those belong to the relevant AI Agent.

---

# Boundary Rules

To keep Swissbay Nexus maintainable, the following rules apply.

## Rule 1

Each Business Object owns its own information.

---

## Rule 2

Objects communicate through relationships.

They do not duplicate data.

---

## Rule 3

The Customer object may reference another object but should not redefine it.

---

## Rule 4

If another Business Object changes, the Customer object should not require structural changes.

Only the relationship changes.

---

## Rule 5

Every piece of information must have exactly one owner.

---

# Customer Lifecycle Scope

The Customer object begins when:

* a Lead becomes an approved Customer

or

* management approves a trading account before the first sale.

The Customer object ends when:

* the relationship has been permanently closed
* all commercial obligations have been completed
* the account has been archived

Archived Customers remain part of Swissbay's business history and should never be permanently deleted if commercial transactions exist.

---

# Organisational Scope

The Customer object is shared across every department.

Departments consume the object differently, but ownership remains centralised.

Departments include:

* Sales
* Procurement
* Finance
* Operations
* Marketing
* Customer Success
* Executive Management
* Artificial Intelligence

This shared ownership model ensures that Swissbay operates from a single source of truth while allowing each department to fulfil its responsibilities.

---

# Future Scope

As Swissbay expands, the Customer object is expected to support:

* multiple legal entities
* multiple business units
* international operations
* customer hierarchies
* parent-child organisations
* customer groups
* customer portals
* digital customer profiles
* AI-generated customer intelligence
* external CRM synchronisation
* ERP integration

The object has therefore been designed with long-term scalability in mind.

---

# Scope Summary

The Customer Business Object defines **who the customer is**.

It does **not** attempt to own every piece of information associated with that customer.

Instead, it acts as the central business reference that connects all customer-related Business Objects through governed relationships.

This clear separation of responsibility allows Swissbay Nexus to remain modular, scalable and adaptable while maintaining a single, trusted definition of every customer across the organisation.
