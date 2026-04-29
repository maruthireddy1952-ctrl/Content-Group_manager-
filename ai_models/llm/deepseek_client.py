import ollama
import json
from config.settings import OLLAMA_MODEL


def analyze_transcript(text):

    prompt = f"""
You are an AI that analyzes YouTube videos.

Return ONLY raw JSON.
NO markdown.
NO ```.
NO explanation.

Format:
{{
  "topic": "...",
  "category": "...",
  "keywords": ["..."],
  "trend_score": 1-10
}}

Transcript:
{text[:4000]}
"""

    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=prompt
    )
    print(response["response"])
    content = response["response"]

    try:
        return json.loads(content)

    except:
        return {
            "topic": "unknown",
            "category": "unknown",
            "keywords": [],
            "trend_score": 0
        }