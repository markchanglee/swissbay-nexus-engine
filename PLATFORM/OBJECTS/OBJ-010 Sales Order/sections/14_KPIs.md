# 14 — Key Performance Indicators (KPIs)

---

# Overview

The Sales Order Business Object provides the enterprise performance measurements used to evaluate commercial transactions throughout their lifecycle.

These KPIs support Sales, Sales Operations, Warehouse, Finance, Customer Service, Executive Management and Artificial Intelligence by providing consistent, governed measurements of commercial performance.

Every KPI defined within this document follows the Swissbay KPI Standard (KPI-000).

---

# Purpose

The Sales Order KPI Model exists to:

- measure commercial performance
- improve fulfilment
- improve customer satisfaction
- improve revenue visibility
- optimise operational efficiency
- support executive reporting
- enable AI insights
- drive continuous improvement

KPIs measure business outcomes rather than business activity.

---

# KPI Catalogue

| KPI ID | KPI Name | Category |
|---------|----------|----------|
| KPI-SO-001 | Orders Processed | Operational |
| KPI-SO-002 | Revenue Generated | Financial |
| KPI-SO-003 | Average Order Value | Financial |
| KPI-SO-004 | Order Cycle Time | Operational |
| KPI-SO-005 | Order Fulfilment Rate | Operational |
| KPI-SO-006 | On-Time Delivery Rate | Logistics |
| KPI-SO-007 | Order Cancellation Rate | Operational |
| KPI-SO-008 | Order Return Rate | Quality |
| KPI-SO-009 | Revenue Forecast Accuracy | AI |
| KPI-SO-010 | Customer Satisfaction Score | Customer Experience |

---

# KPI-SO-001 — Orders Processed

## Purpose

Measures the number of Sales Orders successfully processed during a reporting period.

### Formula

```
Count(Completed Sales Orders)
```

### Frequency

Daily

### Target

Business Defined

---

# KPI-SO-002 — Revenue Generated

## Purpose

Measures total revenue generated from Sales Orders.

### Formula

```
Sum(Grand Total)

WHERE

Sales Order Status = Completed
```

### Frequency

Daily

### Audience

- Finance
- Executive
- Sales

---

# KPI-SO-003 — Average Order Value

## Purpose

Measures the average commercial value of completed Sales Orders.

### Formula

```
Total Revenue

÷

Completed Sales Orders
```

### Frequency

Daily

### Target

Business Defined

---

# KPI-SO-004 — Order Cycle Time

## Purpose

Measures the time taken for a Sales Order to progress from creation to completion.

### Formula

```
Completion Date

-

Order Creation Date
```

### Target

Business Defined

Lower values indicate greater operational efficiency.

---

# KPI-SO-005 — Order Fulfilment Rate

## Purpose

Measures the percentage of Sales Orders successfully fulfilled.

### Formula

```
Completed Orders

÷

Approved Orders

×

100
```

### Target

≥ 98%

---

# KPI-SO-006 — On-Time Delivery Rate

## Purpose

Measures the percentage of Sales Orders delivered on or before the promised delivery date.

### Formula

```
Orders Delivered On Time

÷

Orders Delivered

×

100
```

### Target

≥ 95%

---

# KPI-SO-007 — Order Cancellation Rate

## Purpose

Measures the percentage of Sales Orders cancelled before completion.

### Formula

```
Cancelled Orders

÷

Total Sales Orders

×

100
```

### Target

Business Defined

Lower values generally indicate healthier commercial operations.

---

# KPI-SO-008 — Order Return Rate

## Purpose

Measures the percentage of completed Sales Orders that result in product returns.

### Formula

```
Returned Orders

÷

Completed Orders

×

100
```

### Target

Business Defined

This KPI supports quality improvement and customer satisfaction initiatives.

---

# KPI-SO-009 — Revenue Forecast Accuracy

## Purpose

Measures the accuracy of AI-generated revenue forecasts.

### Formula

```
Forecast Revenue

vs

Actual Revenue
```

### Frequency

Monthly

### Audience

- Executive
- Finance
- AI Governance

---

# KPI-SO-010 — Customer Satisfaction Score

## Purpose

Measures customer satisfaction following Sales Order completion.

### Inputs

- Customer Surveys
- Net Promoter Score (NPS)
- Customer Feedback
- Service Ratings

### Frequency

Monthly

### Target

Business Defined

---

# KPI Ownership

| KPI | Owner |
|------|-------|
| Orders Processed | Sales Operations |
| Revenue | Finance |
| Average Order Value | Finance |
| Order Cycle Time | Sales Operations |
| Fulfilment Rate | Warehouse |
| On-Time Delivery | Logistics |
| Cancellation Rate | Sales Operations |
| Return Rate | Customer Service |
| Revenue Forecast Accuracy | AI Governance |
| Customer Satisfaction | Customer Service |

---

# KPI Hierarchy

```
Executive Commercial KPIs

↓

Revenue KPIs

↓

Operational KPIs

↓

Sales Order KPIs

↓

Supporting Metrics
```

Lower-level metrics contribute directly to strategic business performance.

---

# Dashboard Integration

Sales Order KPIs are displayed within:

- Sales Order Overview Dashboard
- Order Fulfilment Dashboard
- Revenue Dashboard
- Customer Orders Dashboard
- Sales Performance Dashboard
- Executive Commercial Dashboard
- AI Sales Insights Dashboard

Dashboards consume KPI definitions without redefining calculations.

---

# AI Integration

Artificial Intelligence may:

- analyse KPI trends
- forecast KPI performance
- identify anomalies
- explain KPI movement
- recommend operational improvements
- benchmark commercial performance

AI recommendations reference governed KPI definitions.

---

# KPI Validation

Before approval verify:

- KPI purpose defined
- calculation documented
- ownership assigned
- reporting frequency defined
- thresholds documented
- data source governed

---

# KPI Governance

Changes to KPI definitions require:

- Sales Operations Review
- Finance Review (where applicable)
- Governance Approval
- Version Update

KPI definitions remain stable and reusable across the platform.

---

# KPI Summary

The Sales Order KPI Portfolio provides the official performance measurements for commercial transaction management within Swissbay Nexus.

By defining consistent, governed and measurable indicators, Swissbay enables Sales, Warehouse, Finance, Customer Service, Executive Management and Artificial Intelligence to evaluate operational performance objectively, improve fulfilment, optimise revenue generation and strengthen customer experience.

Sales Order KPIs transform commercial activity into measurable enterprise outcomes that drive operational excellence and strategic decision-making.