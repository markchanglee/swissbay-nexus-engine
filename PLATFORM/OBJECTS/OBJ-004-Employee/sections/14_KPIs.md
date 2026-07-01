# 14 — Key Performance Indicators (KPIs)

---

# Overview

The Employee Business Object provides the enterprise performance measurements used to evaluate workforce effectiveness throughout the employee lifecycle.

These KPIs support Human Resources, Executive Management, Information Technology, Information Security, Operations and Artificial Intelligence by providing consistent, governed measurements of organisational performance.

Every KPI defined within this document follows the Swissbay KPI Standard (KPI-000).

---

# Purpose

The Employee KPI Model exists to:

- measure workforce effectiveness
- improve employee retention
- improve organisational performance
- strengthen governance
- support workforce planning
- enable executive reporting
- improve compliance
- enable AI insights

KPIs measure organisational outcomes rather than administrative activity.

---

# KPI Catalogue

| KPI ID | KPI Name | Category |
|---------|----------|----------|
| KPI-EMP-001 | Active Employees | Workforce |
| KPI-EMP-002 | Employee Turnover Rate | Workforce |
| KPI-EMP-003 | Employee Retention Rate | Workforce |
| KPI-EMP-004 | Time to Hire | Recruitment |
| KPI-EMP-005 | Time to Onboard | HR Operations |
| KPI-EMP-006 | Training Completion Rate | Learning |
| KPI-EMP-007 | Workforce Utilisation | Operations |
| KPI-EMP-008 | Leave Utilisation | Workforce |
| KPI-EMP-009 | Workforce Forecast Accuracy | AI |
| KPI-EMP-010 | Security Compliance Rate | Security |

---

# KPI-EMP-001 — Active Employees

## Purpose

Measures the number of Employees currently active within the organisation.

### Formula

```
Count(Employee)

WHERE

Employment Status = Active
```

### Frequency

Daily

### Audience

- Human Resources
- Executive

---

# KPI-EMP-002 — Employee Turnover Rate

## Purpose

Measures the percentage of Employees leaving the organisation.

### Formula

```
Employees Leaving

÷

Average Employee Count

×

100
```

### Frequency

Monthly

### Target

Business Defined

Lower values generally indicate stronger workforce stability.

---

# KPI-EMP-003 — Employee Retention Rate

## Purpose

Measures the percentage of Employees retained during a reporting period.

### Formula

```
Employees Retained

÷

Average Employee Count

×

100
```

### Frequency

Monthly

### Target

≥ 90%

---

# KPI-EMP-004 — Time to Hire

## Purpose

Measures the average time taken to recruit and appoint a new Employee.

### Formula

```
Offer Acceptance Date

-

Vacancy Approval Date
```

### Frequency

Monthly

### Target

Business Defined

Lower values improve organisational responsiveness.

---

# KPI-EMP-005 — Time to Onboard

## Purpose

Measures the average time required for a new Employee to become operational.

### Formula

```
Employee Active Date

-

Offer Acceptance Date
```

### Frequency

Monthly

### Target

Business Defined

---

# KPI-EMP-006 — Training Completion Rate

## Purpose

Measures the percentage of mandatory training successfully completed.

### Formula

```
Completed Training

÷

Assigned Training

×

100
```

### Target

≥ 95%

Training compliance supports governance and operational readiness.

---

# KPI-EMP-007 — Workforce Utilisation

## Purpose

Measures how effectively workforce capacity is being used.

### Formula

```
Productive Hours

÷

Available Hours

×

100
```

### Frequency

Weekly

### Audience

- Operations
- Executive

---

# KPI-EMP-008 — Leave Utilisation

## Purpose

Measures employee leave usage to support workforce planning.

### Formula

```
Leave Days Taken

÷

Leave Days Available

×

100
```

### Frequency

Monthly

### Target

Business Defined

---

# KPI-EMP-009 — Workforce Forecast Accuracy

## Purpose

Measures the accuracy of AI-generated workforce forecasts.

### Formula

```
Forecast Workforce

vs

Actual Workforce
```

### Frequency

Quarterly

### Audience

- Executive
- Human Resources
- AI Governance

---

# KPI-EMP-010 — Security Compliance Rate

## Purpose

Measures workforce compliance with organisational security requirements.

### Inputs

- MFA Compliance
- Access Reviews
- Security Training
- Policy Acknowledgements
- Identity Governance

### Frequency

Monthly

### Target

≥ 98%

---

# KPI Ownership

| KPI | Owner |
|------|-------|
| Active Employees | Human Resources |
| Employee Turnover | Human Resources |
| Employee Retention | Human Resources |
| Time to Hire | Human Resources |
| Time to Onboard | Human Resources |
| Training Completion | Learning & Development |
| Workforce Utilisation | Operations |
| Leave Utilisation | Human Resources |
| Workforce Forecast Accuracy | AI Governance |
| Security Compliance | Information Security |

---

# KPI Hierarchy

```
Executive Workforce KPIs

↓

Human Resources KPIs

↓

Operational KPIs

↓

Employee KPIs

↓

Supporting Metrics
```

Lower-level metrics contribute directly to strategic workforce performance.

---

# Dashboard Integration

Employee KPIs are displayed within:

- Workforce Overview Dashboard
- Organisational Structure Dashboard
- Employee Performance Dashboard
- Workforce Capacity Dashboard
- Security & Access Dashboard
- Executive Workforce Dashboard
- AI Workforce Insights Dashboard

Dashboards consume KPI definitions without redefining calculations.

---

# AI Integration

Artificial Intelligence may:

- analyse KPI trends
- forecast KPI performance
- identify organisational risks
- explain KPI movement
- recommend workforce improvements
- benchmark workforce performance

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

- Human Resources Review
- Executive Review (where applicable)
- Governance Approval
- Version Update

KPI definitions remain stable and reusable across the platform.

---

# KPI Summary

The Employee KPI Portfolio provides the official performance measurements for workforce management within Swissbay Nexus.

By defining consistent, governed and measurable indicators, Swissbay enables Human Resources, Executive Management, Operations, Information Security and Artificial Intelligence to evaluate organisational health objectively, improve workforce planning, strengthen governance and support strategic decision-making.

Employee KPIs transform workforce information into measurable enterprise outcomes that drive organisational excellence.