# 11 — Department Usage

---

# Overview

The Supplier Business Object is a shared enterprise asset used across multiple business functions within Swissbay.

Although Procurement owns the Supplier Business Object, many departments contribute to and consume supplier information throughout the supplier lifecycle.

This document defines how each department interacts with the Supplier Business Object and clarifies ownership, responsibilities and expected business outcomes.

---

# Purpose

The Department Usage Model exists to:

- define departmental responsibilities
- establish ownership
- prevent duplicated effort
- improve collaboration
- support governance
- clarify accountability
- improve AI understanding of organisational roles

Every department should understand its role in supplier management.

---

# Department Responsibility Matrix

| Department | Create | Read | Update | Approve | Review |
|------------|:------:|:----:|:------:|:-------:|:------:|
| Procurement | ✓ | ✓ | ✓ | ✓ | ✓ |
| Finance |  | ✓ | Limited |  | ✓ |
| Operations |  | ✓ | Limited |  | ✓ |
| Legal |  | ✓ | Limited | ✓ | ✓ |
| Executive |  | ✓ |  | Strategic | ✓ |
| AI Agents |  | ✓ | Advisory | ✗ | Advisory |

---

# Procurement

## Role

Procurement is the Business Owner of the Supplier Business Object.

### Responsibilities

- Register suppliers
- Maintain supplier records
- Conduct supplier qualification
- Perform supplier approvals
- Monitor supplier performance
- Manage supplier relationships
- Initiate supplier offboarding

### Business Value

Procurement gains:

- governed supplier information
- consistent onboarding
- performance visibility
- supplier governance
- procurement analytics

---

# Finance

## Role

Finance consumes supplier information for financial processing.

### Responsibilities

- Verify supplier banking details
- Process supplier payments
- Review tax information
- Perform financial reconciliation
- Analyse supplier spend

### Business Value

Finance benefits from:

- trusted supplier master data
- reduced payment errors
- improved audit readiness
- better cash flow analysis

Finance does not own supplier information.

---

# Operations

## Role

Operations interacts with suppliers during service delivery and operational planning.

### Responsibilities

- Monitor delivery performance
- Escalate supplier issues
- Provide operational feedback
- Participate in supplier reviews

### Business Value

Operations gains:

- reliable supplier information
- improved planning
- supply continuity
- operational visibility

---

# Legal

## Role

Legal governs supplier contracts and regulatory compliance.

### Responsibilities

- Review supplier agreements
- Verify contractual compliance
- Maintain legal documentation
- Advise on supplier disputes

### Business Value

Legal benefits from:

- contract visibility
- compliance monitoring
- reduced legal risk
- centralised documentation

---

# Executive Management

## Role

Executives use supplier information for strategic oversight.

### Responsibilities

- Monitor strategic suppliers
- Review procurement performance
- Evaluate supplier risks
- Approve strategic supplier decisions

### Business Value

Executives receive:

- procurement dashboards
- supplier risk insights
- strategic sourcing information
- enterprise-wide supplier visibility

---

# Information Technology

## Role

Technology enables but does not own supplier information.

### Responsibilities

- maintain integrations
- support platform availability
- manage technical infrastructure
- protect supplier data

### Business Value

IT gains:

- governed integrations
- standard APIs
- simplified support
- reusable architecture

---

# Artificial Intelligence

## Role

AI operates as an advisory business capability.

### Responsibilities

AI may:

- analyse supplier performance
- detect duplicate suppliers
- recommend preferred suppliers
- identify procurement risks
- summarise supplier information
- predict supplier trends

AI may not:

- approve suppliers
- change supplier status
- modify supplier records
- bypass governance

---

# External Stakeholders

External stakeholders may interact with supplier information through approved integrations.

Examples include:

- Supplier Portals
- ERP Systems
- Government Services
- Banking Platforms
- Compliance Providers

Access remains governed by Swissbay security standards.

---

# Responsibility Model

```text
Executive

↓

Procurement

↓

Finance

↓

Operations

↓

Legal

↓

AI

↓

External Integrations
```

Each participant contributes according to clearly defined business responsibilities.

---

# Collaboration

Departments collaborate through governed workflows including:

- Supplier Onboarding
- Supplier Qualification
- Contract Approval
- Performance Reviews
- Compliance Audits
- Supplier Offboarding

Business Objects provide the shared information required for collaboration.

---

# Security Responsibilities

Each department is responsible for:

- protecting supplier information
- complying with access controls
- maintaining data quality
- following governance processes
- reporting security concerns

Security ownership remains shared across the organisation.

---

# AI Perspective

Artificial Intelligence uses the Department Usage Model to understand:

- who owns supplier information
- who may approve actions
- who should receive recommendations
- who should be notified
- who is accountable

This improves AI explainability and governance.

---

# Department Usage Summary

The Supplier Business Object enables multiple departments to work from a single governed source of supplier information while maintaining clear ownership and accountability.

By defining departmental responsibilities, Swissbay improves collaboration, strengthens governance and enables AI and automation to support the business without creating ambiguity around ownership or decision-making.