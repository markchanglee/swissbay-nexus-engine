# 16 — Security

---

# Overview

The Security Model defines how the Project Business Object is protected throughout its lifecycle within the Swissbay Nexus platform.

Projects often contain commercially sensitive information including financial forecasts, customer commitments, intellectual property, strategic initiatives and organisational planning. Protecting this information is essential to maintaining confidentiality, integrity and availability.

Security follows the Swissbay Security Standard (SEC-000).

---

# Purpose

The Project Security Model exists to:

- protect project information
- enforce role-based access
- secure commercial data
- strengthen governance
- maintain auditability
- support Artificial Intelligence
- reduce enterprise risk
- protect strategic initiatives

Security enables trusted project execution.

---

# Security Principles

Project security follows these principles:

- least privilege
- need-to-know
- zero trust
- defence in depth
- segregation of duties
- privacy by design
- audit by default
- continuous monitoring

Security applies throughout the entire Project lifecycle.

---

# Data Classification

The Project Business Object is classified as:

| Classification Area | Value |
|--------------------|-------|
| Business Criticality | Critical |
| Confidentiality | Internal / Confidential |
| Integrity | High |
| Availability | High |

Individual projects may have higher classifications based on organisational policy.

---

# Protected Information

Protected information includes:

- Project Identifier
- Business Case
- Financial Information
- Budgets
- Forecasts
- Contracts
- Customer Information
- Resource Assignments
- Risk Register
- Issue Register
- Change Requests
- Deliverables
- Executive Decisions

Access to protected information must be governed.

---

# Access Control

Project information is accessible only to authorised users.

Access is granted according to:

- business role
- project assignment
- department
- governance authority
- security classification

Users should only access projects relevant to their responsibilities.

---

# Role-Based Access Control

| Role | Read | Create | Update | Approve | Archive |
|------|:----:|:------:|:------:|:-------:|:------:|
| Executive | ✓ | | ✓ | ✓ | |
| PMO | ✓ | ✓ | ✓ | ✓ | ✓ |
| Project Manager | ✓ | ✓ | ✓ | Limited | |
| Team Member | Limited | | Limited | | |
| Finance | Limited | | ✓ | Budget Only | |
| Procurement | Limited | | Limited | | |
| Legal | Limited | | Limited | Contract Only | |
| AI Agent | Governed Read | | | ✗ | ✗ |
| System Administrator | Technical Only | | | | |

Permissions should be reviewed regularly.

---

# Segregation of Duties

Critical responsibilities should remain separated.

Examples include:

| Activity | Responsible Role |
|----------|------------------|
| Business Case Approval | Executive Sponsor |
| Budget Approval | Finance |
| Project Delivery | Project Manager |
| Security Review | Information Security |
| Financial Audit | Internal Audit |
| Project Closure Approval | PMO / Executive |

No individual should control the complete project lifecycle without oversight.

---

# Authentication

Project access requires authentication through approved enterprise identity providers.

Supported methods include:

- Microsoft Entra ID
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- Conditional Access Policies

Anonymous access is prohibited.

---

# Authorisation

Every action must be authorised before project information is viewed or modified.

Authorisation considers:

- user role
- project assignment
- project status
- governance authority
- security classification

---

# Privacy

Projects may contain personal or commercially sensitive information.

Privacy controls ensure:

- only required information is collected
- sensitive information is protected
- access is restricted
- retention policies are followed
- AI uses only approved datasets

---

# Attribute-Level Security

Certain attributes require enhanced protection.

Examples include:

- approved budgets
- executive comments
- legal reviews
- commercial pricing
- contract references
- security assessments
- customer confidential information

Attribute-level access should be configurable.

---

# Encryption

Project information must be encrypted.

## Data at Rest

- database encryption
- storage encryption
- backup encryption

## Data in Transit

- HTTPS
- TLS 1.2+
- secure APIs

---

# Audit Logging

Every significant Project action should record:

- Project Identifier
- User
- Timestamp
- Action
- Previous Value
- New Value
- Business Reason

Audit records must be immutable.

---

# Security Events

Examples include:

- Project Created
- Budget Updated
- Project Approved
- Stage Gate Passed
- Project Closed
- Security Role Changed
- Project Archived
- Access Revoked

Security events support monitoring and governance.

---

# AI Security

Artificial Intelligence must:

- inherit user permissions
- respect project classification
- provide explainable recommendations
- maintain audit history
- consume governed data only

AI may not:

- approve projects
- approve budgets
- approve stage gates
- modify governance decisions
- bypass Business Rules

Human accountability remains mandatory.

---

# API Security

Project APIs must implement:

- authentication
- authorisation
- validation
- encryption
- rate limiting
- audit logging

Project Identifiers remain governed by Swissbay.

---

# Integration Security

Project integrations may connect with:

- ERP systems
- PMO platforms
- Microsoft Project
- Azure DevOps
- Jira
- Microsoft Fabric
- Databricks
- Power BI

Each integration must define:

- owner
- access scope
- update authority
- audit requirements
- failure handling

---

# Monitoring

Swissbay should monitor:

- failed access attempts
- privilege changes
- unusual activity
- project data exports
- AI access
- integration failures
- dormant projects

Monitoring supports proactive governance.

---

# Security Validation

Before deployment verify:

- access controls configured
- sensitive fields protected
- MFA enabled where required
- audit logging active
- encryption enabled
- API security tested
- AI permissions validated

---

# Security Governance

Security changes require:

- PMO Review
- Information Security Review
- Enterprise Architecture Review
- Governance Approval
- Version Update

Security remains a governed enterprise capability.

---

# Security Summary

The Project Security Model protects the execution layer of Swissbay Nexus.

By combining role-based access control, encryption, audit logging, privacy controls, AI governance and integration security, Swissbay ensures that Projects remain secure, trustworthy and compliant throughout their lifecycle while supporting enterprise delivery and strategic execution.