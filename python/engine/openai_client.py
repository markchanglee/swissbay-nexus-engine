import os
from openai import OpenAI

def generate_markdown(prompt: str, model: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(
        model=model,
        input=prompt
    )
    return response.output_text
