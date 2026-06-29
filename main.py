import requests
import os

from dotenv import load_dotenv

from tools import search_book
from prompts import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = os.getenv("MODEL")

URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("📚 Book Agent Started")
print("Type exit to quit")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    # Tool Trigger
    if user_input.lower().startswith("search"):

        book_name = user_input.replace("search", "").strip()

        books = search_book(book_name)

        print("\nTop Results:\n")

        for idx, book in enumerate(books, start=1):

            print(f"{idx}. {book['title']}")
            print(f"   Author: {', '.join(book['authors'])}")
            print(f"   Rating: {book['rating']}")
            print()

        continue

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload
    )

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    print("\n📚 BookGPT:")
    print(answer)