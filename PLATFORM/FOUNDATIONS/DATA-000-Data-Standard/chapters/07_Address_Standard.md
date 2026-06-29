# 07 — Address Standard

## Purpose

Addresses must be structured so they can support delivery, billing, reporting and future integrations.

## Address Fields

| Field | Required | Notes |
|---|---|---|
| address_type | Yes | billing, delivery, site, warehouse |
| site_name | No | e.g. Clover Midrand Plant |
| building | No | building or unit |
| street_address | Yes | street number and name |
| suburb | No | suburb or area |
| city | Yes | city |
| province | Yes | province |
| country | Yes | country |
| postal_code | No | postal code |
| delivery_instructions | No | access notes, receiving times |

## South African Standard

Use province values consistently:

- Gauteng
- Western Cape
- KwaZulu-Natal
- Eastern Cape
- Free State
- Limpopo
- Mpumalanga
- North West
- Northern Cape

## Rule

Do not store a complex delivery address as one unstructured paragraph if the address will be used repeatedly.
