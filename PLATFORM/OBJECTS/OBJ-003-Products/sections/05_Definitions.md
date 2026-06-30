# 05 — Definitions

---

# Overview

This document defines the official business terminology used by the Product Business Object.

These definitions establish a common enterprise language for Products across Procurement, Operations, Warehousing, Sales, Finance, Manufacturing, Projects, Artificial Intelligence and Executive Management.

Every Product within Swissbay Nexus should be interpreted consistently regardless of business unit, application or industry.

The definitions contained within this document are the authoritative terminology for product management across the Swissbay Nexus platform.

---

# Core Definitions

## Product

A Product is any governed item, service, material or commercial offering that delivers value to customers or supports internal business operations.

A Product may represent:

- Physical Goods
- Services
- Digital Products
- Raw Materials
- Finished Goods
- Spare Parts
- Mining Commodities
- Healthcare Procedures
- Software Licences
- Subscriptions

Every Product is uniquely represented by one Product Business Object.

---

## Product Identifier

The permanent, unique identifier assigned to every Product.

Example

```
PRODUCT-000001
```

Product Identifiers:

- never change
- are never reused
- uniquely identify a Product across the platform

---

## Product Code

A human-readable business identifier assigned to a Product.

Example

```
SKU-100245
```

Product Codes:

- should be unique
- may follow organisational standards
- may differ from the permanent Product Identifier

---

## Product Name

The official business name used to identify the Product.

Example

```
Hydraulic Pump Assembly
```

Every Product must have one approved Product Name.

---

## Product Description

A structured explanation describing the Product's purpose, characteristics and intended use.

Descriptions should be clear, concise and business-focused.

---

## Product Category

A high-level classification describing the type of Product.

Examples include:

- Equipment
- Consumables
- Services
- Software
- Healthcare
- Mining
- Construction
- Office Supplies

Categories support reporting and governance.

---

## Product Family

A logical grouping of similar Products that share common characteristics.

Example

```
Hydraulic Pumps
```

---

## Product Group

A broader business grouping used for reporting, planning and analytics.

Multiple Product Families may belong to one Product Group.

---

## Product Type

Defines the operational nature of the Product.

Examples include:

- Physical Product
- Service
- Digital Product
- Subscription
- Raw Material
- Finished Good
- Spare Part

---

## Unit of Measure

The standard unit used when purchasing, storing or selling a Product.

Examples include:

- Each
- Kilogram
- Litre
- Metre
- Hour
- Licence

Only approved Units of Measure may be used.

---

## Product Lifecycle

The controlled sequence of stages through which a Product progresses.

Typical stages include:

- Draft
- Review
- Approved
- Active
- Discontinued
- Retired
- Archived

Each Product exists in only one lifecycle stage at a time.

---

## Product Status

The current operational condition of the Product.

Examples include:

- Active
- Inactive
- Pending Approval
- Retired
- Archived

Status supports operational decision-making.

---

## Product Variant

A Product that differs from another Product through one or more controlled characteristics.

Examples include:

- Size
- Colour
- Capacity
- Packaging
- Configuration

Variants inherit the same business meaning while maintaining their own identifiers where required.

---

## Bill of Materials (BOM)

A structured list of components required to manufacture, assemble or configure a Product.

The Product Business Object may reference a Bill of Materials but does not own manufacturing execution.

---

## Product Owner

The department or individual responsible for the governance, quality and lifecycle of the Product Business Object.

Default Business Owner:

**Operations / Product Management**

---

## Product Cost

The governed standard cost assigned to a Product.

This represents the current approved cost.

Historical costing belongs to Finance.

---

## Product Price

The current approved selling price or list price for a Product.

Historical pricing and transactional pricing belong to Sales and Finance.

---

## Artificial Intelligence

Artificial Intelligence refers to governed AI capabilities that analyse Product information to improve inventory management, forecasting, product recommendations and operational planning.

AI supports business users but never replaces governance.

---

# Approved Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| SKU | Stock Keeping Unit |
| BOM | Bill of Materials |
| UOM | Unit of Measure |
| AI | Artificial Intelligence |
| ERP | Enterprise Resource Planning |
| KPI | Key Performance Indicator |
| API | Application Programming Interface |
| ID | Identifier |

Only approved abbreviations should be used throughout the Product Business Object.

---

# Terminology Rules

The following terminology rules apply throughout the Product Business Object.

- Use **Product** rather than Item wherever possible.
- Use **Product Identifier** rather than Product ID in formal documentation.
- Use **Business Object** rather than Record.
- Use **Product Lifecycle** rather than Status when referring to governance stages.
- Use **Unit of Measure (UOM)** rather than free-text units.

Consistent terminology improves reporting, governance and AI interpretation.

---

# AI Interpretation

Artificial Intelligence should interpret every Product term according to this document.

AI should not invent alternative business meanings or classifications.

Where ambiguity exists, this document takes precedence.

---

# Definition Governance

All Product definitions are governed enterprise assets.

Changes require:

- Business Review
- Product Owner Approval
- Governance Review
- Version Update

Definitions evolve only through controlled governance.

---

# Definitions Summary

This document establishes the official enterprise vocabulary for the Product Business Object.

By defining consistent terminology for Products, classifications, lifecycles, identifiers and commercial concepts, Swissbay Nexus ensures that employees, systems, integrations and Artificial Intelligence all operate from the same business understanding.

These definitions form the semantic foundation for product management across the Swissbay Nexus platform.