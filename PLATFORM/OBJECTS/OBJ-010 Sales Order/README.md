# OBJ-010 — Sales Order

## Overview

The Sales Order Business Object defines the governed representation of every customer order processed within Swissbay Nexus.

A Sales Order represents a customer's formal request to purchase one or more Products under agreed commercial terms.

The Sales Order Business Object connects Customers, Products, Pricing, Warehouses, Contracts, Projects, Assets and Finance into a single governed commercial transaction.

Unlike Customer, Supplier and Product, the Sales Order is a transactional Business Object that captures business events rather than master data.

---

## Purpose

The purpose of the Sales Order Business Object is to establish a single governed representation of every commercial sales transaction.

Rather than allowing ERP systems, CRM systems and eCommerce platforms to maintain independent interpretations of sales orders, Swissbay governs Sales Orders through one canonical Business Object.

---

## Inherits From

- OBJ-000 Business Object Standard
- DATA-000 Data Standard
- WF-000 Workflow Standard
- KPI-000 KPI Standard
- DASH-000 Dashboard Standard
- VALID-000 Validation Standard
- SEC-000 Security Standard
- AUTO-000 Automation Standard
- AI-000 AI Operating Standard

---

## Object Owner

Primary Owner

Sales Operations

Supporting Owners

- Sales
- Finance
- Warehouse
- Customer Service

---

## Related Business Objects

- OBJ-001 Customer
- OBJ-002 Supplier
- OBJ-003 Product
- OBJ-004 Employee
- OBJ-005 Contract
- OBJ-006 Project
- OBJ-007 Asset
- OBJ-008 Warehouse
- OBJ-009 Opportunity

---

## Status

Draft v1.0.0