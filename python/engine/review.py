from pathlib import Path
from datetime import datetime
from .config_loader import load_yaml
from .markdown_validator import validate_markdown_file

def _find_target_metadata(target: str, registry: dict) -> dict | None:
    for section_name in [
        "business_objects",
        "departments",
        "ai_agents",
        "workflows",
        "dashboards",
        "standards",
    ]:
        section = registry.get(section_name, {}) or {}
        if target in section:
            item = dict(section[target])
            item["_section"] = section_name
            item["_key"] = target
            return item
    return None

def _get_draft_path(target: str, metadata: dict | None) -> Path:
    if metadata and metadata.get("draft_path"):
        return Path(metadata["draft_path"])
    return Path("outputs") / f"{target}_DRAFT.md"

def _get_required_sections(target: str, config: dict, context_registry: dict) -> list[str]:
    target_cfg = context_registry.get("targets", {}).get(target, {}) or {}
    if target_cfg.get("required_sections"):
        return target_cfg["required_sections"]
    return config.get("markdown_standard", {}).get("required_sections", [])

def _line_count(text: str) -> int:
    return len(text.splitlines())

def _word_count(text: str) -> int:
    return len(text.split())

def run_review(target: str, config_path="config/config.yaml", registry_path="config/registry.yaml", context_registry_path="config/context_registry.yaml") -> int:
    print("NEXUS REVIEW")
    print("============")
    print()
    print(f"Target: {target}")

    config = load_yaml(config_path)
    registry = load_yaml(registry_path)
    context_registry = load_yaml(context_registry_path)

    metadata = _find_target_metadata(target, registry)
    draft_path = _get_draft_path(target, metadata)

    if not draft_path.exists():
        print()
        print(f"[FAIL] Draft file not found: {draft_path}")
        print()
        print("Build the draft first, for example:")
        print(f"python nexus.py build {target}")
        return 1

    required_sections = _get_required_sections(target, config, context_registry)
    missing = validate_markdown_file(draft_path, required_sections)
    text = draft_path.read_text(encoding="utf-8")

    report_lines = []
    report_lines.append(f"# Nexus Review Report — {target}")
    report_lines.append("")
    report_lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}")
    report_lines.append("")
    report_lines.append("## Target")
    report_lines.append("")
    report_lines.append(f"- Target: `{target}`")
    report_lines.append(f"- Draft: `{draft_path}`")

    if metadata:
        report_lines.append(f"- Registry ID: `{metadata.get('id', '-')}`")
        report_lines.append(f"- Registry Status: `{metadata.get('status', '-')}`")
        report_lines.append(f"- Registry Version: `{metadata.get('version', '-')}`")
        report_lines.append(f"- Owner: `{metadata.get('owner', '-')}`")
        report_lines.append(f"- Output Path: `{metadata.get('output_path', '-')}`")
    else:
        report_lines.append("- Registry: `not found`")

    report_lines.append("")
    report_lines.append("## Document Stats")
    report_lines.append("")
    report_lines.append(f"- Lines: {_line_count(text)}")
    report_lines.append(f"- Words: {_word_count(text)}")
    report_lines.append(f"- Required sections: {len(required_sections)}")
    report_lines.append(f"- Missing sections: {len(missing)}")

    report_lines.append("")
    report_lines.append("## Required Section Check")
    report_lines.append("")
    if missing:
        report_lines.append("Status: `WARNINGS`")
        report_lines.append("")
        report_lines.append("Missing sections:")
        for section in missing:
            report_lines.append(f"- {section}")
    else:
        report_lines.append("Status: `PASSED`")
        report_lines.append("")
        report_lines.append("All required sections are present.")

    report_lines.append("")
    report_lines.append("## Registry Dependency Check")
    report_lines.append("")
    if metadata and metadata.get("depends_on"):
        report_lines.append("Dependencies listed in registry:")
        for dep in metadata.get("depends_on", []):
            report_lines.append(f"- {dep}")
    else:
        report_lines.append("No dependencies listed.")

    report_lines.append("")
    report_lines.append("## Review Decision")
    report_lines.append("")
    report_lines.append("Choose one:")
    report_lines.append("")
    report_lines.append("- APPROVE")
    report_lines.append("- REVISE")
    report_lines.append("- REJECT")
    report_lines.append("")
    report_lines.append("## Notes")
    report_lines.append("")
    report_lines.append("This is an automated structural review. Human business review is still required.")

    output_dir = Path(config.get("paths", {}).get("outputs", "./outputs"))
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / f"{target}_REVIEW.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print()
    print(f"Review report created: {report_path}")
    if missing:
        print(f"Status: WARNINGS ({len(missing)} missing section(s))")
    else:
        print("Status: PASSED")

    return 0
