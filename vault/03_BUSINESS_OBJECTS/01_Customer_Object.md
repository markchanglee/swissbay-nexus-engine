---
id: OBJ-001
key: Customer_Object
name: Customer Object
type: business_object
object_type: business_object
status: planned
lifecycle_stage: draft
version: 0.2.0
owner: CRM Intelligence
source_registry: config/registry.yaml
output_path: vault/03_BUSINESS_OBJECTS/01_Customer_Object.md
created: 2026-06-26
last_updated: 2026-06-26
review_status: not_reviewed
approval_status: pending
depends_on:
  - Swissbay_Nexus_Project_Context
  - Nexus_Constitution
  - Nexus_File_Standard
  - Swissbay_Business_Profile
related_departments:
  []
related_ai_agents:
  []
tags:
  - business-object
  - nexus
---

# Customer Object

## Purpose

The Customer Object defines how Swissbay records, understands, serves, and grows each B2B customer account.

For Swissbay, a customer is an organisation that buys, has bought, or is expected to buy operational procurement products from Swissbay, including:

- PPE
- Cleaning chemicals
- Toilet paper
- Cleaning supplies
- Hygiene products
- Coffee cups and food service consumables

Current priority customer types are:

- Schools
- Food manufacturers
- Corporate facilities

This object creates a single shared customer record that connects sales, quoting, order history, follow-up, debtor risk, recurring revenue potential, and customer intelligence.

In Swissbay Nexus, the Customer Object is the main anchor for customer knowledge. If customer information is not connected to this object, it should be treated as incomplete.

> Nexus rule: If it is not in CRM, it does not exist.

## Business Value

The Customer Object helps Swissbay solve current operational problems by making customer information usable, searchable, and actionable.

| Business Problem | How the Customer Object Helps |
|---|---|
| Not enough leads | Identifies target customer types, sectors, locations, and gaps in the customer base. |
| Poor follow-up | Tracks next actions, contact owners, quote status, buying cycles, and dormant accounts. |
| Slow quoting | Stores standard delivery info, product preferences, pricing notes, and previous buying patterns. |
| Not enough recurring revenue | Highlights repeat-use categories such as toilet paper, cleaning chemicals, hygiene products, PPE, and coffee cups. |
| Admin load | Reduces repeated searching through email, WhatsApp, Excel, Sage, and old quotes. |
| Cashflow pressure | Connects customers to payment behaviour, debtor risk, credit terms, and invoice history. |
| Fragmented customer knowledge | Creates one trusted customer profile for sales, operations, admin, and management. |

A strong Customer Object should allow Swissbay to answer:

- Who are our best customers?
- Which customers should we follow up today?
- Which customers buy repeatedly?
- Which customers only buy once?
- Which schools, food manufacturers, or facilities are at risk of being lost?
- Which customers should be offered cleaning chemicals, PPE, hygiene products, toilet paper, or coffee cups next?
- Which customers create cashflow risk?
- Which customers are suitable for long-term recurring supply agreements?

## Owner

**Primary Owner:** CRM Intelligence

**Business Accountability:** Swissbay management

**Operational Users:**

- Sales
- Quoting
- Customer service
- Admin
- Debtors / finance
- Procurement support
- Management

**Ownership Responsibilities:**

CRM Intelligence is responsible for ensuring that the Customer Object:

- Has clear field definitions.
- Supports Swissbay’s current sales and quoting process.
- Can be used by a new employee without needing historical context.
- Connects to related objects such as Contact, Lead, Opportunity, Quote, Order, Invoice, Product, Category, Task, and Meeting.
- Helps Swissbay improve follow-up, recurring revenue, customer retention, and cashflow visibility.
- Evolves from simple customer records today into an AI-enabled procurement intelligence layer in future.

## Inputs

The Customer Object can be created or updated from the following sources:

| Input Source | Customer Information Captured |
|---|---|
| Email | Enquiries, quote requests, complaints, delivery notes, pricing requests, contact details. |
| WhatsApp | Urgent requests, informal orders, buyer preferences, delivery instructions, follow-up commitments. |
| Sage | Legal account name, invoice history, payment behaviour, account code, VAT details, debtor status. |
| Excel | Legacy customer lists, quote trackers, pricing notes, follow-up lists. |
| Website | Contact form enquiries, product interest, company details. |
| Phone calls | Decision maker information, requirements, objections, urgency, relationship notes. |
| Meetings | Account review notes, supply problems, recurring demand, procurement cycles. |
| Quotes | Product interest, pricing history, lost/won patterns, buying categories. |
| Orders | Actual purchasing behaviour, delivery addresses, recurring products, order frequency. |
| Invoices | Revenue, payment terms, overdue amounts, customer value. |
| Inbox notes | Raw notes from [[README|Knowledge Inbox]] that need to be processed into structured customer intelligence. |

Minimum acceptable input for a new customer record:

- Customer organisation name
- Customer type
- Main contact person or department
- Phone number or email address
- Location
- Product/category interest
- Current status
- Owner or responsible Swissbay team member
- Next action

## Outputs

The Customer Object should produce usable outputs for Swissbay operations.

| Output | Used By | Purpose |
|---|---|---|
| Customer profile | Sales, admin, management | Single view of the customer account. |
| Follow-up list | Sales | Shows who needs attention and by when. |
| Quote preparation context | Quoting team | Speeds up quoting with previous needs, preferences, and delivery notes. |
| Recurring revenue opportunities | Management, sales | Identifies repeat-purchase categories and contract potential. |
| Cross-sell suggestions | Sales | Recommends additional Swissbay categories to offer. |
| Dormant customer list | Sales, management | Identifies customers who have not bought recently. |
| Debtor risk view | Admin, finance, management | Supports cashflow decisions and credit control. |
| Customer segmentation | Management | Groups customers by type, value, category usage, location, and buying behaviour. |
| Account history summary | New employees, sales, management | Makes relationship history understandable without searching multiple systems. |
| AI-ready customer context | AI agents, CRM Intelligence | Enables summarisation, prioritisation, next-best action, and customer insights. |

## Core Fields

### Required Identification Fields

| Field | Description | Example |
|---|---|---|
| Customer ID | Unique internal customer identifier. | CUST-000123 |
| Customer Name | Trading or commonly used customer name. | ABC Primary School |
| Legal Entity Name | Registered legal name if different from trading name. | ABC Primary School NPC |
| Sage Account Code | Sage customer/account reference where available. | SAGE-CUS-4582 |
| Customer Type | Main customer segment. | School, Food Manufacturer, Corporate Facility |
| Customer Status | Current lifecycle status. | Active |
| Account Owner | Swissbay person responsible for relationship. | Sales Rep / CRM Owner |
| Created Date | Date customer was first recorded. | 2026-06-26 |
| Last Updated Date | Last meaningful update to customer record. | 2026-06-26 |

### Customer Type

Primary allowed values:

- School
- Food Manufacturer
- Corporate Facility

Secondary/future allowed values:

- Cleaning Contractor
- Hospitality / Food Service
- Healthcare Facility
- Retail / Distribution
- Government / Public Sector
- Other B2B Organisation

### Customer Status

| Status | Meaning | Swissbay Action |
|---|---|---|
| Prospect | Organisation fits Swissbay target market but has not bought yet. | Qualify and create next action. |
| Quoting | Customer has requested pricing or product information. | Complete quote quickly and follow up. |
| Active | Customer has bought recently or is currently buying. | Maintain relationship and grow account. |
| Recurring | Customer buys repeat-use items on a predictable cycle. | Protect relationship and explore supply agreement. |
| Dormant | Previously bought but no recent order. | Re-engage with relevant offer. |
| At Risk | Customer has unresolved complaint, payment issue, poor service experience, or declining activity. | Escalate and recover. |
| On Hold | Customer should not currently be supplied without approval, usually due to account or payment issue. | Management/finance review required. |
| Lost | Customer moved to another supplier or no longer relevant. | Record reason and learn. |
| Do Not Contact | Customer should not be contacted for legal, relationship, or strategic reasons. | Block sales outreach. |

### Contact and Communication Fields

| Field | Description |
|---|---|
| Primary Contact Name | Main person Swissbay deals with. |
| Primary Contact Role | Buyer, procurement manager, school bursar, facilities manager, owner, production manager, etc. |
| Primary Contact Email | Main email address. |
| Primary Contact Phone | Main phone number. |
| WhatsApp Number | Number used for WhatsApp communication, if different. |
| Alternative Contacts | Other people involved in buying, finance, receiving, or approvals. |
| Preferred Communication Channel | Email, WhatsApp, phone, meeting. |
| Communication Notes | Practical notes such as “prefers WhatsApp before 10am” or “send quotes to finance and buyer.” |

### Location and Delivery Fields

| Field | Description |
|---|---|
| Province | Current focus: Gauteng. |
| City / Area | Johannesburg, Pretoria, Midrand, Germiston, Randburg, Centurion, etc. |
| Delivery Address | Main delivery location. |
| Billing Address | Address used for invoicing. |
| Site Access Notes | Gate procedure, receiving hours, security requirements, loading area, school term restrictions. |
| Delivery Preference | Collection, scheduled delivery, urgent delivery, monthly delivery, term-based delivery. |
| Delivery Risk Notes | Any known delivery challenges. |

### Commercial Fields

| Field | Description |
|---|---|
| VAT Number | Customer VAT number where applicable. |
| Payment Terms | COD, 7 days, 15 days, 30 days, approved account, etc. |
| Credit Limit | Approved credit exposure, if used. |
| Account Balance | Current outstanding balance from Sage or finance process. |
| Overdue Amount | Amount overdue, if any. |
| Debtor Risk Level | Low, Medium, High, On Hold. |
| Pricing Tier | Standard, negotiated, contract, school pricing, volume pricing, management approved. |
| Discount Notes | Approved discount logic or pricing exceptions. |
| Purchase Order Required | Yes/No. |
| PO Process Notes | Who issues POs, required format, approval steps. |

### Buying Behaviour Fields

| Field | Description |
|---|---|
| Main Buying Categories | PPE, cleaning chemicals, toilet paper, cleaning supplies, hygiene products, coffee cups. |
| Products Previously Bought | Actual product history where available. |
| Products Quoted But Not Bought | Useful for follow-up and lost opportunity analysis. |
| Order Frequency | Once-off, weekly, monthly, termly, quarterly, ad hoc. |
| Average Order Value | Approximate average order value. |
| Annual Revenue | Total annual sales value where available. |
| Last Quote Date | Most recent quote sent. |
| Last Order Date | Most recent confirmed order. |
| Last Invoice Date | Most recent invoice. |
| Last Contact Date | Most recent meaningful customer communication. |
| Next Expected Purchase Date | Estimated date for next purchase. |
| Recurring Revenue Potential | Low, Medium, High. |
| Cross-Sell Potential | Categories Swissbay should offer next. |

### Segment-Specific Fields

#### Schools

| Field | Description |
|---|---|
| School Type | Public, private, independent, nursery, primary, high school, college. |
| Decision Makers | Principal, bursar, procurement/admin office, facilities manager. |
| Buying Cycle | Monthly, termly, annual budget cycle, urgent ad hoc. |
| Common Needs | Toilet paper, cleaning chemicals, hygiene products, cleaning supplies, PPE. |
| School Calendar Notes | Term dates, holidays, budget timing, exam periods affecting deliveries. |

#### Food Manufacturers

| Field | Description |
|---|---|
| Facility Type | Bakery, meat processor, food packer, beverage producer, other. |
| Decision Makers | Production manager, procurement manager, quality manager, operations manager. |
| Compliance Sensitivity | Food safety, hygiene, PPE suitability, documentation needs. |
| Common Needs | PPE, hygiene products, cleaning chemicals, cleaning supplies, consumables. |
| Urgency Profile | Production stoppage risk, emergency supply likelihood, repeat demand. |

#### Corporate Facilities

| Field | Description |
|---|---|
| Facility Type | Office park, warehouse, head office, call centre, corporate campus. |
| Decision Makers | Facilities manager, office manager, procurement, finance, building manager. |
| Common Needs | Toilet paper, cleaning supplies, hygiene products, coffee cups, cleaning chemicals. |
| Service Expectations | Regular replenishment, reliable delivery, consolidated invoicing, quick quote turnaround. |

### Relationship and Intelligence Fields

| Field | Description |
|---|---|
| Relationship Strength | New, developing, stable, strong, at risk. |
| Key Customer Notes | Important context that affects service or selling. |
| Pain Points | Customer frustrations or operational problems Swissbay can solve. |
| Competitor Notes | Known competing suppliers or reasons customer compares pricing. |
| Win Reason | Why Swissbay won previous business. |
| Loss Reason | Why Swissbay lost a quote or account. |
| Complaint History | Summary of complaints and resolutions. |
| Management Attention Required | Yes/No flag for strategic, high-value, high-risk, or sensitive accounts. |
| Strategic Account Flag | Yes/No. |
| Notes Quality | Clean, incomplete, duplicate, needs review. |

### Data Quality Rules

Every active customer record should have:

- Customer name
- Customer type
- Primary contact or responsible department
- Contact method
- Location
- Customer status
- Account owner
- Last contact date
- Next action
- At least one product category of interest or purchase history
- Payment status or debtor risk indicator where relevant

Records should be flagged for cleanup if:

- The customer name is duplicated.
- The only information is a name and no contact details.
- The customer has no status.
- There is no owner.
- The last contact date is unknown.
- There is quote or invoice activity but no customer profile.
- WhatsApp/email information exists outside CRM but is not captured.

## Relationships

The Customer Object connects to other Swissbay Nexus business objects.

| Related Object | Relationship |
|---|---|
| [[Lead_Object|Lead]] | A lead may become a customer after qualification or purchase. |
| [[Contact_Object|Contact]] | A customer can have multiple contacts, including buyers, finance contacts, receiving contacts, and decision makers. |
| [[Opportunity_Object|Opportunity]] | A customer can have multiple active or historical sales opportunities. |
| [[Quote_Object|Quote]] | A customer can receive many quotes across different categories. |
| [[Order_Object|Order]] | A customer can place many confirmed orders. |
| [[Invoice_Object|Invoice]] | A customer can have many invoices and payment records. |
| [[Product_Object|Product]] | A customer buys or shows interest in specific products. |
| [[Category_Object|Category]] | A customer is linked to buying categories such as PPE, cleaning chemicals, toilet paper, cleaning supplies, hygiene products, and coffee cups. |
| [[Supplier_Object|Supplier]] | Customer needs may influence which suppliers Swissbay must develop or prioritise. |
| [[Task_Object|Task]] | Follow-ups, quote reminders, complaint actions, and account reviews are linked to customers. |
| [[Meeting_Object|Meeting]] | Customer meetings generate relationship notes and action items. |
| [[Decision_Object|Decision]] | Important account decisions, such as credit approval or strategic pricing, should be linked to the customer. |
| [[Risk_Object|Risk]] | Customer-specific risks include debtor risk, supply risk, complaint risk, and churn risk. |
| [[KPI_Object|KPI]] | Customer data feeds KPIs such as quote turnaround, conversion rate, repeat revenue, dormant accounts, and debtor exposure. |
| [[Workflow_Object|Workflow]] | Customer records are used by sales, quoting, follow-up, debtor, and retention workflows. |

## Workflow Usage

The Customer Object is used in the following Swissbay workflows.

### 1. New Lead to Customer Workflow

Used when Swissbay receives an enquiry from email, website, WhatsApp, referral, phone call, or outbound prospecting.

Customer Object usage:

1. Check whether the organisation already exists.
2. If not, create a new customer/prospect record.
3. Capture customer type, location, contact details, and category interest.
4. Assign an owner.
5. Create next action.
6. Link any quote request or opportunity.
7. Update status from Prospect to Quoting, Active, Lost, or Dormant as the relationship develops.

### 2. Quote Request Workflow

Used when a school, food manufacturer, corporate facility, or other B2B customer asks for pricing.

Customer Object usage:

1. Confirm customer details.
2. Check previous quotes and buying history.
3. Check payment status or account hold notes before quoting where relevant.
4. Confirm category and product interest.
5. Use delivery notes and pricing tier to prepare the quote faster.
6. Record quote date and quote status.
7. Create follow-up task.

### 3. Follow-Up Workflow

Used to improve quote conversion and customer retention.

Customer Object usage:

1. Filter customers by last quote date, last contact date, and next action date.
2. Prioritise high-value, recurring, or strategic accounts.
3. Follow up using preferred channel.
4. Record outcome.
5. Update next expected purchase date.
6. Escalate at-risk accounts.

### 4. Recurring Revenue Workflow

Used to build predictable sales from repeat-use operational products.

Customer Object usage:

1. Identify customers buying repeat categories:
   - Toilet paper
   - Cleaning chemicals
   - Hygiene products
   - Cleaning supplies
   - PPE
   - Coffee cups
2. Estimate order frequency.
3. Set next expected purchase date.
4. Create recurring follow-up reminders.
5. Offer monthly, termly, or scheduled supply options.
6. Track whether customer becomes Recurring status.

### 5. Dormant Customer Recovery Workflow

Used when a previously active customer has stopped buying.

Customer Object usage:

1. Identify customers with no recent quote, order, or contact.
2. Check previous categories bought.
3. Check complaint or service history before contacting.
4. Prepare relevant reactivation offer.
5. Record reason for inactivity.
6. Update status to Active, Dormant, Lost, or Do Not Contact.

### 6. Debtor and Cashflow Workflow

Used to reduce cashflow pressure and avoid risky supply decisions.

Customer Object usage:

1. Connect Sage account information to customer record.
2. Check account balance, overdue amount, payment terms, and debtor risk.
3. Flag customers that require management or finance approval before supply.
4. Record account hold status where applicable.
5. Link payment issues to customer notes and future quoting decisions.

### 7. Account Review Workflow

Used for important, high-value, recurring, or strategic customers.

Customer Object usage:

1. Review revenue, margin if available, buying categories, service issues, and payment behaviour.
2. Identify cross-sell opportunities.
3. Identify supply risk or competitor risk.
4. Set next account growth action.
5. Update relationship strength and strategic account flag.

## AI Support

AI may assist with the Customer Object, but humans approve final customer decisions.

### AI Can Help With

| AI Support Area | Description |
|---|---|
| Customer profile summarisation | Summarise email, WhatsApp notes, quote history, order history, and meeting notes into a clear customer profile. |
| CRM cleanup | Detect duplicate customers, missing fields, inconsistent names, and incomplete records. |
| Next-best action | Suggest who to follow up based on last quote date, last contact date, customer value, and expected reorder timing. |
| Quote preparation | Summarise customer preferences, previous buying categories, delivery notes, and pricing history before quote creation. |
| Cross-sell suggestions | Recommend relevant Swissbay categories based on customer type and past purchases. |
| Dormant account detection | Identify customers who have stopped buying and suggest reactivation actions. |
| Churn risk detection | Flag accounts with declining orders, complaints, delayed follow-up, or competitor mentions. |
| Debtor context summaries | Summarise account/payment risk for management review, using finance-approved data. |
| Meeting and call note processing | Convert raw notes into structured customer updates, tasks, and follow-up actions. |
| Customer segmentation | Group customers by type, location, category usage, revenue, recurrence, and risk. |

### AI Must Not

AI must not independently:

- Approve credit terms.
- Change payment status without verified finance data.
- Promise pricing or stock availability.
- Confirm delivery dates without operational confirmation.
- Delete customer records.
- Mark strategic accounts as lost without human approval.
- Override management decisions.
- Send sensitive customer communication without review where risk is high.

### AI Prompt Examples

Useful internal prompts:

```text
Summarise this customer’s latest emails, quotes, and notes into a clean Swissbay customer profile. Highlight buying categories, open follow-ups, debtor concerns, and recurring revenue potential.
```

```text
Review this customer record and identify missing CRM fields that would slow down quoting or follow-up.
```

```text
Based on this customer’s history, suggest the next 3 sales actions Swissbay should take. Prioritise recurring revenue, quote conversion, and customer retention.
```

```text
Identify cross-sell opportunities for this school based on Swissbay categories: PPE, cleaning chemicals, toilet paper, cleaning supplies, hygiene products, and coffee cups.
```

## Related Documents

| Document | Relationship |
|---|---|
| [[Swissbay_Nexus_Project_Context]] | Defines Swissbay Nexus, business context, goals, and current pain points. |
| [[Nexus_Constitution]] | Defines operating principles, including AI prepares and humans approve. |
| [[Nexus_File_Standard]] | Defines required sections and quality test for Nexus files. |
| [[Swissbay_Business_Profile]] | Defines Swissbay’s company type, current market, products, customers, and problem areas. |
| [[Business_Object_Standard]] | Defines the standard structure for Swissbay Nexus business objects. |
| [[Lead_Object]] | Future object for pre-customer sales records. |
| [[Contact_Object]] | Future object for people linked to customer organisations. |
| [[Opportunity_Object]] | Future object for active sales opportunities. |
| [[Quote_Object]] | Future object for quote creation, tracking, and conversion. |
| [[Order_Object]] | Future object for confirmed customer orders. |
| [[Invoice_Object]] | Future object for billing, debtor visibility, and cashflow tracking. |
| [[Product_Object]] | Future object for sellable items. |
| [[Category_Object]] | Future object for product groupings such as PPE and cleaning chemicals. |
| [[Task_Object]] | Future object for follow-ups and operational actions. |
| [[Meeting_Object]] | Future object for customer meeting notes and action items. |

## Future Improvements

Future versions of the Customer Object should add:

1. **CRM system mapping**
   - Map each field to the actual CRM, Sage, Excel, or database location used by Swissbay.

2. **Customer scoring**
   - Add scoring for revenue potential, recurrence potential, debtor risk, relationship strength, and strategic value.

3. **Recurring revenue engine**
   - Automatically identify reorder cycles for toilet paper, hygiene products, cleaning chemicals, PPE, cleaning supplies, and coffee cups.

4. **Quote conversion analytics**
   - Track which customer types convert best and which categories are most profitable.

5. **Dormant customer recovery dashboard**
   - Show customers who should be reactivated by segment, category, and last purchase date.

6. **Customer profitability view**
   - Add margin, delivery cost, admin load, payment behaviour, and service complexity.

7. **AI customer memory**
   - Build customer summaries that update from email, WhatsApp, quotes, orders, invoices, and meeting notes.

8. **Account planning templates**
   - Create specific account review templates for schools, food manufacturers, and corporate facilities.

9. **Credit and debtor workflow integration**
   - Improve connection between customer status, account hold decisions, Sage data, and cashflow management.

10. **Customer duplicate prevention**
   - Add rules for matching customers by legal name, trading name, email domain, phone number, Sage account code, and delivery address.

## Version History

| Version | Date | Status | Owner | Notes |
|---|---:|---|---|---|
| 0.2.0 | 2026-06-26 | Draft | CRM Intelligence | First production draft of the Customer Object for Swissbay Nexus. |

- Approve
- Revise
- Reject