from tavily import TavilyClient
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

print("Key found:", os.getenv("TAVILY_API_KEY") is not None)

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def web_search(
    web_query: str,
    num_results: int
) -> List[str]:

    print(f"Searching: {web_query}")

    response = client.search(
        query=web_query,
        max_results=num_results
    )

    urls = [
        result["url"]
        for result in response["results"]
    ]

    print(f"Found {len(urls)} URLs")

    return urls