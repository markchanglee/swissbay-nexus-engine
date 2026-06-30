# 04 — Scope

---

# Overview

The Supplier Business Object defines the boundaries of supplier management within the Swissbay Nexus platform.

Its purpose is to establish a clear separation of responsibilities between the Supplier Business Object and other Business Objects, ensuring that supplier information remains governed, reusable and free from unnecessary duplication.

This document defines:

- what the Supplier Business Object owns
- what it references
- what is intentionally excluded
- where responsibilities begin and end

Clear boundaries improve governance, scalability and maintainability.

---

# Scope Statement

The Supplier Business Object is responsible for managing the identity, lifecycle, governance and performance of organisations and individuals that supply products, services or strategic capabilities to Swissbay.

The Supplier Business Object owns supplier master information.

It does not own procurement transactions, contracts, invoices or products.

Those are managed by their respective Business Objects.

---

# In Scope

The Supplier Business Object is responsible for:

## Supplier Identity

- Supplier Identifier
- Supplier Name
- Trading Name
- Supplier Type
- Registration Information
- Tax Information
- Legal Entity Details

---

## Supplier Classification

- Supplier Category
- Industry
- Commodity
- Strategic Supplier Status
- Preferred Supplier Status
- Supplier Tier
- Risk Classification

---

## Contact Information

- Primary Contact
- Secondary Contacts
- Telephone Numbers
- Email Addresses
- Website
- Physical Address
- Postal Address

---

## Supplier Lifecycle

- Supplier Registration
- Qualification
- Approval
- Active Management
- Performance Review
- Suspension
- Reactivation
- Offboarding

---

## Supplier Governance

- Approval Status
- Compliance Status
- Certifications
- Audit Information
- Review Dates
- Ownership

---

## Supplier Performance

- Performance Score
- Delivery Performance
- Quality Performance
- Responsiveness
- Risk Rating
- Preferred Supplier Status

---

## Supplier Relationships

The Supplier Business Object maintains governed relationships with:

- Products
- Contracts
- Purchase Requests
- Purchase Orders
- Projects
- Assets
- Invoices
- Payments

Supplier information is referenced rather than duplicated.

---

# Out of Scope

The Supplier Business Object does not own:

## Products

Products belong to:

OBJ-003 Product

---

## Contracts

Contracts belong to:

OBJ-005 Contract

---

## Projects

Projects belong to:

OBJ-006 Project

---

## Assets

Assets belong to:

OBJ-007 Asset

---

## Warehouses

Warehouse operations belong to:

OBJ-008 Warehouse

---

## Sales Orders

Sales Orders belong to:

OBJ-010 Sales Order

---

## Financial Transactions

Supplier invoices

Payments

General Ledger entries

Financial postings

These belong to Finance Business Objects.

---

## Inventory

Inventory quantities

Warehouse stock

Stock movements

Inventory valuation

These belong to Warehouse and Inventory Business Objects.

---

# Referenced Business Objects

The Supplier Business Object references but does not own:

- Customer
- Product
- Contract
- Project
- Asset
- Warehouse
- Sales Order
- Invoice
- Payment

Relationships are maintained through permanent Business Object identifiers.

---

# Business Boundaries

The Supplier Business Object begins when:

- a supplier is identified
- supplier information is captured
- supplier governance begins

The Supplier Business Object ends when:

- supplier information is archived
- supplier relationship is terminated
- retention requirements have been satisfied

Business transactions continue to exist independently.

---

# Responsibilities

The Supplier Business Object is responsible for:

- supplier master data
- supplier governance
- supplier lifecycle
- supplier ownership
- supplier relationships
- supplier performance information

The Supplier Business Object is not responsible for executing procurement transactions.

---

# AI Scope

Artificial Intelligence may:

- recommend suppliers
- analyse supplier performance
- detect duplicates
- predict supplier risk
- identify missing information
- summarise supplier history

Artificial Intelligence may not:

- approve suppliers
- modify supplier information without authorisation
- bypass procurement governance
- override supplier classifications

Human accountability remains mandatory.

---

# Security Scope

Security responsibilities include:

- role-based access
- supplier confidentiality
- audit history
- approval permissions
- document visibility

Supplier security follows the Swissbay Security Standard.

---

# Integration Scope

The Supplier Business Object may integrate with:

- ERP
- CRM
- Finance Systems
- Procurement Platforms
- Contract Management
- AI Services
- Reporting Platforms
- API Gateway

The Supplier Business Object remains the canonical supplier definition regardless of integration technology.

---

# Future Scope

Future enhancements may include:

- supplier ESG scoring
- supplier digital twins
- AI procurement advisors
- predictive supplier risk
- global supplier directories
- supplier collaboration portals
- automated compliance monitoring

Future capabilities extend rather than redefine the Supplier Business Object.

---

# Scope Validation

Before approval verify that:

- ownership is clear
- boundaries are defined
- duplication is avoided
- related Business Objects are referenced
- responsibilities are separated
- AI responsibilities are governed

---

# Scope Summary

The Supplier Business Object owns supplier master information and supplier governance within Swissbay Nexus.

It deliberately excludes procurement transactions, products, contracts and financial processing, instead referencing those Business Objects through governed relationships.

By maintaining clear architectural boundaries, the Supplier Business Object remains reusable, scalable and aligned with the Swissbay Business Object Standard.