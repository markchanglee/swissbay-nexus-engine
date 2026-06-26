from pathlib import Path

def read_text_if_exists(path: str | Path) -> str:
    path = Path(path)
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8")
    return ""

def read_folder_markdown(folder: str | Path) -> str:
    folder = Path(folder)
    if not folder.exists() or not folder.is_dir():
        return ""
    chunks = []
    for file in sorted(folder.rglob("*.md")):
        chunks.append(f"\n\n# FILE: {file}\n" + file.read_text(encoding="utf-8"))
    return "\n".join(chunks)

def ensure_dir(path: str | Path) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)
