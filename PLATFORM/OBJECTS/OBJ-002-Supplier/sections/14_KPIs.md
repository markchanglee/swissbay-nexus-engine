# 14 — Key Performance Indicators (KPIs)

---

# Overview

The Supplier Business Object provides the performance measures used to evaluate supplier effectiveness, procurement efficiency and supplier governance across Swissbay Nexus.

These KPIs provide objective measurements that support operational management, executive oversight and Artificial Intelligence.

Every KPI defined in this document follows the Swissbay KPI Standard (KPI-000).

---

# Purpose

The Supplier KPI Model exists to:

- measure supplier performance
- improve procurement governance
- support executive reporting
- identify operational issues
- monitor supplier risk
- enable AI insights
- drive continuous improvement

KPIs measure business outcomes rather than business activity.

---

# KPI Catalogue

| KPI ID | KPI Name | Category |
|---------|----------|----------|
| KPI-SUP-001 | Active Supplier Count | Operational |
| KPI-SUP-002 | Supplier Performance Score | Performance |
| KPI-SUP-003 | On-Time Delivery Rate | Operational |
| KPI-SUP-004 | Supplier Quality Score | Quality |
| KPI-SUP-005 | Supplier Risk Rating | Risk |
| KPI-SUP-006 | Supplier Compliance Rate | Compliance |
| KPI-SUP-007 | Supplier Approval Cycle Time | Operational |
| KPI-SUP-008 | Preferred Supplier Percentage | Strategic |
| KPI-SUP-009 | Procurement Spend by Supplier | Financial |
| KPI-SUP-010 | Supplier Satisfaction Index | Relationship |

---

# KPI-SUP-001 — Active Supplier Count

## Purpose

Measures the number of suppliers currently authorised to conduct business.

### Formula

```
Count(Suppliers)

WHERE

Status = Active
```

### Target

Business Defined

### Frequency

Daily

---

# KPI-SUP-002 — Supplier Performance Score

## Purpose

Measures the overall effectiveness of each supplier.

### Components

- Delivery
- Quality
- Responsiveness
- Compliance
- Commercial Performance

### Formula

Weighted Procurement Score

### Frequency

Monthly

---

# KPI-SUP-003 — On-Time Delivery Rate

## Purpose

Measures supplier delivery reliability.

### Formula

```
On-Time Deliveries

÷

Total Deliveries

×

100
```

### Target

≥95%

---

# KPI-SUP-004 — Supplier Quality Score

## Purpose

Measures the quality of supplied products or services.

### Inputs

- Defect Rate
- Returns
- Customer Complaints
- Inspection Results

### Frequency

Monthly

---

# KPI-SUP-005 — Supplier Risk Rating

## Purpose

Measures overall supplier risk.

### Components

- Financial Risk
- Operational Risk
- Compliance Risk
- Geopolitical Risk
- ESG Risk

### Scale

Low

↓

Medium

↓

High

↓

Critical

---

# KPI-SUP-006 — Supplier Compliance Rate

## Purpose

Measures supplier compliance with organisational and regulatory requirements.

### Formula

```
Compliant Suppliers

÷

Total Active Suppliers

×

100
```

### Target

100%

---

# KPI-SUP-007 — Supplier Approval Cycle Time

## Purpose

Measures the efficiency of supplier onboarding.

### Formula

```
Approval Date

-

Registration Date
```

### Target

Business Defined

---

# KPI-SUP-008 — Preferred Supplier Percentage

## Purpose

Measures supplier maturity.

### Formula

```
Preferred Suppliers

÷

Active Suppliers

×

100
```

---

# KPI-SUP-009 — Procurement Spend by Supplier

## Purpose

Measures expenditure across suppliers.

### Used By

- Finance
- Procurement
- Executive

Supports supplier concentration analysis.

---

# KPI-SUP-010 — Supplier Satisfaction Index

## Purpose

Measures the quality of supplier relationships.

### Inputs

- Procurement Surveys
- Issue Resolution
- Communication
- Collaboration

Relationship quality contributes to long-term procurement success.

---

# KPI Ownership

| KPI | Owner |
|------|-------|
| Performance | Procurement |
| Compliance | Procurement & Legal |
| Spend | Finance |
| Risk | Procurement |
| Satisfaction | Procurement |

---

# KPI Hierarchy

```
Executive Procurement KPIs

↓

Department KPIs

↓

Supplier KPIs

↓

Operational Metrics
```

Lower-level operational metrics contribute to strategic procurement objectives.

---

# Dashboard Integration

Supplier KPIs are displayed within:

- Supplier Overview Dashboard
- Supplier Performance Dashboard
- Supplier Risk Dashboard
- Executive Procurement Dashboard
- Spend Analysis Dashboard

Dashboards consume KPI definitions without redefining calculations.

---

# AI Integration

Artificial Intelligence may:

- analyse KPI trends
- identify anomalies
- explain KPI movements
- predict future KPI performance
- recommend corrective actions
- benchmark suppliers

AI recommendations reference governed KPI definitions.

---

# KPI Validation

Before approval verify that:

- KPI purpose is defined
- calculation is documented
- ownership is assigned
- data sources are governed
- reporting frequency is defined
- thresholds are documented

---

# KPI Governance

Changes to KPI definitions require:

- Procurement Review
- Business Approval
- Governance Approval
- Version Update

KPI calculations should remain stable and consistent over time.

---

# KPI Summary

The Supplier KPI Portfolio provides the official performance measurements for supplier management within Swissbay Nexus.

By defining consistent, governed and measurable indicators, Swissbay enables Procurement, Finance, Executive Management and Artificial Intelligence to monitor supplier performance objectively, identify improvement opportunities and support strategic decision-making.

Supplier KPIs transform procurement activities into measurable business outcomes that drive operational excellence and continuous improvement.