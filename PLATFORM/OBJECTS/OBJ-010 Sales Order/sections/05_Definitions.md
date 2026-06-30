# 05 — Definitions

---

# Overview

This document defines the official business terminology used by the Sales Order Business Object.

These definitions establish a common enterprise language for commercial transactions across Sales, Customer Service, Finance, Warehouse Operations, Executive Management and Artificial Intelligence.

Every Sales Order within Swissbay Nexus should be interpreted consistently regardless of department, application or sales channel.

The definitions contained within this document are the authoritative terminology for order management across the Swissbay Nexus platform.

---

# Core Definitions

## Sales Order

A Sales Order is a governed commercial transaction representing a customer's request to purchase one or more Products under agreed commercial terms.

A Sales Order records:

- Customer
- Products
- Quantities
- Pricing
- Taxes
- Delivery Information
- Payment Terms
- Order Status

Every Sales Order is uniquely represented by one Sales Order Business Object.

---

## Sales Order Identifier

The permanent, unique identifier assigned to every Sales Order.

Example

```
SO-2026-000001
```

Sales Order Identifiers:

- never change
- are never reused
- uniquely identify a transaction

---

## Sales Order Number

A human-readable business reference used by customers and employees.

Example

```
SO-100245
```

The Sales Order Number is unique within the organisation.

---

## Customer

The organisation or individual purchasing Products.

Customer ownership belongs to:

OBJ-001 Customer

The Sales Order references Customers but never owns them.

---

## Order Line

An individual Product contained within a Sales Order.

Each Order Line includes:

- Product Reference
- Quantity
- Unit Price
- Discount
- Tax
- Extended Amount

A Sales Order contains one or more Order Lines.

---

## Product Reference

A governed reference to a Product Business Object.

The Sales Order stores:

- Product Identifier
- Quantity
- Price at Time of Sale

Product ownership belongs to:

OBJ-003 Product

---

## Order Status

The current operational state of the Sales Order.

Examples include:

- Draft
- Submitted
- Approved
- Allocated
- Fulfilled
- Delivered
- Invoiced
- Completed
- Cancelled
- Closed

Every Sales Order exists in one status at a time.

---

## Order Lifecycle

The controlled sequence of stages through which a Sales Order progresses from creation through completion or cancellation.

The lifecycle governs approvals, fulfilment and auditability.

---

## Payment Terms

The agreed commercial terms governing customer payment.

Examples include:

- Cash
- COD
- 30 Days
- 60 Days
- Prepaid

Payment processing belongs to Finance.

---

## Delivery Method

The agreed method used to deliver Products.

Examples include:

- Collection
- Courier
- Freight
- Internal Delivery
- Digital Delivery

---

## Shipping Address

The destination where Products are delivered.

The Sales Order stores the address snapshot at the time of ordering.

Changes to the Customer record do not alter historical Sales Orders.

---

## Billing Address

The address used for invoicing.

The Billing Address is stored as part of the transaction history.

---

## Currency

The currency applicable to the commercial transaction.

Examples include:

- ZAR
- USD
- EUR
- GBP

Currency is fixed at the time the Sales Order is created unless changed through an approved business process.

---

## Tax

The calculated tax applicable to the transaction.

Examples include:

- VAT
- GST
- Sales Tax

Tax calculations may be performed by external Finance systems but the resulting value forms part of the Sales Order.

---

## Discount

A reduction applied to the standard selling price.

Discounts may be:

- Line Discount
- Order Discount
- Promotional Discount
- Contract Discount

Discount approval follows governed commercial rules.

---

## Fulfilment

The operational process of preparing and delivering Products to the Customer.

Fulfilment may include:

- allocation
- picking
- packing
- shipment
- delivery

Execution belongs to Warehouse Operations.

The Sales Order tracks fulfilment status.

---

## Invoice

The financial document requesting payment for fulfilled Products.

Invoices belong to the Finance domain.

The Sales Order may reference an Invoice but does not own it.

---

## Artificial Intelligence

Artificial Intelligence refers to governed AI capabilities that analyse Sales Orders to improve forecasting, fulfilment, customer service and operational planning.

AI supports business users but never replaces commercial governance.

---

# Approved Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| SO | Sales Order |
| SKU | Stock Keeping Unit |
| VAT | Value Added Tax |
| AI | Artificial Intelligence |
| ERP | Enterprise Resource Planning |
| CRM | Customer Relationship Management |
| API | Application Programming Interface |
| KPI | Key Performance Indicator |
| ID | Identifier |

Only approved abbreviations should be used throughout the Sales Order Business Object.

---

# Terminology Rules

The following terminology rules apply throughout the Sales Order Business Object.

- Use **Sales Order** rather than Order where practical.
- Use **Sales Order Identifier** rather than Order ID in formal documentation.
- Use **Order Line** rather than Item.
- Use **Product Reference** rather than Product Record.
- Use **Order Lifecycle** when referring to governed stages.

Consistent terminology improves governance, reporting and AI interpretation.

---

# AI Interpretation

Artificial Intelligence should interpret every Sales Order term according to this document.

AI should not invent alternative commercial meanings.

Where ambiguity exists, this document takes precedence.

---

# Definition Governance

All Sales Order definitions are governed enterprise assets.

Changes require:

- Business Review
- Sales Operations Approval
- Governance Review
- Version Update

Definitions evolve only through controlled governance.

---

# Definitions Summary

This document establishes the official enterprise vocabulary for the Sales Order Business Object.

By defining consistent terminology for commercial transactions, order lines, fulfilment, pricing, taxation, delivery and lifecycle management, Swissbay Nexus ensures that employees, systems, integrations and Artificial Intelligence all operate from the same business understanding.

These definitions form the semantic foundation for commercial transaction management across the Swissbay Nexus platform.