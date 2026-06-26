from pathlib import Path
from datetime import date
from .config_loader import load_yaml

def _find_object(target: str, registry: dict) -> dict | None:
    business_objects = registry.get("business_objects", {}) or {}
    if target in business_objects:
        obj = dict(business_objects[target])
        obj["_key"] = target
        return obj
    return None

def _as_yaml_list(values) -> str:
    if not values:
        return "[]"
    lines = []
    for value in values:
        lines.append(f"  - {value}")
    return "\n".join(lines)

def _build_object_markdown(target: str, obj: dict) -> str:
    title = obj.get("name", target.replace("_", " "))
    object_id = obj.get("id", "-")
    owner = obj.get("owner", "-")
    status = obj.get("status", "draft")
    version = obj.get("version", "0.1.0")
    depends_on = obj.get("depends_on", []) or []
    today = date.today().isoformat()

    return f'''---
id: {object_id}
type: business_object
name: {title}
key: {target}
status: {status}
version: {version}
owner: {owner}
depends_on:
{_as_yaml_list(depends_on)}
created: {today}
last_updated: {today}
---

# {title}

## Purpose

Define the `{title}` business object inside Swissbay Nexus.

## Business Value

This object creates a shared definition so Sales, Procurement, Finance, Marketing, Customer Success, AI Agents, and Dashboards all refer to the same concept.

## Owner

{owner}

## Inputs

- To be defined.
- Source systems may include CRM, Excel, Sage, Email, WhatsApp, Obsidian, website forms, and meeting notes.

## Outputs

- To be defined.
- This object should support workflows, reports, dashboards, AI agents, and operational decisions.

## Core Fields

| Field | Description | Required |
|---|---|---|
| ID | Unique object identifier | Yes |
| Name | Human-readable name | Yes |
| Status | Current lifecycle status | Yes |
| Owner | Responsible department or person | Yes |
| Notes | Operational notes | No |

## Relationships

Depends on:

{chr(10).join(f"- {dep}" for dep in depends_on) if depends_on else "- None"}

## Workflow Usage

This object may be used by workflows that need a consistent definition of `{title}`.

## AI Support

AI agents should use this object as the source of truth when reasoning about `{title}`.

## Related Documents

- [[Business_Object_Standard]]
- [[Nexus_File_Standard]]
- [[Swissbay_Nexus_Project_Context]]

## Future Improvements

- Add Swissbay-specific fields.
- Add workflow examples.
- Add validation rules.
- Add dashboard usage.
- Add AI agent usage.

## Version History

| Version | Date | Change |
|---|---|---|
| {version} | {today} | Initial object created by Nexus Object Builder |
'''

def run_create(target: str, registry_path="config/registry.yaml") -> int:
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

    if path.exists():
        print()
        print(f"[SKIP] File already exists: {path}")
        print("Object Builder will not overwrite existing files.")
        return 0

    markdown = _build_object_markdown(target, obj)
    path.write_text(markdown, encoding="utf-8")

    print()
    print(f"[OK] Created object file: {path}")
    return 0
