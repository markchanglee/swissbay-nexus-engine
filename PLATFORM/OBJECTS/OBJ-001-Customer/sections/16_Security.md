# 16 — Security

---

# Overview

The Customer Business Object contains commercially sensitive information that is fundamental to the operation of Swissbay.

Protecting Customer information is essential to maintaining customer trust, safeguarding intellectual property, supporting regulatory compliance and ensuring responsible business operations.

Security within Swissbay Nexus is not limited to preventing unauthorised access.

It also ensures that authorised users can only perform actions appropriate to their responsibilities.

Security therefore combines:

- Authentication
- Authorisation
- Auditability
- Accountability
- Confidentiality
- Integrity
- Availability

Every interaction with the Customer Business Object must be governed by these principles.

---

# Security Philosophy

Swissbay believes that information should be available to the people who need it while remaining protected from inappropriate access.

Security should enable business.

It should never unnecessarily restrict productivity.

Access should always follow the principle of:

> Least Privilege

Users receive only the permissions required to perform their responsibilities.

Nothing more.

---

# Security Principles

## Principle 1 — Least Privilege

Users receive only the minimum permissions required.

---

## Principle 2 — Role Based Access

Permissions are assigned to business roles rather than individuals.

---

## Principle 3 — Accountability

Every significant action must be traceable to a user, system or AI Agent.

---

## Principle 4 — Auditability

Every important change must create an audit record.

---

## Principle 5 — Human Authority

Artificial Intelligence assists business.

Humans remain accountable.

---

# Security Classification

Customer information should be classified according to business sensitivity.

| Classification | Description |
|----------------|-------------|
| Public | Safe for external publication |
| Internal | Available to all Swissbay employees |
| Confidential | Limited to authorised business users |
| Restricted | Highly sensitive commercial information |

Most Customer information should be classified as **Confidential**.

Financial information should normally be classified as **Restricted**.

---

# Role-Based Access Control (RBAC)

## CEO

### Permissions

- View all Customers
- View financial information
- View dashboards
- View AI insights
- Approve strategic changes

---

## Sales Director

### Permissions

- Create Customers
- Edit Customer information
- Assign Account Owners
- View Opportunities
- View Quotes
- View Customer dashboards

Cannot:

- Approve credit limits
- Change financial ownership

---

## Sales Representative

### Permissions

- Create Leads
- Request Customer creation
- Update relationship information
- Record meetings
- View assigned Customers

Cannot:

- Delete Customers
- Change payment terms
- Approve strategic accounts

---

## Finance

### Permissions

- View all Customers
- Edit payment terms
- Edit credit limits
- Maintain debtor information
- View invoices

Cannot:

- Delete Customer records

---

## Procurement

### Permissions

- View Customers
- View purchasing history
- View demand forecasts

Cannot:

- Edit commercial ownership
- Change financial information

---

## Operations

### Permissions

- View delivery information
- Update operational notes
- Maintain delivery addresses

Cannot:

- Modify financial information

---

## Customer Success

### Permissions

- View Customer Health
- Record satisfaction
- Manage complaints
- Recommend retention activities

Cannot:

- Approve commercial decisions

---

## AI Agents

AI operates with controlled permissions.

AI may:

- Read approved Customer information
- Analyse information
- Generate recommendations
- Produce summaries
- Prepare drafts

AI may never:

- Delete Customers
- Approve Customers
- Change payment terms
- Modify credit limits
- Archive Customers
- Create commercial commitments

---

# Permission Matrix

| Activity | Sales | Finance | Operations | Procurement | Customer Success | AI |
|----------|------|----------|------------|-------------|------------------|----|
| View Customer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Create Customer | ✓ | Review | ✗ | ✗ | ✗ | ✗ |
| Edit Customer | ✓ | Partial | Partial | View | Partial | ✗ |
| Delete Customer | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Change Payment Terms | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Change Credit Limit | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Archive Customer | Manager | Review | ✗ | ✗ | Review | ✗ |

---

# Authentication

Swissbay Nexus should support enterprise authentication including:

- Microsoft Entra ID
- Google Workspace
- Multi-Factor Authentication (MFA)
- Single Sign-On (SSO)

Every authenticated session should be linked to a unique user identity.

---

# Audit Logging

The following actions must generate audit entries:

- Customer creation
- Customer updates
- Payment term changes
- Credit limit changes
- Account Owner changes
- Customer archival
- Permission changes
- AI-generated recommendations accepted or rejected

Each audit entry should record:

- Timestamp
- User or AI Agent
- Action performed
- Previous value
- New value
- Reason (where applicable)

Audit records must be immutable.

---

# Data Protection

Customer information should be protected:

- In transit using encrypted connections (TLS)
- At rest using encrypted storage
- Through regular backups
- Through access controls
- Through monitoring and alerting

Sensitive data should never be exposed in logs or error messages.

---

# AI Security

AI Agents must operate within approved permissions.

AI interactions should:

- be logged
- reference governed data
- identify generated content
- avoid exposing restricted information
- respect user permissions

AI should never bypass security controls.

---

# Security Monitoring

Swissbay should monitor:

- Failed login attempts
- Unauthorised access attempts
- Privilege changes
- Unusual customer edits
- Bulk data exports
- AI activity
- Audit log anomalies

Alerts should be generated for suspicious behaviour.

---

# Compliance

Security controls should support compliance with:

- POPIA
- GDPR (where applicable)
- Customer confidentiality agreements
- Internal governance policies

Compliance requirements should evolve with applicable legislation.

---

# Future Security

Future versions may include:

- Attribute-Based Access Control (ABAC)
- Context-aware permissions
- Zero Trust Architecture
- Behavioural analytics
- AI-assisted threat detection
- Data Loss Prevention (DLP)
- Customer data masking
- Fine-grained API permissions

---

# Security Summary

Security ensures that Customer information remains protected, trustworthy and available to authorised users.

By combining role-based permissions, auditability, strong authentication and governed AI access, Swissbay Nexus establishes a secure operating environment that protects both the organisation and its customers.

Security is not simply a technical feature.

It is a core business capability that enables trusted collaboration, responsible Artificial Intelligence and sustainable business growth.