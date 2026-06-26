from pathlib import Path
from .config_loader import load_yaml
from .markdown_validator import validate_markdown_file

DEFAULT_SCAN_PATHS = ["vault", "outputs"]

def _get_required_sections(config: dict) -> list[str]:
    return config.get("markdown_standard", {}).get("required_sections", [])

def _iter_markdown_files(scan_paths: list[str]):
    for scan_path in scan_paths:
        path = Path(scan_path)
        if not path.exists():
            continue

        if path.is_file() and path.suffix.lower() == ".md":
            yield path
            continue

        if path.is_dir():
            for file in sorted(path.rglob("*.md")):
                yield file

def run_validate(config_path="config/config.yaml", scan_paths=None):
    print("NEXUS VALIDATE")
    print("==============")

    config_file = Path(config_path)
    if not config_file.exists():
        print()
        print(f"[FAIL] Config file missing: {config_file}")
        return 1

    config = load_yaml(config_file)
    required_sections = _get_required_sections(config)

    if not required_sections:
        print()
        print("[FAIL] No required sections found in config/config.yaml")
        return 1

    scan_paths = scan_paths or DEFAULT_SCAN_PATHS
    files = list(_iter_markdown_files(scan_paths))

    print()
    print("Scan Paths")
    print("----------")
    for path in scan_paths:
        print(f"- {path}")

    print()
    print(f"Markdown files found: {len(files)}")

    if not files:
        print()
        print("No markdown files found.")
        return 0

    failures = []
    passed = 0

    print()
    print("Validation Results")
    print("------------------")

    for file in files:
        missing = validate_markdown_file(file, required_sections)
        if missing:
            failures.append((file, missing))
            print(f"[WARN] {file} missing: {', '.join(missing)}")
        else:
            passed += 1
            print(f"[OK]   {file}")

    print()
    print("Summary")
    print("-------")
    print(f"Checked : {len(files)}")
    print(f"Passed  : {passed}")
    print(f"Warnings: {len(failures)}")

    if failures:
        print()
        print("Status: VALIDATION WARNINGS")
        print("Note: Warnings do not block the engine yet. They show which files need review.")
        return 0

    print()
    print("Status: VALIDATION PASSED")
    return 0
