# 04 — Scope

---

# Overview

The Project Business Object defines the boundaries of project governance within the Swissbay Nexus platform.

Its purpose is to clearly identify what information, responsibilities and lifecycle activities belong to the Project Business Object and which responsibilities belong to other Business Objects.

Clearly defined scope prevents duplication, simplifies integrations and ensures consistent governance across the enterprise.

---

# Purpose

The Scope Model exists to:

- define Project responsibilities
- establish governance boundaries
- eliminate duplicated information
- simplify integrations
- improve maintainability
- support enterprise architecture
- enable Artificial Intelligence

The Project Business Object governs projects—not every activity performed within a project.

---

# In Scope

The Project Business Object governs:

- Project Identity
- Project Ownership
- Business Objectives
- Project Scope
- Project Status
- Project Lifecycle
- Project Budget
- Project Schedule
- Milestones
- Deliverables
- Dependencies
- Risks
- Issues
- Change Requests
- Resource Assignments
- Governance Decisions
- Project Closure
- Lessons Learned

These capabilities form the canonical representation of a Project.

---

# Project Information

The Project Business Object owns:

- Project ID
- Project Name
- Description
- Business Justification
- Sponsor
- Project Manager
- Business Owner
- Start Date
- Planned Finish Date
- Actual Finish Date
- Current Status
- Priority
- Methodology

---

# Project Governance

Projects maintain:

- Steering Committee
- Stage Gates
- Approval History
- Governance Decisions
- Executive Reporting
- Audit Trail

Governance remains part of the Project Business Object.

---

# Financial Scope

Projects govern:

- Approved Budget
- Forecast Budget
- Actual Cost
- Cost Variance
- Financial Approvals

Detailed accounting remains the responsibility of Finance systems.

---

# Resource Scope

Projects maintain references to:

- Employees
- Contractors
- Suppliers
- Equipment
- Assets

Resource identity remains owned by the corresponding Business Objects.

---

# Risk & Issue Scope

Projects govern:

- Risks
- Issues
- Assumptions
- Dependencies
- Mitigation Plans
- Escalations

Collectively these may be managed through a RAID register.

---

# Deliverable Scope

Projects govern:

- Deliverables
- Milestones
- Acceptance Criteria
- Completion Status

Deliverables remain linked to the project throughout its lifecycle.

---

# Portfolio Scope

Projects may belong to:

- Programmes
- Portfolios
- Strategic Initiatives

Portfolio governance remains outside the individual Project Business Object.

---

# Out of Scope

The Project Business Object does not own:

- Customer master data
- Employee master data
- Supplier master data
- Product master data
- Asset master data
- Warehouse operations
- Sales Orders
- Financial Ledger
- Payroll

Instead, it references these Business Objects through governed relationships.

---

# Relationship Boundaries

| Business Object | Relationship |
|-----------------|--------------|
| Customer | Project Customer |
| Contract | Governs the Project |
| Employee | Project Resources |
| Product | Project Deliverables |
| Asset | Project Assets |
| Opportunity | Project Origin |
| Sales Order | Project Fulfilment |

Projects coordinate work across these Business Objects without replacing them.

---

# AI Scope

Artificial Intelligence may:

- analyse project health
- predict delays
- recommend resources
- forecast completion
- identify risks
- summarise project status

AI may not:

- approve projects
- change budgets
- modify governance decisions
- bypass Business Rules

---

# Scope Summary

The Project Business Object governs the planning, execution, monitoring and completion of enterprise projects while coordinating related Business Objects through governed relationships.

Its scope is intentionally limited to project governance, ensuring a clear separation of responsibilities and a maintainable enterprise architecture.