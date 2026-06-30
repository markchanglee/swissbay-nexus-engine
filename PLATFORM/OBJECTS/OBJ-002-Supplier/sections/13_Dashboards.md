# 13 — Dashboards

---

# Overview

The Supplier Business Object provides trusted information to a number of business dashboards throughout Swissbay Nexus.

Dashboards transform governed supplier information into actionable business intelligence for Procurement, Finance, Operations, Executive Management and Artificial Intelligence.

Dashboards consume Supplier information.

They never own or modify Supplier information.

The Supplier Business Object remains the authoritative source of supplier data.

---

# Purpose

Supplier dashboards exist to:

- monitor procurement performance
- improve supplier visibility
- reduce supplier risk
- support executive decision-making
- improve supplier relationships
- identify operational issues
- enable AI-assisted insights

Every dashboard should answer meaningful business questions.

---

# Dashboard Catalogue

| Dashboard ID | Dashboard Name | Primary Audience |
|--------------|----------------|------------------|
| DASH-SUP-001 | Supplier Overview Dashboard | Procurement |
| DASH-SUP-002 | Supplier Performance Dashboard | Procurement |
| DASH-SUP-003 | Supplier Risk Dashboard | Executive |
| DASH-SUP-004 | Supplier Compliance Dashboard | Procurement / Legal |
| DASH-SUP-005 | Procurement Executive Dashboard | Executive |
| DASH-SUP-006 | Spend Analysis Dashboard | Finance |
| DASH-SUP-007 | AI Procurement Insights | AI / Procurement |

---

# DASH-SUP-001 — Supplier Overview

## Purpose

Provides an operational overview of all suppliers.

### Business Questions

- How many suppliers do we have?
- How many are active?
- How many are pending approval?
- How many are preferred suppliers?
- Which suppliers require attention?

### KPIs

- Total Suppliers
- Active Suppliers
- Pending Approvals
- Preferred Suppliers
- Suspended Suppliers

### Primary Users

- Procurement
- Operations

---

# DASH-SUP-002 — Supplier Performance

## Purpose

Measures supplier effectiveness.

### Business Questions

- Which suppliers perform best?
- Which suppliers are declining?
- Which suppliers require intervention?

### KPIs

- Performance Score
- Delivery Score
- Quality Score
- Responsiveness
- Contract Compliance

### Visuals

- Supplier Ranking
- Trend Analysis
- Performance Heatmap
- Score Distribution

---

# DASH-SUP-003 — Supplier Risk

## Purpose

Monitor procurement risk.

### Business Questions

- Which suppliers are high risk?
- Which suppliers have expired compliance?
- Which suppliers require review?

### KPIs

- Risk Rating
- Compliance Expiry
- High Risk Suppliers
- Suspended Suppliers

### Audience

- Executive
- Procurement
- Risk Management

---

# DASH-SUP-004 — Supplier Compliance

## Purpose

Monitor supplier governance and compliance.

### Business Questions

- Which certifications expire soon?
- Which suppliers are non-compliant?
- Which audits are overdue?

### KPIs

- Compliance Rate
- Certification Status
- Audit Completion
- Outstanding Issues

---

# DASH-SUP-005 — Procurement Executive Dashboard

## Purpose

Provide executives with procurement visibility.

### Business Questions

- Are procurement objectives being achieved?
- Are strategic suppliers performing?
- Where are procurement risks increasing?

### KPIs

- Procurement Spend
- Strategic Supplier Count
- Preferred Supplier %
- Procurement Savings
- Supplier Performance Index

---

# DASH-SUP-006 — Spend Analysis

## Purpose

Analyse procurement expenditure.

### Business Questions

- Who receives the most spend?
- Which categories cost the most?
- How has spend changed over time?

### KPIs

- Total Spend
- Spend by Supplier
- Spend by Category
- Spend Trend

---

# DASH-SUP-007 — AI Procurement Insights

## Purpose

Provide AI-generated procurement intelligence.

### AI Capabilities

- Supplier summaries
- Supplier recommendations
- Procurement anomalies
- Risk forecasts
- Spend optimisation
- Supplier comparisons

### Outputs

- Executive Brief
- Procurement Actions
- AI Alerts
- Improvement Opportunities

---

# Dashboard Filters

Supplier dashboards should support filtering by:

- Supplier
- Supplier Category
- Supplier Status
- Country
- Region
- Procurement Manager
- Performance Rating
- Risk Rating
- Date Range

Filters should remain consistent across all supplier dashboards.

---

# Drill-Down Navigation

Dashboards should support drill-down.

```
Executive Dashboard

↓

Supplier Dashboard

↓

Supplier Record

↓

Contracts

↓

Purchase Orders

↓

Invoices
```

Users should always be able to navigate back to the governing Business Object.

---

# AI Integration

Artificial Intelligence enhances dashboards by:

- explaining trends
- identifying anomalies
- predicting future risks
- recommending actions
- generating executive summaries

AI recommendations remain advisory.

---

# Refresh Frequency

| Dashboard | Frequency |
|------------|-----------|
| Supplier Overview | Daily |
| Performance | Daily |
| Risk | Hourly |
| Compliance | Daily |
| Executive | Weekly |
| Spend Analysis | Daily |
| AI Insights | Near Real-Time |

Refresh frequency should align with operational requirements.

---

# Security

Dashboard visibility follows the Swissbay Security Standard.

Users only see supplier information that they are authorised to access.

Sensitive procurement information must never be exposed through dashboards.

---

# Dashboard Validation

Before approval verify that:

- dashboard purpose is defined
- KPIs are governed
- Business Questions are meaningful
- visuals support decisions
- drill-down exists
- AI explanations are available
- security is applied

---

# Dashboard Summary

The Supplier Dashboard Portfolio transforms governed supplier information into actionable procurement intelligence.

By combining operational metrics, executive reporting, AI insights and governed KPIs, Swissbay enables Procurement and Executive Management to make faster, more informed decisions while maintaining complete traceability back to the Supplier Business Object.

Dashboards are therefore a decision-support capability built upon trusted supplier information rather than independent reporting artefacts.