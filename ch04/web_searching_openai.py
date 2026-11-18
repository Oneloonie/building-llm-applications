import os
from typing import List
from openai import OpenAI


def web_search(web_query: str, num_results: int) -> List[str]:
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set.")

        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-4.1",
            tools=[{"type": "web_search_preview"}],
            input=f"Search the web for: {web_query}. Return the top {num_results} result links only."
        )

        links = []

        for item in response.output:
            if hasattr(item, "content"):
                for content_item in item.content:
                    if hasattr(content_item, "text") and content_item.text:
                        lines = content_item.text.splitlines()
                        for line in lines:
                            line = line.strip()
                            if line.startswith("http://") or line.startswith("https://"):
                                links.append(line)

        return links[:num_results]

    except Exception as e:
        print(f"Web search failed: {e}")
        return []
