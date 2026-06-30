# 07 — Naming Convention Standard

---

# Purpose

The Naming Convention Standard defines how Business Objects, documents, workflows, dashboards, automations, AI Agents and supporting artefacts are named throughout the Swissbay Nexus platform.

Consistent naming improves discoverability, governance, automation and communication.

A name should immediately communicate what an artefact is, its purpose and its place within the platform.

---

# Objective

The objectives of this standard are to:

- establish consistent naming across the platform
- eliminate ambiguity
- improve AI interpretation
- support automation
- simplify searching
- improve maintainability
- support future scalability

---

# Philosophy

Swissbay believes that names are part of the architecture.

A good name should:

- describe the business concept
- remain stable over time
- avoid unnecessary abbreviations
- be understandable by both humans and AI

Naming should always favour clarity over brevity.

---

# General Rules

Every name should be:

- descriptive
- unique within its scope
- business-focused
- technology independent
- written in Title Case for display names
- written in a consistent machine-readable format where required

Avoid:

- personal abbreviations
- project nicknames
- temporary names
- implementation-specific terminology

---

# Business Object Naming

Business Objects use the following format:

```
OBJ-001 Customer

OBJ-002 Supplier

OBJ-003 Product

OBJ-004 Employee
```

Rules:

- Prefix with `OBJ-`
- Three-digit identifier
- Singular business noun
- Display name in Title Case

---

# Foundation Standards

Foundation Standards use the format:

```
NX-000 Constitution

OBJ-000 Business Object Standard

DATA-000 Data Standard

AI-000 AI Operating Standard

WF-000 Workflow Standard

SEC-000 Security Standard
```

Rules:

- Standard identifier
- Meaningful title
- Version managed independently

---

# Workflow Naming

Workflow documents use:

```
WF-CUST-001 Create Customer

WF-CUST-002 Update Customer

WF-SUP-001 Approve Supplier
```

Rules:

- Prefix `WF`
- Business Object code
- Sequential number
- Verb + Business Object

---

# Business Rule Naming

Business Rules use:

```
BR-CUST-001

BR-CUST-002

BR-SUP-001
```

Rules:

- Prefix `BR`
- Object identifier
- Sequential numbering

Business Rule IDs never change.

---

# KPI Naming

KPIs use:

```
KPI-CUST-001 Customer Growth Rate

KPI-CUST-002 Revenue per Customer

KPI-SUP-001 Supplier Performance
```

---

# Dashboard Naming

Dashboards use:

```
DASH-001 Executive Dashboard

DASH-002 Sales Dashboard

DASH-003 Finance Dashboard
```

---

# Automation Naming

Automations use:

```
AUTO-CUST-001 Customer Created

AUTO-CUST-002 Dormant Customer

AUTO-SUP-001 Supplier Approved
```

---

# AI Agent Naming

AI Agents use:

```
AI-001 CEO Advisor

AI-002 Sales Advisor

AI-003 Procurement Advisor

AI-004 Customer Success Advisor
```

Names should describe the business role rather than the underlying model.

---

# API Naming

REST endpoints should follow resource naming.

Examples:

```
/customers

/customers/{id}

/suppliers

/products

/orders
```

Use plural nouns for collections.

Avoid verbs in endpoint names where HTTP methods already express the action.

---

# File Naming

Markdown documents should follow:

```
01_Executive_Summary.md

02_Purpose.md

03_Business_Value.md
```

Rules:

- Two-digit section number
- Underscore separator
- Title Case words separated by underscores
- `.md` extension

---

# Folder Naming

Folders should use Pascal Case or approved platform naming.

Examples:

```
OBJECTS

FOUNDATIONS

WORKFLOWS

AI

DASHBOARDS

AUTOMATION
```

Avoid spaces in folder names.

---

# Identifier Standards

Every Business Object should define a permanent identifier.

Examples:

```
CUSTOMER-000001

SUPPLIER-000001

PRODUCT-000001

EMPLOYEE-000001
```

Rules:

- Uppercase prefix
- Hyphen separator
- Fixed-width numeric sequence
- Never reused
- Never edited manually

---

# Reserved Prefixes

| Prefix | Meaning |
|----------|----------|
| NX | Nexus Foundation |
| OBJ | Business Object |
| DATA | Data Standard |
| AI | Artificial Intelligence |
| WF | Workflow |
| BR | Business Rule |
| KPI | Key Performance Indicator |
| DASH | Dashboard |
| AUTO | Automation |
| SEC | Security |
| VALID | Validation |
| API | API Specification |
| DOC | Supporting Documentation |

Reserved prefixes must not be reused for other purposes.

---

# Naming Validation

Before approval verify that:

- names are descriptive
- numbering is unique
- prefixes follow standards
- abbreviations are approved
- filenames follow conventions
- identifiers remain stable

---

# Common Mistakes

Avoid:

- duplicate identifiers
- inconsistent numbering
- plural Business Object names
- technology-specific names
- changing identifiers after publication
- mixing naming styles

Consistency is more important than creativity.

---

# AI Generation Guidance

When generating names, AI should:

- follow the approved prefix
- use business terminology
- avoid abbreviations unless approved
- ensure uniqueness
- preserve numbering conventions

AI should never invent new prefixes without governance approval.

---

# Review Questions

Governance reviewers should ask:

- Does the name clearly describe the artefact?
- Does it follow the approved format?
- Is the identifier unique?
- Will the name still make sense in five years?
- Can AI reliably interpret the name?

---

# Deliverable

Every Business Object and supporting artefact within Swissbay Nexus must follow this naming convention.

Consistent naming enables governance, automation, AI interpretation and long-term scalability across the platform.

---

# Standard Summary

The Naming Convention Standard provides a unified language for identifying every artefact within Swissbay Nexus.

By standardising names, identifiers and numbering, Swissbay creates a platform that is easier to understand, search, automate and maintain.

Naming is therefore a core architectural capability rather than a documentation preference.