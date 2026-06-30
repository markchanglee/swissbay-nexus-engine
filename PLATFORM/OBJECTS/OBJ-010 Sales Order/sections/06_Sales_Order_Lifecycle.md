# 06 — Sales Order Lifecycle

---

# Overview

The Sales Order Lifecycle defines the complete operational journey of a Sales Order within the Swissbay Nexus platform.

Beginning with the creation of a customer order and ending with completion, cancellation or archival, the lifecycle ensures that every commercial transaction progresses through governed stages with full visibility, auditability and accountability.

Each Sales Order exists in one—and only one—lifecycle stage at any given time.

---

# Purpose

The Sales Order Lifecycle exists to:

- standardise commercial processing
- improve fulfilment efficiency
- improve customer experience
- support warehouse operations
- support financial processing
- enable automation
- enable Artificial Intelligence
- maintain complete transaction traceability

The lifecycle provides a consistent operational framework across every sales channel.

---

# Lifecycle Overview

Every Sales Order progresses through the following stages.

```text
Draft

↓

Submitted

↓

Validated

↓

Approved

↓

Allocated

↓

Picking

↓

Packing

↓

Shipped

↓

Delivered

↓

Invoiced

↓

Completed

↓

Archived
```

Alternative paths

```text
Draft

↓

Cancelled
```

or

```text
Delivered

↓

Returned

↓

Closed
```

Each transition is governed by Business Rules and approval requirements.

---

# Stage 1 — Draft

## Purpose

A Sales Order has been created but has not yet entered the commercial workflow.

### Activities

- capture customer
- add products
- calculate pricing
- calculate taxes
- select delivery method

### Exit Criteria

Order submitted for validation.

---

# Stage 2 — Submitted

## Purpose

The customer or sales representative submits the Sales Order.

### Activities

- lock commercial values
- assign order number
- begin validation
- notify workflow engine

### Exit Criteria

Validation successful.

---

# Stage 3 — Validated

## Purpose

The Sales Order satisfies business validation requirements.

### Validation Includes

- Customer exists
- Products exist
- Pricing valid
- Inventory available
- Required approvals identified

### AI Assistance

AI may:

- identify unusual pricing
- detect duplicate orders
- identify fulfilment risks
- estimate delivery dates

### Exit Criteria

Ready for approval.

---

# Stage 4 — Approved

## Purpose

Required commercial approvals have been completed.

### Approval Examples

- pricing approval
- discount approval
- credit approval
- contract approval

### Exit Criteria

Inventory allocation begins.

---

# Stage 5 — Allocated

## Purpose

Inventory has been reserved for the Sales Order.

### Activities

- reserve stock
- assign warehouse
- schedule fulfilment
- prepare picking tasks

Inventory ownership remains with the Warehouse Business Object.

---

# Stage 6 — Picking

## Purpose

Warehouse personnel collect Products required for the Sales Order.

### Activities

- generate pick list
- scan products
- verify quantities
- record picking completion

### Exit Criteria

Order packed.

---

# Stage 7 — Packing

## Purpose

Products are prepared for shipment.

### Activities

- packaging
- labelling
- shipment preparation
- weight verification
- documentation

### Exit Criteria

Shipment created.

---

# Stage 8 — Shipped

## Purpose

Products have left the warehouse.

### Activities

- carrier assigned
- tracking number generated
- shipment confirmed
- customer notified

### Outputs

Shipment tracking information becomes available.

---

# Stage 9 — Delivered

## Purpose

Products have been delivered to the customer.

### Activities

- delivery confirmation
- proof of delivery
- customer acknowledgement
- delivery timestamp

### Exit Criteria

Invoice generated or confirmed.

---

# Stage 10 — Invoiced

## Purpose

A commercial invoice has been generated.

### Activities

- create invoice
- send invoice
- notify finance
- update receivables

Invoice ownership belongs to the Finance domain.

---

# Stage 11 — Completed

## Purpose

The commercial transaction has concluded successfully.

### Activities

- close fulfilment
- final audit
- update reporting
- release workflow resources

The Sales Order becomes read-only except through governed correction processes.

---

# Stage 12 — Archived

## Purpose

Completed Sales Orders are retained for historical reference.

Archived Sales Orders:

- remain searchable
- support reporting
- support auditing
- cannot be modified

Retention follows organisational policy.

---

# Exception Path — Cancelled

## Purpose

The Sales Order has been cancelled before successful completion.

### Typical Reasons

- customer cancellation
- payment failure
- inventory unavailable
- pricing issue
- duplicate order

Cancelled orders remain permanently recorded.

---

# Exception Path — Returned

## Purpose

Products have been returned after delivery.

### Activities

- return authorisation
- warehouse inspection
- refund processing
- replacement order (where applicable)

Returns reference the original Sales Order.

---

# Lifecycle Transitions

| From | To | Approval Required |
|------|----|-------------------|
| Draft | Submitted | No |
| Submitted | Validated | System |
| Validated | Approved | Sales / Finance |
| Approved | Allocated | System |
| Allocated | Picking | Warehouse |
| Picking | Packing | Warehouse |
| Packing | Shipped | Warehouse |
| Shipped | Delivered | Logistics |
| Delivered | Invoiced | Finance |
| Invoiced | Completed | System |
| Completed | Archived | System |
| Any Eligible Stage | Cancelled | Authorised User |
| Delivered | Returned | Customer Service |

---

# Lifecycle Events

Major lifecycle events include:

- Order Created
- Order Submitted
- Order Validated
- Order Approved
- Inventory Allocated
- Picking Started
- Packing Completed
- Shipment Created
- Delivered
- Invoice Generated
- Order Completed
- Order Cancelled
- Order Returned
- Order Archived

These events initiate workflows, notifications, dashboards and automation.

---

# AI Throughout the Lifecycle

Artificial Intelligence may:

- estimate fulfilment time
- predict delivery delays
- recommend warehouse selection
- identify fraud indicators
- forecast revenue
- identify high-risk orders
- recommend substitute products

AI remains advisory throughout every lifecycle stage.

---

# Lifecycle KPIs

Key measurements include:

- Order Cycle Time
- Approval Time
- Fulfilment Time
- Delivery Time
- Order Accuracy
- On-Time Delivery
- Cancellation Rate
- Return Rate

These KPIs measure operational performance.

---

# Governance

Every lifecycle transition requires:

- validation
- audit logging
- Business Rule compliance
- security verification
- workflow execution

Lifecycle integrity is enforced by the Swissbay Nexus Governance Engine.

---

# Lifecycle Summary

The Sales Order Lifecycle provides the governed operational framework for managing customer orders from creation through fulfilment, invoicing, completion and archival.

By defining controlled lifecycle stages, approvals, validations, warehouse activities and AI-assisted decision making, Swissbay Nexus ensures that every Sales Order remains a trusted enterprise transaction supporting Sales, Warehouse Operations, Finance, Customer Service and Executive Management throughout the complete Quote-to-Cash process.