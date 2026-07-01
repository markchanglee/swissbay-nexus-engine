# 04 — Scope

---

# Overview

The Employee Business Object defines the business boundaries for representing every authorised worker within the Swissbay Nexus platform.

It establishes clear ownership of employee identity, organisational structure and workforce information while preventing duplication of data owned by other Business Objects.

This document defines:

- what the Employee Business Object owns
- what it references
- what is intentionally excluded
- where responsibility begins and ends

Well-defined boundaries ensure Employees remain the authoritative workforce identity across the enterprise.

---

# Scope Statement

The Employee Business Object owns the identity and organisational representation of every authorised worker.

It governs:

- employee identity
- employment information
- organisational hierarchy
- reporting relationships
- business roles
- workforce status

The Employee Business Object references Projects, Sales Orders, Contracts, Assets and other Business Objects but never owns them.

---

# In Scope

The Employee Business Object is responsible for:

## Employee Identity

The Employee Business Object owns:

- Employee Identifier
- Employee Number
- First Name
- Last Name
- Preferred Name
- Employment Status
- Date Joined
- Employment Type

Employee identity is permanent throughout the employment lifecycle.

---

## Organisational Information

The Employee Business Object owns:

- Department
- Division
- Business Unit
- Cost Centre
- Job Title
- Position
- Manager
- Reporting Line

These define the employee's place within the organisation.

---

## Workforce Status

The Employee Business Object manages:

- Active
- On Leave
- Suspended
- Seconded
- Retired
- Terminated

Status reflects employment availability rather than system access.

---

## Contact Information

The Employee Business Object owns:

- Corporate Email
- Business Telephone
- Mobile Number
- Office Location
- Work Address

Personal contact information should only be stored where required by business policy.

---

## Organisational Relationships

The Employee Business Object maintains relationships including:

- Manager
- Direct Reports
- Department Membership
- Team Membership
- Executive Structure

These relationships support reporting and governance.

---

## Skills & Competencies

The Employee Business Object may own:

- Skills
- Certifications
- Professional Registrations
- Languages
- Areas of Expertise
- Training Completion

These support workforce planning and AI recommendations.

---

## Accountability

Employees may be responsible for:

- Business Object Ownership
- Workflow Approval
- Task Assignment
- Policy Ownership
- Audit Responsibility
- KPI Ownership

The Employee Business Object records accountability but does not own the referenced Business Objects.

---

# Out of Scope

The Employee Business Object does not own:

## Customers

Customer ownership belongs to:

OBJ-001 Customer

---

## Suppliers

Supplier ownership belongs to:

OBJ-002 Supplier

---

## Products

Product ownership belongs to:

OBJ-003 Product

---

## Contracts

Contract ownership belongs to:

OBJ-005 Contract

Employees may negotiate or approve Contracts but do not own Contract information.

---

## Projects

Project ownership belongs to:

OBJ-006 Project

Employees participate in Projects but Project information belongs to the Project Business Object.

---

## Assets

Asset ownership belongs to:

OBJ-007 Asset

Employees may be assigned Assets but Asset lifecycle management remains independent.

---

## Warehouses

Warehouse ownership belongs to:

OBJ-008 Warehouse

Employees work within Warehouses but do not own Warehouse information.

---

## Opportunities

Opportunity ownership belongs to:

OBJ-009 Opportunity

Employees create and manage Opportunities without owning Opportunity data.

---

## Sales Orders

Sales Order ownership belongs to:

OBJ-010 Sales Order

Employees create, approve and fulfil Sales Orders but the transaction belongs to the Sales Order Business Object.

---

## Authentication

Authentication belongs to enterprise Identity Providers.

Examples include:

- Microsoft Entra ID
- Active Directory
- Single Sign-On

The Employee Business Object references digital identities but does not authenticate users.

---

## Security Policies

Security Policies belong to:

SEC-000 Security Standard

Employees receive permissions but do not own security policies.

---

# Referenced Business Objects

The Employee Business Object references:

- Customer
- Supplier
- Product
- Contract
- Project
- Asset
- Warehouse
- Opportunity
- Sales Order

Relationships are maintained using permanent Business Object identifiers.

---

# Business Boundaries

The Employee Business Object begins when:

- a person joins the organisation
- a contractor is engaged
- an authorised worker requires enterprise identity

The Employee Business Object ends when:

- retention obligations expire
- historical employment records are archived according to policy

Employee history remains available for governance and audit purposes.

---

# Responsibilities

The Employee Business Object is responsible for:

- workforce identity
- organisational hierarchy
- reporting relationships
- employment status
- business accountability
- organisational reporting

It is not responsible for transactional business information.

---

# AI Scope

Artificial Intelligence may:

- recommend task assignments
- identify skills gaps
- forecast workforce demand
- analyse organisational structures
- recommend training
- support succession planning

Artificial Intelligence may not:

- hire employees
- terminate employees
- change reporting structures
- grant security permissions
- modify employment records without approval

Human accountability remains mandatory.

---

# Security Scope

Security responsibilities include:

- workforce identity protection
- organisational confidentiality
- role-based visibility
- audit logging
- access governance

Security implementation follows SEC-000.

---

# Integration Scope

The Employee Business Object may integrate with:

- Human Resources Systems
- ERP Platforms
- Identity Providers
- Payroll Systems
- Workflow Engine
- Microsoft Fabric
- Databricks
- AI Services
- Enterprise APIs

The Employee Business Object remains the canonical workforce identity regardless of implementation technology.

---

# Future Scope

Future enhancements may include:

- digital workforce profiles
- enterprise skills graph
- workforce capacity modelling
- AI competency recommendations
- organisational digital twins
- workforce collaboration analytics

These capabilities extend rather than redefine the Employee Business Object.

---

# Scope Validation

Before approval verify that:

- ownership is clearly defined
- business boundaries are understood
- identity ownership is separated from transactional ownership
- related Business Objects are referenced
- organisational accountability is defined
- AI boundaries are governed

---

# Scope Summary

The Employee Business Object owns the complete organisational identity of every authorised worker within Swissbay Nexus.

It intentionally excludes Customers, Products, Contracts, Projects, Assets, Warehouses, Opportunities and Sales Orders while maintaining governed relationships with those Business Objects.

This separation ensures Employees remain the trusted identity and accountability layer supporting governance, security, workflows, approvals and enterprise operations across the Swissbay Nexus platform.