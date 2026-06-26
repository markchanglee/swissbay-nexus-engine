from pathlib import Path
import os
import sys
import importlib.util
from dotenv import load_dotenv

def _check_exists(path):
    p = Path(path)
    return p.exists(), str(p)

def _check_import(package):
    return importlib.util.find_spec(package) is not None

def run_doctor():
    load_dotenv()
    checks = []
    checks.append(("Python version", sys.version.split()[0], True))

    required_files = [
        "nexus.py",
        "config/config.yaml",
        "config/context_registry.yaml",
        "config/registry.yaml",
        "requirements.txt",
        ".env",
    ]

    for file_path in required_files:
        exists, display = _check_exists(file_path)
        checks.append((f"File: {display}", "found" if exists else "missing", exists))

    required_folders = [
        "vault",
        "vault/00_CONTEXT",
        "vault/00_INBOX",
        "outputs",
        "prompts",
        "python/engine",
    ]

    for folder_path in required_folders:
        exists, display = _check_exists(folder_path)
        checks.append((f"Folder: {display}", "found" if exists else "missing", exists))

    has_key = bool(os.getenv("OPENAI_API_KEY"))
    checks.append(("OPENAI_API_KEY", "set" if has_key else "missing", has_key))

    packages = ["openai", "dotenv", "yaml", "rich"]
    for package in packages:
        ok = _check_import(package)
        checks.append((f"Package: {package}", "installed" if ok else "missing", ok))

    print("NEXUS DOCTOR")
    print("============")
    print()

    failed = 0
    for name, value, ok in checks:
        icon = "OK" if ok else "FAIL"
        print(f"[{icon}] {name}: {value}")
        if not ok:
            failed += 1

    print()
    if failed == 0:
        print("Status: HEALTHY")
        return 0

    print(f"Status: ATTENTION REQUIRED ({failed} issue(s))")
    print()
    print("Suggested fixes:")
    print("- If .env is missing, copy .env.example to .env and add OPENAI_API_KEY.")
    print("- If packages are missing, run: python -m pip install -r requirements.txt")
    print("- If config files are missing, confirm config/ contains config.yaml, context_registry.yaml, and registry.yaml.")
    return 1
