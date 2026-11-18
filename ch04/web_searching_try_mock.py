from web_searching_mock import web_search

result = web_search(
    web_query="How many titles did Michael Jordan win?",
    num_results=5
)

print(result)