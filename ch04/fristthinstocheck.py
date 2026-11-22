import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print("Key found:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello"}],
    timeout=20
)

print(response.choices[0].message.content)