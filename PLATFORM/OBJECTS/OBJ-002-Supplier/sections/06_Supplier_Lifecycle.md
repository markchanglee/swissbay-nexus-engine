# 06 — Supplier Lifecycle

---

# Overview

The Supplier Lifecycle defines the complete journey of a supplier within the Swissbay Nexus platform.

A supplier is not simply created and forgotten. Every supplier progresses through a governed series of lifecycle stages that ensure appropriate evaluation, approval, management, monitoring and eventual retirement.

The lifecycle provides a consistent operational framework for Procurement, Finance, Operations, Legal, Executive Management and Artificial Intelligence.

---

# Purpose

The Supplier Lifecycle exists to:

- standardise supplier management
- improve procurement governance
- reduce supplier risk
- ensure regulatory compliance
- improve supplier performance
- support automation
- provide measurable lifecycle metrics

Every supplier must exist in one—and only one—lifecycle state at any point in time.

---

# Lifecycle Overview

Every supplier progresses through the following stages.

```text
Prospective

↓

Registered

↓

Qualification

↓

Approval

↓

Active

↓

Performance Review

↓

Suspended (optional)

↓

Reactivated (optional)

↓

Offboarded

↓

Archived
```

Each transition is governed by business rules and approval requirements.

---

# Stage 1 — Prospective

## Purpose

A potential supplier has been identified but no formal business relationship exists.

Typical sources include:

- market research
- referrals
- tenders
- supplier enquiries
- strategic sourcing

### Allowed Activities

- collect preliminary information
- perform initial screening
- assign procurement owner

### Exit Criteria

Move to **Registered** once sufficient supplier information has been collected.

---

# Stage 2 — Registered

## Purpose

Basic supplier information has been captured.

Supplier identity is now established within Swissbay.

### Required Information

- Supplier Name
- Registration Number
- Tax Number
- Contact Details
- Supplier Category
- Country
- Primary Contact

### Exit Criteria

Supplier proceeds to Qualification.

---

# Stage 3 — Qualification

## Purpose

Swissbay evaluates whether the supplier satisfies business requirements.

Qualification may include:

- financial review
- capability assessment
- technical evaluation
- compliance verification
- reference checks
- document verification

### AI Assistance

AI may:

- analyse submitted documents
- identify missing information
- recommend additional verification
- calculate preliminary risk

AI recommendations remain advisory.

### Exit Criteria

Supplier qualifies for Approval.

---

# Stage 4 — Approval

## Purpose

Formal governance approval occurs.

Authorised Procurement personnel determine whether the supplier may conduct business with Swissbay.

### Approval Requirements

- qualification complete
- required documentation received
- compliance verified
- procurement approval obtained

### AI Restrictions

Artificial Intelligence may not approve suppliers.

Approval always requires authorised human decision-makers.

### Exit Criteria

Supplier becomes Active.

---

# Stage 5 — Active

## Purpose

Supplier is authorised to conduct business.

This is the primary operational state.

### Typical Activities

- purchase orders
- contract management
- invoice processing
- performance monitoring
- relationship management

### Monitoring

Supplier performance is continuously monitored.

---

# Stage 6 — Performance Review

## Purpose

Supplier performance is formally evaluated.

Review criteria may include:

- delivery performance
- product quality
- responsiveness
- pricing competitiveness
- contract compliance
- customer feedback
- operational reliability

### Possible Outcomes

- continue active relationship
- preferred supplier designation
- improvement plan
- suspension

---

# Stage 7 — Suspended

## Purpose

Supplier is temporarily prevented from conducting new business.

Typical reasons include:

- poor performance
- compliance failure
- financial instability
- contractual disputes
- regulatory concerns

Existing obligations remain subject to contractual agreements.

---

# Stage 8 — Reactivated

## Purpose

Previously suspended supplier has resolved outstanding issues.

Requirements include:

- corrective actions completed
- compliance restored
- procurement approval
- governance review

Supplier returns to Active status.

---

# Stage 9 — Offboarded

## Purpose

Business relationship has formally ended.

Typical reasons include:

- contract expiry
- supplier closure
- strategic sourcing changes
- acquisition
- voluntary termination

### Activities

- final payment reconciliation
- contract closure
- document retention
- knowledge capture

---

# Stage 10 — Archived

## Purpose

Supplier information is retained for historical, audit and legal purposes.

Archived suppliers:

- cannot transact
- remain searchable
- preserve audit history
- support reporting

Retention periods follow legal and governance requirements.

---

# Lifecycle Transitions

| From | To | Approval Required |
|------|----|-------------------|
| Prospective | Registered | No |
| Registered | Qualification | No |
| Qualification | Approval | Procurement |
| Approval | Active | Procurement Manager |
| Active | Performance Review | No |
| Performance Review | Suspended | Procurement Manager |
| Suspended | Reactivated | Procurement Manager |
| Active | Offboarded | Procurement |
| Offboarded | Archived | System |

---

# AI Throughout the Lifecycle

Artificial Intelligence may assist by:

- identifying duplicate suppliers
- recommending qualification actions
- analysing documentation
- calculating supplier risk
- monitoring performance
- predicting supply chain issues
- generating executive summaries

AI may never:

- approve suppliers
- alter lifecycle stages
- bypass governance
- override procurement decisions

---

# Lifecycle KPIs

Key lifecycle measurements include:

- Registration Time
- Qualification Duration
- Approval Cycle Time
- Active Supplier Count
- Preferred Supplier Percentage
- Suspension Rate
- Reactivation Rate
- Offboarding Time
- Supplier Performance Score

These KPIs support continuous improvement.

---

# Lifecycle Events

The following events may trigger workflows or automations:

- Supplier Registered
- Qualification Started
- Qualification Completed
- Supplier Approved
- Supplier Activated
- Performance Review Due
- Supplier Suspended
- Supplier Reactivated
- Supplier Offboarded
- Supplier Archived

Each event may initiate notifications, approvals, dashboards or AI analysis.

---

# Governance

Every lifecycle transition requires:

- audit logging
- authorised ownership
- validation
- business rule compliance
- version history

Lifecycle integrity is protected through governance.

---

# Lifecycle Summary

The Supplier Lifecycle provides a governed framework for managing supplier relationships from initial identification through retirement.

By defining clear lifecycle stages, responsibilities, approvals and transition rules, Swissbay ensures that supplier information remains trusted, measurable and reusable across procurement, finance, operations, AI and automation.

The lifecycle serves as the operational backbone of supplier management within the Swissbay Nexus platform.