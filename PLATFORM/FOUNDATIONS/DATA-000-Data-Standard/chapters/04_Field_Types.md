# 04 — Field Types

## Purpose

Field types define how data should be represented.

## Standard Field Types

| Type | Use |
|---|---|
| text | General words or descriptions |
| number | Numeric values without currency |
| currency | Money values |
| date | Calendar dates |
| datetime | Date and time |
| boolean | True or false |
| enum | Controlled list |
| relationship | Link to another object |
| document_link | Link to a file |
| email | Email address |
| phone | Phone number |
| url | Website link |
| address | Structured address |

## Field Definition Standard

Each field should define:

- field name
- type
- required or optional
- description
- owner
- validation rule
- example value

## Example

| Field | Type | Required | Example |
|---|---|---|---|
| customer_id | text | Yes | CUSTOMER-000001 |
| legal_name | text | Yes | Clover SA (Pty) Ltd |
| payment_terms | enum | Yes | 30 days |
| credit_limit | currency | No | ZAR 100,000 |
