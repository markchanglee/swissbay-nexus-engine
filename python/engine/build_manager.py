from pathlib import Path
from .context_loader import load_context
from .prompt_builder import build_prompt
from .openai_client import generate_markdown
from .markdown_validator import validate_markdown_text
from .file_utils import ensure_dir

def build_target(target: str, config: dict, registry: dict) -> Path:
    target_cfg = registry.get("targets", {}).get(target)
    if not target_cfg:
        raise ValueError(f"Unknown target: {target}")

    model = config.get("ai", {}).get("default_model", "gpt-5.5")
    output_dir = Path(config.get("paths", {}).get("outputs", "./outputs"))
    ensure_dir(output_dir)

    context = load_context(target, registry)
    prompt = build_prompt(target, target_cfg["prompt_file"], context)

    markdown = generate_markdown(prompt, model)

    required_sections = target_cfg.get(
        "required_sections",
        config.get("markdown_standard", {}).get("required_sections", [])
    )

    missing = validate_markdown_text(markdown, required_sections)

    output_file = output_dir / target_cfg.get("output_file", f"{target}_DRAFT.md")
    output_file.write_text(markdown, encoding="utf-8")

    validation_file = output_dir / f"{target}_VALIDATION.txt"
    if missing:
        validation_file.write_text(
            "Missing required sections:\n" + "\n".join(missing),
            encoding="utf-8"
        )
    else:
        validation_file.write_text("Validation passed. No missing required sections.", encoding="utf-8")

    return output_file
