from typing import List
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


def web_search(web_query: str, num_results: int) -> List[str]:
    try:
        search = DuckDuckGoSearchAPIWrapper()
        results = search.results(web_query, num_results)
        return [r["link"] for r in results]
    except Exception as e:
        print(f"DuckDuckGo search failed: {e}")
        return []