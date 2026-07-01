# 08 — Relationships

---

# Overview

The Contract Business Object connects legal and commercial governance to enterprise operations.

Contracts govern relationships with customers, suppliers, employees, products, projects, opportunities, assets and sales orders.

---

# Relationship Map

```text
Customer ── signs ── Contract ── governs ── Sales Order
Supplier ── signs ── Contract ── governs ── Product
Employee ── owns ─── Contract ── governs ── Project
```

---

# Customer Relationship

Customer contracts define commercial terms, obligations and service expectations.

---

# Supplier Relationship

Supplier contracts govern procurement, service levels, pricing, delivery terms and compliance obligations.

---

# Employee Relationship

Employees may draft, review, approve, own or be responsible for Contracts.

---

# Product Relationship

Contracts may define product pricing, warranty, service, licensing or support terms.

---

# Sales Order Relationship

Sales Orders may reference Contracts for pricing, discounts, payment terms and fulfilment obligations.

---

# Opportunity Relationship

Opportunities may convert into Contracts before becoming Sales Orders.

---

# Project Relationship

Projects may be governed by Contracts, statements of work or service agreements.

---

# Asset Relationship

Assets may be governed by lease, warranty, service or maintenance contracts.

---

# AI Relationships

AI analyses Contracts for risk, obligations, renewals, clause comparison and compliance issues.

---

# Knowledge Graph Representation

```text
Contract
├── signed by → Customer
├── signed by → Supplier
├── owned by → Employee
├── governs → Product
├── governs → Sales Order
├── governs → Project
├── governs → Asset
├── contains → Obligation
└── analysed by → AI
```

---

# Relationship Governance

Every relationship must be valid, auditable and lifecycle-compatible.

---

# Relationship Summary

The Contract Business Object is the legal and commercial relationship hub of Swissbay Nexus.
