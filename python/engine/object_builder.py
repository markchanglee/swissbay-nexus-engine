from pathlib import Path
from datetime import date
from .config_loader import load_yaml

OBJECT_SECTIONS = [
    "Purpose",
    "Business Value",
    "Owner",
    "Inputs",
    "Outputs",
    "Core Fields",
    "Relationships",
    "Workflow Usage",
    "AI Support",
    "Related Documents",
    "Future Improvements",
    "Version History",
]

def _find_object(target: str, registry: dict) -> dict | None:
    business_objects = registry.get("business_objects", {}) or {}
    if target in business_objects:
        obj = dict(business_objects[target])
        obj["_key"] = target
        return obj
    return None

def _yaml_list(values, indent: int = 2) -> str:
    spaces = " " * indent
    if not values:
        return f"{spaces}[]"
    return "\n".join(f"{spaces}- {value}" for value in values)

def _slug(value: str) -> str:
    return value.lower().replace(" ", "_").replace("-", "_")

def _build_frontmatter(target: str, obj: dict) -> str:
    today = date.today().isoformat()
    depends_on = obj.get("depends_on", []) or []
    related_departments = obj.get("related_departments", []) or []
    related_agents = obj.get("related_agents", []) or []
    tags = obj.get("tags", ["business-object", "nexus"])

    return f'''---
id: {obj.get("id", "-")}
key: {target}
name: {obj.get("name", target.replace("_", " "))}
type: {obj.get("type", "business_object")}
object_type: business_object
status: {obj.get("status", "draft")}
lifecycle_stage: draft
version: {obj.get("version", "0.1.0")}
owner: {obj.get("owner", "-")}
source_registry: config/registry.yaml
output_path: {obj.get("output_path", "-")}
created: {today}
last_updated: {today}
review_status: not_reviewed
approval_status: pending
depends_on:
{_yaml_list(depends_on)}
related_departments:
{_yaml_list(related_departments)}
related_ai_agents:
{_yaml_list(related_agents)}
tags:
{_yaml_list(tags)}
---
'''

def _relationships_text(depends_on: list[str]) -> str:
    if not depends_on:
        return "- None listed in registry."
    return "\n".join(f"- [[{dep}]]" for dep in depends_on)

def _related_documents_text(target: str, obj: dict) -> str:
    docs = [
        "[[Business_Object_Standard]]",
        "[[Nexus_File_Standard]]",
        "[[Swissbay_Nexus_Project_Context]]",
        "[[MASTER_BUILD_INDEX]]",
    ]

    for dep in obj.get("depends_on", []) or []:
        docs.append(f"[[{dep}]]")

    seen = []
    for doc in docs:
        if doc not in seen:
            seen.append(doc)

    return "\n".join(f"- {doc}" for doc in seen)

def _build_object_markdown(target: str, obj: dict) -> str:
    title = obj.get("name", target.replace("_", " "))
    owner = obj.get("owner", "-")
    version = obj.get("version", "0.1.0")
    today = date.today().isoformat()
    depends_on = obj.get("depends_on", []) or []

    frontmatter = _build_frontmatter(target, obj)

    body = f'''
# {title}

## Purpose

Define the `{title}` business object inside Swissbay Nexus.

This file exists so every Swissbay department uses the same definition when referring to `{title}`.

## Business Value

A consistent `{title}` object helps Swissbay reduce confusion, improve reporting, support AI agents, and prevent duplicated definitions across departments.

## Owner

{owner}

## Inputs

Potential input sources:

- CRM records
- Excel files
- Sage records
- Email conversations
- WhatsApp notes
- Website forms
- Meeting notes
- Knowledge Inbox entries
- Manual updates from team members

## Outputs

This object should support:

- Operational workflows
- Dashboards
- AI prompts
- Customer or supplier records
- Reporting
- Decision-making
- Department playbooks

## Core Fields

| Field | Description | Required |
|---|---|---|
| id | Unique Nexus identifier | Yes |
| name | Human-readable object name | Yes |
| status | Current lifecycle status | Yes |
| owner | Responsible role or department | Yes |
| source_registry | Registry source file | Yes |
| output_path | Approved vault location | Yes |
| created | Date object file was created | Yes |
| last_updated | Last update date | Yes |
| notes | Operational notes | No |

## Relationships

This object depends on:

{_relationships_text(depends_on)}

## Workflow Usage

This object may be used by any workflow that needs a consistent definition of `{title}`.

Future workflows should reference this object rather than creating duplicate definitions.

## AI Support

AI agents should use this file as the source of truth when reasoning about `{title}`.

AI agents should not invent fields or statuses that conflict with this object.

## Related Documents

{_related_documents_text(target, obj)}

## Future Improvements

- Add Swissbay-specific fields.
- Add lifecycle statuses.
- Add workflow examples.
- Add validation rules.
- Add dashboard usage.
- Add AI agent usage.
- Add real examples from Swissbay operations.

## Version History

| Version | Date | Change |
|---|---|---|
| {version} | {today} | Initial object created by Nexus Object Builder |
'''
    return frontmatter + "\n" + body.strip() + "\n"

def run_create(target: str, registry_path="config/registry.yaml", force: bool = False) -> int:
    print("NEXUS OBJECT BUILDER")
    print("====================")
    print()
    print(f"Target: {target}")

    registry_file = Path(registry_path)
    if not registry_file.exists():
        print()
        print(f"[FAIL] Registry file missing: {registry_file}")
        return 1

    registry = load_yaml(registry_file)
    obj = _find_object(target, registry)

    if not obj:
        print()
        print(f"[FAIL] Business object not found in registry: {target}")
        return 1

    output_path = obj.get("output_path")
    if not output_path:
        print()
        print(f"[FAIL] output_path missing for {target} in registry.")
        return 1

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists() and not force:
        print()
        print(f"[SKIP] File already exists: {path}")
        print("Object Builder will not overwrite existing files unless --force is used.")
        return 0

    markdown = _build_object_markdown(target, obj)
    path.write_text(markdown, encoding="utf-8")

    print()
    print(f"[OK] Created object file: {path}")
    if force:
        print("[INFO] Existing file was overwritten because --force was used.")
    return 0
