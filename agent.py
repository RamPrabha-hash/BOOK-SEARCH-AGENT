import os
import requests
from dotenv import load_dotenv

from tools import search_books
from planner import decide_action

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b:free")


def run_agent(user_query, start_index=0):

    action = decide_action(user_query)

    total, books = search_books(user_query, start_index)

    book_text = "\n".join(
        [
            f"{b['title']} - {b['author']}"
            for b in books
        ]
    )

    prompt = f"""
You are an Agentic AI Book Mentor.

You are NOT allowed to answer directly.

You are given tools output.

ACTION: {action}

USER QUERY: {user_query}

BOOK DATA:
{book_text}

TOTAL BOOKS FOUND: {total}

Tasks:
1. Analyze books
2. Rank best ones
3. Suggest learning path if needed
4. Explain reasoning clearly
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    return total, books, answer