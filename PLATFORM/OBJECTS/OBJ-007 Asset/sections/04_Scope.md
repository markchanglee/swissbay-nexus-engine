# 04 — Scope

---

# Overview

The Asset Business Object defines the governance boundaries for enterprise asset management within Swissbay Nexus.

Its purpose is to identify which responsibilities belong to the Asset Business Object and which remain the responsibility of other Business Objects.

Clearly defined scope prevents duplication, simplifies integrations and strengthens enterprise governance.

---

# Purpose

The Scope Model exists to:

- define asset governance
- establish ownership boundaries
- eliminate duplication
- improve interoperability
- simplify maintenance
- support Artificial Intelligence

The Asset Business Object governs enterprise assets—not every operational transaction involving them.

---

# In Scope

The Asset Business Object governs:

- Asset Identity
- Asset Classification
- Asset Ownership
- Asset Custodian
- Asset Status
- Asset Lifecycle
- Asset Location
- Asset Condition
- Asset Valuation
- Maintenance History
- Inspection History
- Depreciation Information
- Warranty Information
- Retirement Information
- Disposal Information

These capabilities form the canonical representation of an enterprise Asset.

---

# Asset Information

The Asset Business Object owns:

- Asset Identifier
- Asset Name
- Asset Description
- Asset Category
- Asset Type
- Serial Number
- Manufacturer
- Model
- Purchase Date
- Acquisition Cost
- Current Status
- Assigned Owner
- Assigned Custodian

---

# Lifecycle Scope

Assets govern:

- acquisition
- commissioning
- operation
- maintenance
- inspection
- transfer
- retirement
- disposal

Lifecycle history remains permanently associated with the asset.

---

# Financial Scope

Assets maintain:

- acquisition value
- current book value
- depreciation method
- accumulated depreciation
- replacement estimate

General ledger accounting remains the responsibility of Finance systems.

---

# Maintenance Scope

Assets govern:

- maintenance schedules
- completed maintenance
- inspection records
- service history
- warranty information

Detailed maintenance work orders may be managed by specialised maintenance systems while remaining linked to the Asset.

---

# Location Scope

Assets maintain references to:

- Site
- Building
- Warehouse
- Department
- Project
- Employee

Location history remains fully auditable.

---

# Relationship Scope

Assets reference:

- Employees
- Suppliers
- Contracts
- Projects
- Warehouses
- Products

Identity remains owned by the corresponding Business Objects.

---

# Out of Scope

The Asset Business Object does **not** own:

- Employee master data
- Supplier master data
- Customer master data
- Financial ledger transactions
- Warehouse inventory
- Procurement transactions
- Sales Orders
- Payroll

These remain the responsibility of their respective Business Objects.

---

# AI Scope

Artificial Intelligence may:

- predict failures
- forecast maintenance
- estimate remaining useful life
- recommend replacement
- identify abnormal utilisation

AI may not:

- dispose of assets
- change valuations
- approve purchases
- override governance

---

# Scope Summary

The Asset Business Object governs the complete lifecycle of enterprise assets while coordinating related Business Objects through governed relationships.

Its scope is intentionally limited to asset governance, ensuring clear ownership boundaries, strong interoperability and a maintainable enterprise architecture.