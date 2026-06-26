from pathlib import Path

def validate_markdown_text(text: str, required_sections: list[str]) -> list[str]:
    missing = []
    for section in required_sections:
        if f"## {section}" not in text and f"# {section}" not in text:
            missing.append(section)
    return missing

def validate_markdown_file(path: str | Path, required_sections: list[str]) -> list[str]:
    text = Path(path).read_text(encoding="utf-8")
    return validate_markdown_text(text, required_sections)
