from pathlib import Path
from .config_loader import load_yaml

SECTION_LABELS = {
    "business_objects": "Business Objects",
    "departments": "Departments",
    "ai_agents": "AI Agents",
    "workflows": "Workflows",
    "dashboards": "Dashboards",
    "standards": "Standards",
}

def _safe_get(item, key, default=""):
    value = item.get(key, default)
    if value is None:
        return default
    return str(value)

def _print_section(title, items):
    print()
    print(title)
    print("-" * len(title))

    if not items:
        print("(empty)")
        return 0

    for key, item in items.items():
        item_id = _safe_get(item, "id", "-")
        name = _safe_get(item, "name", key)
        status = _safe_get(item, "status", "unknown")
        version = _safe_get(item, "version", "-")
        owner = _safe_get(item, "owner", "-")
        print(f"{item_id:<10} {name:<35} {status:<15} v{version:<8} owner: {owner}")

    return len(items)

def run_registry(registry_path="config/registry.yaml"):
    path = Path(registry_path)

    print("NEXUS REGISTRY")
    print("==============")

    if not path.exists():
        print()
        print(f"[FAIL] Registry file missing: {path}")
        return 1

    registry = load_yaml(path)

    project = registry.get("project", {})
    print()
    print("Project")
    print("-------")
    print(f"Name    : {project.get('name', 'Unknown')}")
    print(f"Version : {project.get('version', '-')}")
    print(f"Status  : {project.get('status', '-')}")
    print(f"Owner   : {project.get('owner', '-')}")

    totals = {}
    for section_key, label in SECTION_LABELS.items():
        count = _print_section(label, registry.get(section_key, {}) or {})
        totals[label] = count

    print()
    print("Statistics")
    print("----------")
    for label, count in totals.items():
        print(f"{label:<18}: {count}")

    print()
    print("Registry Loaded Successfully")
    return 0
