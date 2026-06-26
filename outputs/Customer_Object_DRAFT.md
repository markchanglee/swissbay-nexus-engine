```markdown
# Customer Object

**File:** `03_BUSINESS_OBJECTS/01_Customer_Object.md`  
**Object ID:** OBJ-001  
**Status:** Building  
**Version:** 0.2.0  
**Last Updated:** 2026-06-26  

---

## 1. Purpose

The Customer Object defines how Swissbay records, manages, and understands every company or organisation that buys from Swissbay, may buy from Swissbay, or should be managed as a target account.

A Customer is the organisation Swissbay serves or wants to serve.

For Swissbay, this includes:

- Schools
- Food manufacturers
- Corporate facilities
- Other Gauteng-based B2B organisations that buy operational procurement products

Swissbay supplies customers with categories such as:

- PPE
- Cleaning chemicals
- Toilet paper
- Cleaning supplies
- Hygiene products
- Coffee cups and food service consumables

This object creates one standard way to track customer knowledge across sales, quoting, orders, follow-up, recurring revenue, account risk, and AI support.

---

## 2. Business Value

The Customer Object helps Swissbay:

1. **Increase recurring revenue**
   - Identify customers that should be buying monthly or quarterly.
   - Track repeat-purchase potential across PPE, hygiene, cleaning, toilet paper, and consumables.

2. **Improve follow-up**
   - Ensure no school, factory, or facility account is forgotten after a quote, order, complaint, or meeting.

3. **Quote faster**
   - Store customer preferences, delivery details, procurement contacts, and previous purchase history.

4. **Reduce admin load**
   - Keep customer information in one structured format instead of scattered across email, WhatsApp, Sage, Excel, and memory.

5. **Improve customer retention**
   - Track customer health, risks, complaints, payment behaviour, and relationship strength.

6. **Build toward scale**
   - Create a customer data structure that can later support CRM automation, AI account management, procurement intelligence, and a larger Swissbay platform.

---

## 3. Owner

### Business Owner

**Sales / Account Management Owner**

Responsible for:

- Ensuring every active and target customer exists in the CRM or customer tracker.
- Keeping customer status, contacts, follow-up dates, and account notes up to date.
- Reviewing customer health and risk.
- Identifying recurring revenue opportunities.

### Supporting Owners

| Role | Responsibility |
|---|---|
| Sales | Leads, opportunities, quotes, follow-ups, relationship notes |
| Operations / Admin | Orders, delivery details, invoice support, customer requirements |
| Finance | Payment terms, overdue invoices, credit risk |
| Leadership | Key accounts, strategic customers, lost customers, escalation decisions |

---

## 4. When This Object Is Created

A Customer record must be created when any of the following happens:

1. A company requests a quote.
2. Swissbay identifies a company as a serious target account.
3. A company places an order.
4. A company is imported from Sage, Excel, email, WhatsApp, or historical records.
5. A lead becomes qualified enough that Swissbay needs to track the organisation, contacts, buying needs, and follow-up.
6. A previous customer needs to be reactivated.

A Customer record must **not** be created for:

- A person only — use the Contact Object.
- A once-off unqualified name with no company details — use the Lead Object first.
- A supplier — use the Supplier Object.
- A product buyer without an organisation, unless Swissbay chooses to serve them as a business customer.

Rule:

> If Swissbay has quoted, sold to, met with, or actively wants to sell to an organisation, it must exist as a Customer record.

---

## 5. Core Data Fields

### 5.1 Required Fields

| Field | Description | Example |
|---|---|---|
| Customer Name | Official or trading name of the organisation | ABC Primary School |
| Customer Type | Main customer segment | School |
| Customer Status | Current commercial status | Active Customer |
| Primary Contact | Main person Swissbay deals with | Procurement Manager |
| Contact Details | Email and phone number for main contact | buyer@example.co.za |
| Location | Main area or delivery location | Midrand, Gauteng |
| Product Categories Needed | Categories the customer buys or may buy | Cleaning chemicals, toilet paper |
| Account Owner | Swissbay person responsible for follow-up | Sales Rep / Owner |
| Last Interaction Date | Last quote, call, WhatsApp, meeting, or order date | 2026-06-20 |
| Next Follow-Up Date | Next required action date | 2026-07-01 |
| Source | How Swissbay found or acquired the customer | Referral, website, cold outreach |
| Notes | Practical account notes | Uses monthly hygiene consumables |

### 5.2 Recommended Fields

| Field | Description | Example |
|---|---|---|
| Registered Company Name | Legal entity name if different from trading name | ABC Education NPC |
| Registration Number | Company or school registration number if available | 2020/000000/08 |
| VAT Number | VAT number if applicable | 4000000000 |
| Billing Address | Address used for invoices | Johannesburg |
| Delivery Address | Main delivery location | Germiston |
| Payment Terms | Agreed terms | COD, 7 days, 30 days |
| Credit Limit | Internal approved credit exposure | R20,000 |
| Preferred Quote Format | How the customer prefers quotes | PDF by email |
| Preferred Communication Channel | Email, WhatsApp, phone, in-person | WhatsApp + email |
| Buying Frequency | Expected buying pattern | Monthly |
| Estimated Monthly Spend | Approximate potential recurring value | R15,000 |
| Current Supplier | Known competitor or current supplier | Existing PPE supplier |
| Decision Process | How buying decisions are made | Principal approval required |
| Procurement Notes | Special requirements | Needs 3 quotes for school approval |
| Delivery Notes | Access, receiving times, security details | Deliver before 12:00 |
| Compliance Needs | Documents required | B-BBEE, tax clearance, MSDS |
| Customer Health | Green, Amber, Red | Green |
| Customer Risk Level | Low, Medium, High | Medium |
| Recurring Revenue Potential | Low, Medium, High | High |
| Last Order Date | Most recent confirmed order | 2026-06-10 |
| Last Quote Date | Most recent quote sent | 2026-06-18 |
| Total Lifetime Revenue | Total historical sales | R85,000 |
| Open Invoice Balance | Amount currently unpaid | R12,500 |
| Overdue Amount | Amount past due date | R5,000 |
| Tags | Useful labels | Key Account, School, Cleaning |

---

## 6. Customer Types

Swissbay uses Customer Type to segment accounts by how they buy, what they need, and how they should be served.

| Customer Type | Description | Typical Needs |
|---|---|---|
| School | Public or private education institution | Toilet paper, cleaning chemicals, hygiene products, PPE, cleaning supplies |
| Food Manufacturer | Factory or production business in food sector | PPE, hygiene products, cleaning chemicals, consumables, compliance-related supplies |
| Corporate Facility | Office park, corporate building, warehouse, facility manager, or operations site | Toilet paper, cleaning supplies, hygiene products, coffee cups, PPE |
| Facility Management Company | Company buying for multiple managed sites | Cleaning supplies, hygiene products, consumables, PPE |
| Hospitality / Food Service | Business using consumables for serving food or drinks | Coffee cups, food service consumables, cleaning products |
| Industrial / Operations Business | Operational site requiring PPE and supplies | PPE, cleaning chemicals, hygiene products |
| Government / Public Institution | Public sector or municipal-type customer | PPE, cleaning, hygiene, tender-related supply |
| Other B2B Customer | Any other business with operational procurement needs | Depends on account |

Each customer must have one primary Customer Type.

Secondary tags may be used where needed.

Example:

- Primary Type: Corporate Facility
- Tags: Office Park, Monthly Consumables, Hygiene

---

## 7. Customer Statuses

Customer Status shows where the organisation is in its commercial relationship with Swissbay.

| Status | Meaning | Action Required |
|---|---|---|
| Target Account | Swissbay wants to sell to this organisation but has not yet engaged meaningfully | Assign owner and create outreach task |
| Active Prospect | Engagement has started but no quote or order yet | Qualify needs and decision process |
| Quoted | Swissbay has sent at least one quote but no confirmed order yet | Follow up until won, lost, or revised |
| Active Customer | Customer has placed an order within the last 90 days | Maintain relationship and look for repeat orders |
| Recurring Customer | Customer buys repeatedly on a known cycle | Track reorder dates and protect account |
| Dormant Customer | No order in the last 90–180 days but still worth reactivating | Create reactivation task |
| Lost Customer | Customer has moved to another supplier or stopped buying from Swissbay | Record lost reason and review later |
| Inactive / Archive | No current value or not a fit for Swissbay | Keep record but stop active follow-up |
| Do Not Serve | Customer should not be served due to payment, risk, abuse, or strategic decision | Leadership approval required |

Status must be reviewed whenever:

- A quote is sent.
- An order is placed.
- A customer stops buying.
- A payment issue occurs.
- A major complaint occurs.
- A customer is reactivated.

---

## 8. Related Contacts

A Customer can have many related Contacts.

A Contact is a person who works at or is connected to the customer organisation.

Examples:

- Buyer
- Procurement manager
- Principal
- Operations manager
- Facility manager
- Finance contact
- Receiving contact
- Owner / Managing director

### Required Contact Rules

Every active Customer should have at least:

1. One primary buying contact.
2. One finance or accounts contact, if credit is offered.
3. One delivery or receiving contact, where relevant.

### Contact Fields to Link

| Contact Field | Purpose |
|---|---|
| Name | Identifies the person |
| Role | Shows buying influence |
| Email | Quote and invoice communication |
| Phone / WhatsApp | Fast operational communication |
| Decision Influence | Decision maker, influencer, admin, finance, receiver |
| Preferred Channel | Email, phone, WhatsApp |
| Notes | Relationship details and practical context |

Rule:

> Do not store all relationship knowledge only in WhatsApp or memory. Key contact information must be linked to the Customer record.

---

## 9. Related Leads

A Lead is an early-stage sales signal.

A Customer may have one or many related Leads.

Examples:

- Website enquiry from a school.
- Referral to a food manufacturing buyer.
- Cold outreach list for corporate facilities.
- WhatsApp request for PPE pricing.
- Email enquiry for toilet paper supply.

### Lead-to-Customer Rule

A Lead becomes linked to a Customer when:

- The organisation is identified.
- There is a real buying need.
- Swissbay needs to quote, follow up, or track the account.

The Lead should show:

- Source
- Date received
- Product interest
- Contact person
- Qualification notes
- Conversion status

Lead outcomes:

- Converted to Opportunity
- Converted to Quote
- Disqualified
- No response
- Future follow-up

---

## 10. Related Opportunities

An Opportunity is a possible sale or account expansion.

A Customer can have multiple Opportunities.

Examples:

- Monthly toilet paper supply for a school.
- PPE contract for a food manufacturer.
- Cleaning chemicals supply for a facility.
- Coffee cup supply for a corporate canteen.
- Switching a customer from once-off orders to monthly recurring supply.

### Opportunity Fields to Link

| Field | Description |
|---|---|
| Opportunity Name | Clear description of potential sale |
| Product Category | PPE, cleaning chemicals, hygiene, etc. |
| Estimated Value | Expected order or monthly value |
| Probability | Likelihood of winning |
| Stage | Qualified, quoted, negotiation, won, lost |
| Close Date | Expected decision date |
| Owner | Swissbay person responsible |
| Next Step | Required action |
| Competitor / Current Supplier | If known |
| Lost Reason | If not won |

Rule:

> Every meaningful future sale should be captured as an Opportunity, not left as a memory or WhatsApp thread.

---

## 11. Related Quotes

A Quote is a formal or semi-formal offer to supply products at stated prices and terms.

A Customer can have many Quotes.

Quote history is essential for Swissbay because slow quoting and poor follow-up are current pain points.

### Quote Links Required

Each quote must link back to:

- Customer
- Contact
- Opportunity, where applicable
- Products quoted
- Quote date
- Quote amount
- Quote status
- Follow-up date
- Outcome

### Quote Statuses

| Status | Meaning |
|---|---|
| Draft | Quote being prepared |
| Sent | Quote sent to customer |
| Follow-Up Due | Customer has not responded and follow-up is needed |
| Revised | Quote updated due to price, quantity, or requirements |
| Accepted | Customer approved quote |
| Rejected | Customer declined quote |
| Expired | Quote validity period passed |
| Converted to Order | Quote became a confirmed order |

### Operational Rule

Every quote must have a next action:

- Follow up
- Revise
- Convert to order
- Mark as lost
- Set future reminder

No quote should disappear after being sent.

---

## 12. Related Orders

An Order is a confirmed customer purchase.

A Customer can have many Orders.

Orders reveal what the customer actually buys, how often they buy, and what repeat revenue is possible.

### Order Fields to Link

| Field | Description |
|---|---|
| Customer | Buying organisation |
| Contact | Person who placed or approved order |
| Quote Reference | Quote that became the order, if applicable |
| Order Date | Date order was confirmed |
| Products | Items ordered |
| Quantities | Order quantities |
| Order Value | Total value |
| Delivery Address | Where goods must be delivered |
| Delivery Date | Requested or actual delivery date |
| Order Status | New, processing, delivered, complete, cancelled |
| Invoice Reference | Related invoice |
| Notes | Special instructions |

### Order Insights to Capture

For repeatable customers, record:

- Frequently ordered products
- Average order value
- Buying frequency
- Seasonal patterns
- Preferred brands or specifications
- Delivery requirements
- Problems or complaints

---

## 13. Related Invoices

An Invoice is a financial record of what Swissbay has billed the customer.

A Customer can have many Invoices.

Invoice data helps Swissbay manage cashflow, risk, credit decisions, and account health.

### Invoice Fields to Link

| Field | Description |
|---|---|
| Customer | Billed organisation |
| Invoice Number | Sage or internal invoice reference |
| Invoice Date | Date issued |
| Due Date | Payment due date |
| Invoice Amount | Total value |
| Amount Paid | Amount received |
| Outstanding Amount | Balance unpaid |
| Payment Status | Paid, unpaid, part-paid, overdue |
| Related Order | Order being invoiced |
| Finance Notes | Payment issues or agreements |

### Payment Statuses

| Status | Meaning |
|---|---|
| Paid | Fully paid |
| Unpaid | Not yet paid but not overdue |
| Part-Paid | Partial payment received |
| Overdue | Past payment due date |
| Disputed | Customer has queried invoice |
| Written Off | Not expected to be recovered |

### Finance Rule

If a customer has overdue invoices, Sales must know before offering further credit or accepting large new orders.

---

## 14. Related Meetings

A Meeting is any meaningful customer interaction that creates business value or requires follow-up.

Meetings include:

- In-person visits
- Phone calls
- WhatsApp discussions
- Online meetings
- Site inspections
- Procurement reviews
- Complaint discussions
- Pricing negotiations

### Meeting Fields to Link

| Field | Description |
|---|---|
| Customer | Organisation discussed |
| Contacts Present | People involved |
| Meeting Date | Date of interaction |
| Meeting Type | Sales, account review, complaint, negotiation, site visit |
| Summary | What was discussed |
| Needs Identified | Products, problems, buying cycles |
| Decisions Made | Customer or Swissbay decisions |
| Actions | Follow-up tasks |
| Owner | Person responsible |
| Due Date | Date action must be completed |

### Meeting Rule

Any meeting that produces a quote, task, complaint, decision, or opportunity must be recorded against the Customer.

---

## 15. Customer Health

Customer Health shows the current strength and quality of the customer relationship.

Swissbay uses a simple traffic-light model.

| Health | Meaning | Typical Signs | Action |
|---|---|---|---|
| Green | Healthy account | Buying regularly, pays on time, responsive, no major issues | Maintain and grow |
| Amber | Needs attention | Slow responses, reduced buying, late payment, unresolved quote, small complaint | Follow up and review |
| Red | At risk | Overdue payments, serious complaint, no recent orders, switching supplier, poor relationship | Escalate and intervene |

### Health Factors

Customer Health should consider:

1. Last order date
2. Last interaction date
3. Quote response behaviour
4. Payment behaviour
5. Complaint history
6. Buying trend
7. Relationship strength
8. Recurring revenue potential
9. Competitor threat
10. Strategic value to Swissbay

### Health Review Frequency

| Customer Type | Review Frequency |
|---|---|
| Key recurring customer | Monthly |
| Active customer | Every 60–90 days |
| Dormant customer | Before reactivation campaign |
| Red-risk customer | Weekly until resolved |

---

## 16. Customer Risk

Customer Risk identifies accounts that may create financial, operational, reputational, or strategic problems.

### Risk Categories

| Risk Type | Description | Example |
|---|---|---|
| Payment Risk | Customer may not pay on time or at all | Repeated overdue invoices |
| Margin Risk | Customer demands unsustainable pricing | Very low-margin PPE order |
| Operational Risk | Difficult delivery or fulfilment requirements | Remote delivery with strict receiving windows |
| Relationship Risk | Weak or unstable relationship | Only one contact and that person may leave |
| Churn Risk | Customer may stop buying | Competitor quoting aggressively |
| Compliance Risk | Customer requires documents Swissbay cannot provide quickly | Tender compliance documents |
| Concentration Risk | Too much revenue depends on one customer | Large monthly customer with no backup |
| Reputation Risk | Customer may damage Swissbay through disputes or unreasonable expectations | Abusive or dishonest behaviour |

### Risk Levels

| Level | Meaning | Action |
|---|---|---|
| Low | Normal commercial risk | Continue standard service |
| Medium | Needs monitoring | Add notes and review regularly |
| High | Could harm cashflow, margin, or reputation | Escalate to leadership before major commitments |

### High-Risk Rules

A customer should be marked High Risk if:

- They have significant overdue invoices.
- They repeatedly dispute invoices without valid reason.
- They demand pricing below sustainable margin.
- They place urgent orders but delay payment.
- They have caused serious operational or relationship issues.
- Leadership decides Swissbay should limit exposure.

---

## 17. Recurring Revenue Potential

Recurring Revenue Potential shows whether the customer could buy from Swissbay repeatedly.

This is critical because Swissbay wants more recurring revenue and more predictable cashflow.

### Potential Levels

| Level | Meaning | Example |
|---|---|---|
| High | Customer has repeat monthly or quarterly needs across Swissbay categories | School buying toilet paper, cleaning chemicals, hygiene products monthly |
| Medium | Customer has some repeat needs but volume or consistency is uncertain | Corporate facility ordering cleaning supplies occasionally |
| Low | Mostly once-off or irregular buying | One-time PPE request |

### Factors to Assess

Recurring Revenue Potential should consider:

1. Customer type
2. Number of sites
3. Number of staff, learners, workers, or facility users
4. Product categories used regularly
5. Existing supplier relationship
6. Buying frequency
7. Monthly spend potential
8. Ability to standardise a basket of products
9. Payment reliability
10. Delivery feasibility in Gauteng

### Product Categories with Strong Recurring Potential

| Category | Recurring Use Case |
|---|---|
| Toilet Paper | Schools, corporate facilities, factories |
| Cleaning Chemicals | Schools, facilities, food manufacturers |
| Hygiene Products | Bathrooms, kitchens, production areas |
| Cleaning Supplies | Mops, cloths, gloves, refuse bags |
| PPE | Factories, operations teams, food manufacturing |
| Coffee Cups / Food Service Consumables | Corporate canteens, events, food service areas |

### Recurring Revenue Actions

For High Potential customers:

- Build a standard monthly basket.
- Track expected reorder dates.
- Create follow-up tasks before stock runs out.
- Offer scheduled ordering where possible.
- Review pricing and margin regularly.
- Identify cross-sell opportunities.

---

## 18. Workflow Usage

The Customer Object is used in the following Swissbay workflows.

| Workflow | How the Customer Object Is Used |
|---|---|
| Lead Capture | Links new enquiries to an organisation |
| Lead Qualification | Confirms whether the organisation is a real potential buyer |
| Quote Preparation | Supplies customer details, contacts, requirements, and history |
| Quote Follow-Up | Tracks quote status and next action |
| Order Processing | Links confirmed purchases to customer history |
| Delivery Coordination | Provides delivery address, receiving contact, and special instructions |
| Invoicing | Links billing details, payment terms, and finance contacts |
| Collections | Shows overdue invoices and payment risk |
| Account Management | Tracks health, recurring revenue, and relationship notes |
| Reactivation | Identifies dormant customers worth contacting again |
| Complaint Handling | Records issues, actions, and impact on customer health |
| Supplier Planning | Uses customer demand patterns to improve supplier sourcing |
| Sales Reporting | Measures active customers, conversion, revenue, and retention |
| AI Account Support | Allows AI to summarise accounts and recommend next actions |

### Minimum Workflow Rule

Every active Customer must have:

- A current status
- An account owner
- A primary contact
- A last interaction date
- A next follow-up date or clear reason why no follow-up is needed

---

## 19. AI Support

AI may support the Customer Object by preparing, summarising, classifying, and recommending actions.

AI does not approve final business decisions.

### AI Can Help With

| AI Task | Description |
|---|---|
| Customer Summary | Summarise the account history, needs, quotes, orders, and risks |
| Follow-Up Suggestions | Recommend next actions based on quote status, last interaction, and order history |
| Quote Preparation Support | Draft quote emails using customer context and previous purchases |
| Recurring Basket Suggestions | Suggest repeat-order bundles based on customer type and order history |
| Customer Health Review | Flag customers that may be Amber or Red |
| Risk Detection | Identify payment, churn, margin, or relationship risks from notes and invoices |
| Meeting Note Processing | Turn meeting notes or WhatsApp summaries into structured actions |
| Reactivation Campaigns | Identify dormant customers and draft reactivation messages |
| Cross-Sell Suggestions | Suggest additional categories relevant to the customer |
| CRM Hygiene | Detect missing fields, duplicates, outdated contacts, or stale follow-ups |

### AI Must Not

AI must not:

- Approve customer credit.
- Promise pricing without human approval.
- Confirm delivery dates without operations confirmation.
- Change customer status without human review.
- Delete customer records.
- Make final decisions on high-risk customers.

### Useful AI Prompts

Examples:

```text
Summarise this customer account for a sales follow-up. Include last quote, last order, open risks, recurring revenue potential, and next best action.
```

```text
Review this customer history and classify customer health as Green, Amber, or Red. Explain the reasons and suggest follow-up actions.
```

```text
Create a reactivation message for a dormant school customer who previously bought toilet paper and cleaning chemicals.
```

```text
Suggest a monthly recurring basket for a corporate facility buying hygiene products, toilet paper, and cleaning supplies.
```

---

## 20. Related Documents

| Document | Relationship |
|---|---|
| `vault/00_CONTEXT/Swissbay_Nexus_Project_Context.md` | Defines overall Swissbay Nexus context |
| `vault/00_CONTEXT/Nexus_Constitution.md` | Defines principles and approval model |
| `vault/00_CONTEXT/Nexus_File_Standard.md` | Defines required file structure |
| `vault/00_CONTEXT/Swissbay_Business_Profile.md` | Defines Swissbay business profile |
| `vault/03_BUSINESS_OBJECTS/Business_Object_Standard.md` | Defines standard for all business objects |
| `03_BUSINESS_OBJECTS/02_Supplier_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/03_Product_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/04_Category_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/05_Lead_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/06_Opportunity_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/07_Quote_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/08_Order_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/09_Invoice_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/10_Contact_Object.md` | Future related object |
| `03_BUSINESS_OBJECTS/11_Meeting_Object.md` | Future related object |
| `MASTER_BUILD_INDEX.md` | Tracks build status of Nexus files |

---

## 21. Version History

| Version | Date | Status | Notes |
|---|---:|---|---|
| 0.1.0 | 2026-06-26 | Draft | Initial Customer Object structure created |
| 0.2.0 | 2026-06-26 | Building | Expanded into production-quality Swissbay Customer Object with statuses, relationships, health, risk, recurring revenue, workflow usage, and AI support |

---

## Approval

- Approve
- Revise
- Reject
```