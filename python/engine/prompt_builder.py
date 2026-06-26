from pathlib import Path

def build_prompt(target: str, prompt_file: str, context: str) -> str:
    prompt = Path(prompt_file).read_text(encoding="utf-8")
    return f'''
You are working inside Swissbay Nexus.

TARGET:
{target}

PROJECT CONTEXT:
{context}

TASK PROMPT:
{prompt}
'''.strip()
