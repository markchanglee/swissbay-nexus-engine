# 04 — Scope

---

# Overview

The Product Business Object defines the boundaries of product management within the Swissbay Nexus platform.

Its purpose is to establish clear ownership of product master information while preventing duplication across Procurement, Sales, Warehousing, Finance, Projects and Customer Management.

This document defines:

- what the Product Business Object owns
- what it references
- what is intentionally excluded
- where responsibilities begin and end

Well-defined boundaries ensure that Products remain reusable enterprise assets rather than application-specific records.

---

# Scope Statement

The Product Business Object is responsible for managing the identity, classification, lifecycle and governance of every product, service, material and commercial offering managed by Swissbay.

The Product Business Object owns product master information.

It does not own inventory transactions, sales orders, contracts, pricing history or financial postings.

Those responsibilities belong to their respective Business Objects.

---

# In Scope

The Product Business Object is responsible for:

## Product Identity

- Product Identifier
- Product Code
- Product Name
- Product Description
- Product Type
- Product Brand
- Product Model
- Product Version

---

## Product Classification

- Product Category
- Product Family
- Product Group
- Product Line
- Product Status
- Industry Classification
- Tax Classification

---

## Product Characteristics

- Unit of Measure
- Dimensions
- Weight
- Colour
- Material
- Packaging
- Shelf Life
- Country of Origin

---

## Commercial Information

- Standard Cost
- List Price
- Currency
- Pricing Method
- Warranty Period

Pricing history belongs to Finance and Sales.

The Product Business Object stores only the current governed commercial attributes.

---

## Product Lifecycle

- Draft
- Review
- Approved
- Active
- Discontinued
- Retired
- Archived

Lifecycle governance belongs to the Product Business Object.

---

## Product Relationships

The Product Business Object maintains governed relationships with:

- Suppliers
- Warehouses
- Sales Orders
- Customers
- Projects
- Assets
- Contracts
- Opportunities

Products are referenced rather than duplicated.

---

# Out of Scope

The Product Business Object does not own:

## Inventory Transactions

Inventory movements

Stock adjustments

Receiving

Picking

Transfers

These belong to the Warehouse Business Object.

---

## Sales Orders

Sales Orders belong to:

OBJ-010 Sales Order

---

## Customer Information

Customer ownership belongs to:

OBJ-001 Customer

---

## Supplier Information

Supplier ownership belongs to:

OBJ-002 Supplier

---

## Contracts

Contract ownership belongs to:

OBJ-005 Contract

---

## Financial Transactions

Invoices

Payments

General Ledger

Inventory valuation journals

Financial postings

These belong to Finance.

---

## Projects

Project ownership belongs to:

OBJ-006 Project

---

# Referenced Business Objects

The Product Business Object references:

- Customer
- Supplier
- Warehouse
- Asset
- Contract
- Opportunity
- Sales Order
- Project

Relationships are maintained using permanent Business Object identifiers.

---

# Business Boundaries

The Product Business Object begins when:

- a new product is proposed
- product information is captured
- governance begins

The Product Business Object ends when:

- the product is permanently retired
- governance requirements have been satisfied
- retention obligations have been met

Historical references remain available for reporting and audit purposes.

---

# Responsibilities

The Product Business Object is responsible for:

- product master data
- product lifecycle
- product classification
- product governance
- product relationships
- product discoverability

The Product Business Object is not responsible for inventory operations or commercial transactions.

---

# AI Scope

Artificial Intelligence may:

- classify products
- recommend categories
- detect duplicate products
- recommend substitute products
- forecast demand
- identify pricing anomalies
- generate product summaries

Artificial Intelligence may not:

- approve products
- change product ownership
- bypass governance
- alter lifecycle status without approval

Human accountability remains mandatory.

---

# Security Scope

Security responsibilities include:

- role-based access
- product confidentiality
- approval permissions
- audit logging
- attribute-level security

Security follows the Swissbay Security Standard.

---

# Integration Scope

The Product Business Object may integrate with:

- ERP
- Warehouse Management Systems
- Sales Platforms
- Procurement Systems
- Manufacturing Systems
- Finance Systems
- Microsoft Fabric
- Databricks
- AI Services

The Product Business Object remains the canonical product definition regardless of implementation technology.

---

# Future Scope

Future enhancements may include:

- digital product twins
- AI product assistants
- sustainability metrics
- carbon footprint
- product lifecycle optimisation
- intelligent product recommendations
- predictive replenishment

These enhancements extend rather than redefine the Product Business Object.

---

# Scope Validation

Before approval verify that:

- ownership is defined
- business boundaries are clear
- responsibilities are assigned
- duplicated ownership is avoided
- related Business Objects are referenced
- AI boundaries are governed

---

# Scope Summary

The Product Business Object owns the enterprise definition of every product within Swissbay Nexus.

It deliberately excludes inventory transactions, financial processing and sales execution while maintaining governed relationships with the Business Objects that perform those functions.

This separation ensures that Products remain reusable, scalable and trusted across every department, application and AI capability within the Swissbay Nexus platform.