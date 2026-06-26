from pathlib import Path
from python.engine.markdown_validator import validate_markdown_file
from python.engine.config_loader import load_yaml

config = load_yaml("config/config.yaml")
registry = load_yaml("config/context_registry.yaml")
required = config["markdown_standard"]["required_sections"]

for file in Path("outputs").glob("*.md"):
    missing = validate_markdown_file(file, required)
    if missing:
        print(f"{file}: missing {missing}")
    else:
        print(f"{file}: OK")
