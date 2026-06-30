# 04 — Scope

---

# Overview

The Sales Order Business Object defines the business boundaries for managing commercial sales transactions within the Swissbay Nexus platform.

It establishes clear ownership of transactional order information while preventing duplication of master data owned by other Business Objects.

This document defines:

- what the Sales Order Business Object owns
- what it references
- what is intentionally excluded
- where responsibility begins and ends

Well-defined boundaries ensure that Sales Orders remain governed commercial transactions rather than collections of duplicated business information.

---

# Scope Statement

The Sales Order Business Object owns the complete commercial transaction between an organisation and its customer.

It governs:

- order creation
- order lifecycle
- order fulfilment
- order status
- commercial transaction history

The Sales Order Business Object references Customer, Product, Warehouse, Contract and Employee information but does not own those Business Objects.

---

# In Scope

The Sales Order Business Object is responsible for:

## Order Identity

- Sales Order Number
- Order Identifier
- Order Date
- Order Type
- Order Source
- Sales Channel

---

## Customer Reference

The Sales Order references:

- Customer
- Customer Contact
- Delivery Address
- Billing Address

Customer ownership belongs to the Customer Business Object.

---

## Product Lines

The Sales Order owns the transactional line items including:

- Product Reference
- Quantity Ordered
- Unit Price
- Discount
- Tax
- Extended Amount
- Requested Delivery Date

Product master information belongs to the Product Business Object.

---

## Commercial Information

The Sales Order owns:

- Currency
- Payment Terms
- Shipping Method
- Delivery Method
- Tax Amount
- Order Total
- Discount Total
- Freight Charges

Commercial values apply only to this transaction.

---

## Fulfilment Information

The Sales Order manages:

- Allocation Status
- Picking Status
- Packing Status
- Shipment Status
- Delivery Status
- Completion Status

Warehouse operations execute fulfilment but the Sales Order tracks the commercial status.

---

## Lifecycle Management

The Sales Order owns its operational lifecycle including:

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

Lifecycle governance belongs to the Sales Order Business Object.

---

## Transaction History

The Sales Order maintains:

- Status History
- Approval History
- Shipment History
- Change History
- Audit History

Historical records remain immutable.

---

# Out of Scope

The Sales Order Business Object does not own:

## Customer Information

Customer ownership belongs to:

OBJ-001 Customer

---

## Product Information

Product ownership belongs to:

OBJ-003 Product

---

## Supplier Information

Supplier ownership belongs to:

OBJ-002 Supplier

---

## Warehouse Operations

Warehouse ownership includes:

- inventory quantities
- storage locations
- picking execution
- packing execution
- inventory movements

These belong to the Warehouse Business Object.

---

## Financial Accounting

The Sales Order does not own:

- General Ledger
- Accounts Receivable
- Journal Entries
- Financial Posting
- Bank Transactions

These belong to Finance.

---

## Contracts

Commercial agreements belong to:

OBJ-005 Contract

The Sales Order may reference a Contract but never owns it.

---

## Opportunities

Sales Opportunities belong to:

OBJ-009 Opportunity

A Sales Order may originate from an Opportunity but remains a separate Business Object.

---

# Referenced Business Objects

The Sales Order Business Object references:

- Customer
- Product
- Supplier
- Warehouse
- Contract
- Employee
- Opportunity
- Project
- Asset

Relationships are maintained through permanent Business Object identifiers.

---

# Business Boundaries

The Sales Order Business Object begins when:

- a customer places an order
- an order is created internally
- an approved quotation is converted into an order

The Sales Order Business Object ends when:

- the order is completed
- the order is cancelled
- retention obligations have been met

Historical transactions remain available for reporting and audit purposes.

---

# Responsibilities

The Sales Order Business Object is responsible for:

- commercial transaction management
- order lifecycle
- fulfilment status
- pricing at the time of sale
- transactional audit history
- order traceability

It is not responsible for maintaining master data.

---

# AI Scope

Artificial Intelligence may:

- predict delivery delays
- identify fulfilment risks
- recommend substitute Products
- estimate revenue
- forecast order volumes
- detect pricing anomalies
- prioritise fulfilment

Artificial Intelligence may not:

- approve Sales Orders
- alter pricing
- modify Customers
- bypass commercial approvals
- complete financial transactions

Human accountability remains mandatory.

---

# Security Scope

Security responsibilities include:

- role-based access
- commercial confidentiality
- approval permissions
- audit logging
- financial data protection

Security follows the Swissbay Security Standard.

---

# Integration Scope

The Sales Order Business Object may integrate with:

- ERP Systems
- CRM Platforms
- Warehouse Management Systems
- Finance Systems
- Shipping Providers
- eCommerce Platforms
- Microsoft Fabric
- Databricks
- AI Services

The Sales Order remains the canonical commercial transaction regardless of implementation technology.

---

# Future Scope

Future enhancements may include:

- omnichannel order orchestration
- AI-assisted fulfilment
- intelligent delivery scheduling
- dynamic pricing recommendations
- digital order assistants
- predictive customer fulfilment
- autonomous order monitoring

These capabilities extend rather than redefine the Sales Order Business Object.

---

# Scope Validation

Before approval verify that:

- ownership is clearly defined
- business boundaries are understood
- transactional ownership is separated from master data
- related Business Objects are referenced
- lifecycle ownership is defined
- AI boundaries are governed

---

# Scope Summary

The Sales Order Business Object owns the complete commercial transaction between the organisation and its customer.

It intentionally excludes Customer, Product, Supplier, Warehouse and Contract ownership while maintaining governed relationships with those Business Objects.

This separation ensures that Sales Orders remain trusted transactional records that connect enterprise master data into governed commercial operations across the Swissbay Nexus platform.