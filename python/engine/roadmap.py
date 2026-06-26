from pathlib import Path
from .config_loader import load_yaml

ORDERED_SECTIONS = [
    ("business_objects", "Business Objects"),
    ("departments", "Departments"),
    ("ai_agents", "AI Agents"),
    ("workflows", "Workflows"),
    ("dashboards", "Dashboards"),
    ("standards", "Standards"),
]

STATUS_ORDER = {
    "active": 0,
    "approved": 1,
    "ready_for_test": 2,
    "building": 3,
    "planned": 4,
    "backlog": 5,
    "draft": 6,
    "unknown": 7,
}

def _status_rank(status):
    return STATUS_ORDER.get(str(status).lower(), 99)

def _collect_items(registry):
    items = []
    for section_key, section_label in ORDERED_SECTIONS:
        section = registry.get(section_key, {}) or {}
        for key, item in section.items():
            items.append({
                "section": section_label,
                "key": key,
                "id": item.get("id", "-"),
                "name": item.get("name", key),
                "status": item.get("status", "unknown"),
                "version": item.get("version", "-"),
                "owner": item.get("owner", "-"),
            })
    return items

def run_roadmap(registry_path="config/registry.yaml"):
    path = Path(registry_path)

    print("NEXUS ROADMAP")
    print("=============")

    if not path.exists():
        print()
        print(f"[FAIL] Registry file missing: {path}")
        return 1

    registry = load_yaml(path)
    project = registry.get("project", {})

    print()
    print(f"Project : {project.get('name', 'Unknown')}")
    print(f"Version : {project.get('version', '-')}")
    print(f"Status  : {project.get('status', '-')}")
    print()

    items = _collect_items(registry)

    if not items:
        print("No roadmap items found.")
        return 0

    total = len(items)
    done_statuses = {"active", "approved", "done", "completed"}
    done = sum(1 for i in items if str(i["status"]).lower() in done_statuses)
    progress = round((done / total) * 100, 1) if total else 0

    print("Progress")
    print("--------")
    print(f"Items tracked : {total}")
    print(f"Completed     : {done}")
    print(f"Progress      : {progress}%")
    print()

    print("Next Planned Items")
    print("------------------")
    planned = [
        i for i in items
        if str(i["status"]).lower() in {"planned", "backlog", "draft", "building", "ready_for_test"}
    ]
    planned.sort(key=lambda x: (_status_rank(x["status"]), x["version"], x["id"]))

    if not planned:
        print("(none)")
    else:
        for item in planned[:10]:
            print(
                f"{item['id']:<10} {item['name']:<35} "
                f"{item['status']:<15} v{item['version']:<8} {item['section']}"
            )

    print()
    print("By Section")
    print("----------")
    for section_key, section_label in ORDERED_SECTIONS:
        section_items = [i for i in items if i["section"] == section_label]
        if not section_items:
            continue
        section_done = sum(1 for i in section_items if str(i["status"]).lower() in done_statuses)
        print(f"{section_label:<18}: {section_done}/{len(section_items)} completed")

    print()
    print("Roadmap Loaded Successfully")
    return 0
