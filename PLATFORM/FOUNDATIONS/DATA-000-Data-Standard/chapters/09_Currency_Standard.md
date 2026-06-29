# 09 — Currency Standard

## Purpose

Currency values must be explicit and consistent.

## Default Currency

Default operational currency:

```text
ZAR
```

## Format

Use:

```text
ZAR 30,000
```

or structured fields:

```yaml
amount: 30000
currency: ZAR
```

## Rules

- Do not store monetary amounts without currency.
- Do not mix VAT-inclusive and VAT-exclusive amounts without labelling them.
- Quote, order and invoice specifications must define whether amounts include VAT.

## Important Fields

- unit_price_ex_vat
- unit_price_inc_vat
- vat_amount
- total_ex_vat
- total_inc_vat
- currency
