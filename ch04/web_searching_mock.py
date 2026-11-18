from typing import List

def web_search(web_query: str, num_results: int) -> List[str]:
    sample_results = [
        "https://en.wikipedia.org/wiki/Michael_Jordan",
        "https://www.nba.com/player/893/michael-jordan",
        "https://www.britannica.com/biography/Michael-Jordan"
    ]
    return sample_results[:num_results]