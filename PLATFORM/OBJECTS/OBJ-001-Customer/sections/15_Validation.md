# 15 — Validation

---

# Overview

Validation ensures that every Customer record created or maintained within Swissbay Nexus meets the organisation's standards for quality, completeness and consistency.

The objective of validation is not simply to prevent incorrect information from being entered.

Its purpose is to ensure that every Customer record can be trusted by employees, dashboards, integrations, reports and Artificial Intelligence.

Every Customer must pass validation before becoming an Active Customer.

Validation continues throughout the Customer lifecycle.

---

# Validation Philosophy

Swissbay believes that trusted decisions require trusted data.

Poor-quality customer information leads to:

- incorrect quotations
- delayed deliveries
- failed invoicing
- duplicate work
- misleading reports
- unreliable AI recommendations

Validation protects the integrity of the Customer Business Object.

---

# Validation Principles

## Principle 1 — Validate Early

Validation should occur as information is entered.

Problems should be corrected immediately rather than discovered later.

---

## Principle 2 — Validate Automatically

Where possible, validation should be performed automatically.

Automation reduces human error and improves consistency.

---

## Principle 3 — Business Before Technical

Validation rules should protect business quality rather than simply checking technical formats.

---

## Principle 4 — Every Validation Must Explain Failure

Validation messages should clearly explain:

- what failed
- why it failed
- how it can be corrected

---

# Mandatory Validation

Every Customer must contain the following information before activation.

| Field | Required |
|---------|----------|
| Customer ID | Yes |
| Legal Name | Yes |
| Customer Type | Yes |
| Industry | Yes |
| Customer Status | Yes |
| Account Owner | Yes |
| Primary Contact | Yes |
| Payment Terms | Yes |
| Billing Address | Yes |

If any required field is missing, the Customer cannot become Active.

---

# Identity Validation

The following validations apply.

## Customer ID

Rules

- Must be unique.
- Must follow Swissbay ID standards.
- Cannot be edited manually.
- Cannot be reused.

Example

```
CUSTOMER-000458
```

---

## Legal Name

Rules

- Cannot be blank.
- Must contain a valid business name.
- Leading and trailing spaces removed automatically.

---

## Customer Type

Must match an approved Customer Type.

Examples

- Corporate
- Government
- Municipality
- Hospital
- School
- University
- Mining Company
- Distributor
- Retail

---

# Duplicate Detection

Swissbay should automatically check for possible duplicate Customers.

Matching criteria may include:

- Legal Name
- Registration Number
- VAT Number
- Email Domain
- Website
- Primary Contact
- Telephone Number

Potential duplicates should be reviewed before Customer creation.

---

# Contact Validation

The Primary Contact should include:

- Full Name
- Email Address
- Telephone Number
- Position

Email addresses should follow valid email formatting.

Telephone numbers should comply with regional standards.

---

# Commercial Validation

Before activation:

Payment Terms must be approved.

Credit Limits must be approved where applicable.

Customer Segment must exist.

Preferred Currency must be valid.

---

# Financial Validation

Finance validates:

- Payment Terms
- Credit Limit
- Tax Information
- VAT Number
- Financial Risk

Sales cannot approve financial fields.

---

# Operational Validation

Operations validates:

- Delivery Address
- Site Requirements
- Receiving Instructions
- Delivery Constraints

Operational validation reduces fulfilment risk.

---

# Lifecycle Validation

Customer lifecycle transitions require validation.

Examples

Lead

↓

Qualified Lead

Validation Required

- Qualification Complete

---

Qualified Lead

↓

Customer

Validation Required

- Management Approval (if applicable)
- Customer Information Complete

---

Customer

↓

Archived Customer

Validation Required

- No Active Orders
- No Open Quotes
- No Outstanding Deliveries

---

# AI Validation

Artificial Intelligence should assist validation by:

- detecting duplicates
- identifying incomplete records
- checking inconsistent information
- highlighting unusual behaviour
- recommending corrections

AI recommendations remain advisory.

---

# Validation Severity

Swissbay defines four validation levels.

## Information

Minor improvement suggested.

Example

Website missing.

---

## Warning

Customer can be saved but requires attention.

Example

No secondary contact.

---

## Error

Customer cannot be activated.

Example

Missing Legal Name.

---

## Critical

Major governance issue.

Example

Duplicate Customer ID.

Immediate correction required.

---

# Validation Matrix

| Validation | Severity | Owner |
|------------|----------|-------|
| Missing Legal Name | Error | Sales |
| Duplicate Customer ID | Critical | System |
| Missing Payment Terms | Error | Finance |
| Invalid Email | Warning | Sales |
| Missing Delivery Address | Warning | Operations |
| Duplicate Customer | Critical | Sales |
| Invalid VAT Number | Error | Finance |
| Missing Primary Contact | Error | Sales |

---

# Validation Reporting

Swissbay should monitor:

- Validation Failure Rate
- Duplicate Rate
- Incomplete Customer Records
- Average Time to Correct Errors
- Validation Trends
- AI Validation Accuracy

These metrics help improve data quality over time.

---

# Validation Governance

Validation rules may only be modified through the Nexus Governance process.

Changes must be:

- documented
- approved
- version controlled
- communicated

All validation logic should remain consistent across systems.

---

# Future Validation

Future releases may include:

- real-time company registration verification
- VAT validation through government services
- address verification
- fraud detection
- AI-powered data quality scoring
- duplicate probability scoring
- sanctions and compliance screening

---

# Validation Summary

Validation ensures that every Customer record entering Swissbay Nexus is accurate, complete and trustworthy.

By enforcing consistent validation standards, Swissbay protects the integrity of its business information, improves operational efficiency and enables Artificial Intelligence to operate on reliable data.

Validation is therefore a core governance capability and an essential component of the Customer Business Object.