from pathlib import Path
from datetime import date
from .config_loader import load_yaml
from .context_loader import load_context
from .openai_client import generate_markdown

BUSINESS_OBJECTS_INDEX = Path("vault/03_BUSINESS_OBJECTS/00_Business_Objects_Index.md")

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

def _obsidian_label(value: str) -> str:
    return str(value).replace("_", " ")

def _obsidian_link(value: str) -> str:
    return f"[[{value}|{_obsidian_label(value)}]]"

def _section_links(values) -> str:
    if not values:
        return "- None listed."
    return "\n".join(f"- {_obsidian_link(value)}" for value in values)

def _build_frontmatter(target: str, obj: dict) -> str:
    today = date.today().isoformat()
    depends_on = obj.get("depends_on", []) or []
    related_departments = obj.get("related_departments", []) or []
    related_agents = obj.get("related_agents", []) or []
    tags = obj.get("tags", ["business-object", "nexus"])
    return f"""---
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
"""

def _related_documents_text(obj: dict) -> str:
    docs = [
        "Business_Object_Standard",
        "Nexus_File_Standard",
        "Swissbay_Nexus_Project_Context",
        "MASTER_BUILD_INDEX",
        "00_Business_Objects_Index",
    ]
    for dep in obj.get("depends_on", []) or []:
        docs.append(dep)
    seen = []
    for doc in docs:
        if doc not in seen:
            seen.append(doc)
    return "\n".join(f"- {_obsidian_link(doc)}" for doc in seen)

def _build_template_object_markdown(target: str, obj: dict) -> str:
    title = obj.get("name", target.replace("_", " "))
    owner = obj.get("owner", "-")
    version = obj.get("version", "0.1.0")
    today = date.today().isoformat()
    depends_on = obj.get("depends_on", []) or []
    related_departments = obj.get("related_departments", []) or []
    related_agents = obj.get("related_agents", []) or []
    body = f"""
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

### Depends On

{_section_links(depends_on)}

### Related Departments

{_section_links(related_departments)}

### Related AI Agents

{_section_links(related_agents)}

## Workflow Usage

This object may be used by any workflow that needs a consistent definition of `{title}`.

Future workflows should reference this object rather than creating duplicate definitions.

## AI Support

AI agents should use this file as the source of truth when reasoning about `{title}`.

AI agents should not invent fields or statuses that conflict with this object.

## Related Documents

{_related_documents_text(obj)}

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
| {version} | {today} | Object updated by Nexus Object Builder |
"""
    return _build_frontmatter(target, obj) + "\n" + body.strip() + "\n"

def _build_ai_prompt(target: str, obj: dict, context: str) -> str:
    title = obj.get("name", target.replace("_", " "))
    frontmatter = _build_frontmatter(target, obj)
    return f"""
You are the Chief Architect of Swissbay Nexus.

Create a production-quality Markdown file for this Business Object:

Object: {title}
Target key: {target}

Registry metadata:
{obj}

Context:
{context}

Use this exact frontmatter at the top:
{frontmatter}

Requirements:
- Make the document specific to Swissbay.
- Swissbay is a Gauteng-based B2B operational procurement company.
- Current categories include PPE, cleaning chemicals, toilet paper, cleaning supplies, hygiene products, and coffee cups.
- Current customer types include schools, food manufacturers, and corporate facilities.
- Do not write generic CRM theory.
- Include these exact headings:
  ## Purpose
  ## Business Value
  ## Owner
  ## Inputs
  ## Outputs
  ## Core Fields
  ## Relationships
  ## Workflow Usage
  ## AI Support
  ## Related Documents
  ## Future Improvements
  ## Version History
- Use Obsidian-style links where useful.
- Return Markdown only.
""".strip()

def _build_ai_object_markdown(target: str, obj: dict, config: dict, context_registry: dict) -> str:
    model = config.get("ai", {}).get("default_model", "gpt-5.5")
    context = load_context(target, context_registry)
    prompt = _build_ai_prompt(target, obj, context)
    return generate_markdown(prompt, model)

def _write_business_object_index(registry: dict) -> None:
    BUSINESS_OBJECTS_INDEX.parent.mkdir(parents=True, exist_ok=True)
    business_objects = registry.get("business_objects", {}) or {}
    lines = [
        "---",
        "type: index",
        "section: business_objects",
        "status: active",
        "---",
        "",
        "# Business Objects Index",
        "",
        "## Purpose",
        "",
        "This index lists the Business Objects currently registered in Nexus.",
        "",
        "## Registered Business Objects",
        "",
        "| ID | Object | Status | Owner | Output Path |",
        "|---|---|---|---|---|",
    ]
    for key, obj in business_objects.items():
        lines.append(
            f"| {obj.get('id','-')} | [[{key}|{obj.get('name', key)}]] | {obj.get('status','-')} | {obj.get('owner','-')} | `{obj.get('output_path','-')}` |"
        )
    lines.extend(["", "## Related Documents", "", "- [[Business_Object_Standard]]", "- [[Nexus_File_Standard]]", "- [[MASTER_BUILD_INDEX]]"])
    BUSINESS_OBJECTS_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")

def run_create(
    target: str,
    registry_path="config/registry.yaml",
    force: bool = False,
    update_index: bool = True,
    use_ai: bool = False,
    config_path="config/config.yaml",
    context_registry_path="config/context_registry.yaml",
) -> int:
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
        if update_index:
            _write_business_object_index(registry)
            print(f"[OK] Updated index: {BUSINESS_OBJECTS_INDEX}")
        return 0

    if use_ai:
        print("[INFO] AI assisted build enabled.")
        config = load_yaml(config_path)
        context_registry = load_yaml(context_registry_path)
        markdown = _build_ai_object_markdown(target, obj, config, context_registry)
    else:
        markdown = _build_template_object_markdown(target, obj)

    path.write_text(markdown, encoding="utf-8")

    print()
    print(f"[OK] Created object file: {path}")
    if force:
        print("[INFO] Existing file was overwritten because --force was used.")
    if use_ai:
        print("[INFO] Content was generated using AI assistance.")

    if update_index:
        _write_business_object_index(registry)
        print(f"[OK] Updated index: {BUSINESS_OBJECTS_INDEX}")
    return 0
