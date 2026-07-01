# 05 — Definitions

---

# Overview

This document defines the official business terminology used by the Employee Business Object.

These definitions establish a common enterprise language for workforce identity, organisational structure, accountability and employment across Human Resources, Operations, Finance, Information Technology, Security and Artificial Intelligence.

Every Employee within Swissbay Nexus should be interpreted consistently regardless of department, application or business process.

The definitions contained within this document are the authoritative terminology for workforce management across the Swissbay Nexus platform.

---

# Core Definitions

## Employee

An Employee is a governed representation of a person authorised to perform work on behalf of the organisation.

An Employee may be:

- Permanent Employee
- Temporary Employee
- Contractor
- Consultant
- Executive
- Intern

Every Employee is uniquely represented by one Employee Business Object.

---

## Employee Identifier

The permanent, globally unique identifier assigned to every Employee.

Example

```
EMP-000124
```

Employee Identifiers:

- never change
- are never reused
- uniquely identify an Employee

---

## Employee Number

A human-readable business reference used within the organisation.

Example

```
E10245
```

Employee Numbers remain unique within the organisation.

---

## Employment Status

The current employment state of the Employee.

Examples include:

- Active
- On Leave
- Suspended
- Seconded
- Retired
- Terminated

An Employee exists in one employment status at a time.

---

## Employment Type

Defines the contractual relationship between the Employee and the organisation.

Examples include:

- Permanent
- Fixed Term
- Temporary
- Contractor
- Consultant
- Intern

Employment Type does not determine permissions.

---

## Department

The organisational unit responsible for the Employee.

Examples include:

- Human Resources
- Finance
- Operations
- Sales
- Information Technology
- Legal

Departments support reporting and organisational governance.

---

## Business Unit

A higher-level organisational grouping containing one or more Departments.

Business Units support enterprise reporting and strategic planning.

---

## Position

The approved organisational position occupied by an Employee.

Examples include:

- Business Analyst
- Project Manager
- Finance Manager
- Warehouse Supervisor
- Chief Executive Officer

A Position exists independently of the Employee occupying it.

---

## Job Title

The official title assigned to an Employee.

Examples include:

- Data Engineer
- Procurement Officer
- Sales Consultant
- HR Administrator

Job Titles describe responsibilities but do not define permissions.

---

## Manager

The Employee responsible for supervising another Employee.

Managers support:

- approvals
- reporting
- coaching
- performance management
- organisational governance

Manager relationships define reporting structures.

---

## Direct Report

An Employee who reports directly to another Employee.

Direct Reports establish organisational hierarchy.

---

## Organisational Hierarchy

The governed reporting structure linking Employees throughout the organisation.

Example

```
CEO

↓

Executive

↓

Manager

↓

Supervisor

↓

Employee
```

The hierarchy supports governance, approvals and workforce reporting.

---

## Business Role

A governed business responsibility assigned to an Employee.

Examples include:

- Sales Representative
- Finance Approver
- Warehouse Operator
- Product Owner
- Project Manager

Business Roles determine responsibilities but not technical permissions.

---

## System Role

A technical access role assigned through the enterprise security model.

Examples include:

- System Administrator
- HR User
- Finance User
- Read Only User

System Roles are governed by SEC-000.

---

## Business Owner

The Employee accountable for a Business Object, policy, workflow or process.

Examples include ownership of:

- Customer
- Product
- Contract
- Project
- Dashboard
- KPI

Ownership establishes accountability rather than operational responsibility.

---

## Approval Authority

The authority granted to an Employee to approve governed business activities.

Examples include:

- Sales Approval
- Financial Approval
- Contract Approval
- Procurement Approval

Approval authority is governed separately from employment status.

---

## Skills

Professional capabilities held by an Employee.

Examples include:

- Project Management
- Data Engineering
- Procurement
- Python
- Azure
- Risk Management

Skills support workforce planning and AI recommendations.

---

## Certification

A recognised qualification or professional accreditation held by an Employee.

Examples include:

- PMP
- Microsoft Certified
- AWS Certified
- Chartered Accountant

Certifications support competency management.

---

## Artificial Intelligence

Artificial Intelligence refers to governed AI capabilities that analyse Employee information to improve workforce planning, organisational effectiveness and operational efficiency.

AI supports workforce decisions but never replaces human accountability.

---

# Approved Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| EMP | Employee |
| HR | Human Resources |
| IT | Information Technology |
| AI | Artificial Intelligence |
| KPI | Key Performance Indicator |
| ID | Identifier |
| API | Application Programming Interface |
| SSO | Single Sign-On |
| MFA | Multi-Factor Authentication |

Only approved abbreviations should be used throughout the Employee Business Object.

---

# Terminology Rules

The following terminology rules apply throughout the Employee Business Object.

- Use **Employee** rather than User where practical.
- Use **Employee Identifier** rather than Employee ID in formal documentation.
- Use **Manager** rather than Supervisor unless formally defined.
- Use **Business Role** rather than Position when referring to responsibilities.
- Use **Employment Status** when referring to workforce availability.

Consistent terminology improves governance, reporting and AI interpretation.

---

# AI Interpretation

Artificial Intelligence should interpret every Employee term according to this document.

AI should not infer alternative organisational meanings.

Where ambiguity exists, this document takes precedence.

---

# Definition Governance

All Employee definitions are governed enterprise assets.

Changes require:

- Human Resources Review
- Enterprise Architecture Review
- Governance Approval
- Version Update

Definitions evolve only through controlled governance.

---

# Definitions Summary

This document establishes the official enterprise vocabulary for the Employee Business Object.

By defining consistent terminology for workforce identity, organisational structure, reporting relationships, roles, approvals, skills and accountability, Swissbay Nexus ensures that employees, systems, workflows, integrations and Artificial Intelligence all operate from the same business understanding.

These definitions form the semantic foundation for workforce governance across the Swissbay Nexus platform.