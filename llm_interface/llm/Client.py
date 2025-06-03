import os
from openai import OpenAI
from ..config import OPENAI_API_KEY


class LLMClient:
    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key not set in environment.")
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt, max_tokens=150):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0
        )
        content = response.choices[0].message.content
        return content.strip() if content is not None else ""
