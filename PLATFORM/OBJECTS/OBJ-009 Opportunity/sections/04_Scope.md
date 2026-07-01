# 04 — Scope

---

# Overview

The Opportunity Business Object defines the governance boundaries for enterprise opportunity management within Swissbay Nexus.

Its purpose is to identify which responsibilities belong to the Opportunity Business Object and which remain the responsibility of other Business Objects.

Clearly defined scope prevents duplication, simplifies integrations and strengthens enterprise governance.

---

# Purpose

The Scope Model exists to:

- define commercial governance
- establish ownership boundaries
- eliminate duplication
- improve interoperability
- simplify maintenance
- support Artificial Intelligence

The Opportunity Business Object governs opportunities—not every customer interaction or downstream commercial process.

---

# In Scope

The Opportunity Business Object governs:

- Opportunity Identity
- Opportunity Name
- Opportunity Type
- Sales Stage
- Opportunity Owner
- Customer Reference
- Estimated Value
- Win Probability
- Expected Close Date
- Pipeline Status
- Commercial Activities
- Opportunity History

These capabilities form the canonical representation of an enterprise Opportunity.

---

# Opportunity Information

The Opportunity Business Object owns:

- Opportunity Identifier
- Opportunity Name
- Description
- Opportunity Type
- Sales Stage
- Commercial Value
- Probability
- Expected Close Date
- Opportunity Owner
- Pipeline Status

---

# Commercial Scope

The Opportunity Business Object governs:

- opportunity registration
- qualification
- pipeline progression
- forecasting
- proposal tracking
- negotiation status
- win/loss recording
- opportunity closure

Commercial history remains permanently associated with the Opportunity.

---

# Forecasting Scope

The Opportunity Business Object maintains:

- estimated revenue
- probability
- forecast category
- expected close date
- pipeline weighting

Financial accounting remains governed by Finance systems.

---

# Relationship Scope

Opportunities reference:

- Customers
- Products
- Employees
- Contracts
- Projects
- Sales Orders
- Marketing Campaigns

Identity remains owned by the corresponding Business Objects.

---

# Out of Scope

The Opportunity Business Object does **not** own:

- Customer master data
- Product master data
- Contract documents
- Project execution
- Sales Orders
- Financial transactions
- Marketing content
- Employee records

These remain governed by their respective Business Objects.

---

# AI Scope

Artificial Intelligence may:

- predict win probability
- recommend next best actions
- identify pipeline risk
- forecast revenue
- recommend cross-sell opportunities
- summarise opportunity activity

AI may not:

- approve commercial discounts
- approve contracts
- modify opportunity ownership
- bypass Business Rules

Human accountability remains mandatory.

---

# Scope Summary

The Opportunity Business Object governs the complete commercial representation of enterprise opportunities while coordinating related Business Objects through governed relationships.

Its scope is intentionally limited to opportunity governance, ensuring clear ownership boundaries, strong interoperability and a maintainable enterprise architecture.