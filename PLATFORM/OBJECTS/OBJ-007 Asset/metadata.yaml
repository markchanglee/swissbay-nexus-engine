# ==========================================================
# Swissbay Nexus
# Business Object Metadata
# ==========================================================

object:
  id: OBJ-007
  code: ASSET
  name: Asset
  plural: Assets
  version: 1.0.0
  status: Draft

ownership:
  business_owner: Asset Management
  technical_owner: Swissbay Architecture
  governance_owner: Nexus Governance Board

classification:
  object_type: Master Business Object
  domain: Enterprise Asset Management
  criticality: Critical
  confidentiality: Internal
  lifecycle: Active

description:
  summary: >
    Represents every governed physical, digital and
    intangible asset managed within Swissbay Nexus.

  purpose: >
    Establish a canonical representation of enterprise
    assets throughout their lifecycle including
    acquisition, operation, maintenance and disposal.

relationships:

  parents: []

  children: []

  references:
    - OBJ-001 Customer
    - OBJ-002 Supplier
    - OBJ-003 Product
    - OBJ-004 Employee
    - OBJ-005 Contract
    - OBJ-006 Project
    - OBJ-008 Warehouse
    - OBJ-009 Opportunity
    - OBJ-010 SalesOrder

    - DATA-000
    - VALID-000
    - SEC-000
    - AI-000
    - AUTO-000
    - WF-000

departments:

  owner:
    - Asset Management

  contributors:
    - Operations
    - Engineering
    - Information Technology
    - Finance
    - Procurement
    - Facilities Management

  consumers:
    - Executive
    - Asset Managers
    - Operations
    - Finance
    - Maintenance
    - AI Agents

ai:

  enabled: true

  capabilities:

    - Predictive Maintenance
    - Asset Health Analysis
    - Lifecycle Forecasting
    - Asset Optimisation
    - Depreciation Forecasting
    - Asset Recommendations
    - Utilisation Analysis

security:

  classification: Internal

workflow:

  primary:

    - Asset Registration
    - Asset Assignment
    - Maintenance
    - Asset Transfer
    - Asset Retirement
    - Asset Disposal

dashboards:

  - Asset Dashboard
  - Maintenance Dashboard
  - Executive Asset Dashboard
  - Asset Health Dashboard

kpis:

  - Asset Utilisation
  - Asset Availability
  - Maintenance Compliance
  - Mean Time Between Failures
  - Asset Health Score

automation:

  enabled: true

validation:

  required_fields:

    - Asset ID
    - Asset Name
    - Asset Type
    - Asset Status
    - Asset Owner
    - Current Location

documentation:

  readme: README.md

  sections: sections/

history:

  created: 2026-06-30

  created_by: Swissbay Architecture Team

  last_updated: 2026-06-30

  change_log: CHANGELOG.md

  decision_log: DECISION_LOG.md