from pathlib import Path
from .file_utils import read_text_if_exists, read_folder_markdown

def load_context(target: str, registry: dict) -> str:
    chunks = []

    global_required = registry.get("global", {}).get("required", [])
    target_cfg = registry.get("targets", {}).get(target, {})
    target_required = target_cfg.get("context", {}).get("required", [])
    target_optional = target_cfg.get("context", {}).get("optional", [])

    for file_path in global_required + target_required:
        text = read_text_if_exists(file_path)
        if text:
            chunks.append(f"\n\n--- CONTEXT FILE: {file_path} ---\n{text}")

    for optional_path in target_optional:
        p = Path(optional_path)
        if p.is_dir():
            text = read_folder_markdown(p)
        else:
            text = read_text_if_exists(p)
        if text:
            chunks.append(f"\n\n--- OPTIONAL CONTEXT: {optional_path} ---\n{text}")

    return "\n".join(chunks)
