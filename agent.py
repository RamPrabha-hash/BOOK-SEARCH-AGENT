import os
import requests
from dotenv import load_dotenv

from tools import search_books
from planner import decide_action

# Load environment variables (.env for local)
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b:free")


def run_agent(user_query, start_index=0):

    # Check if API key exists
    if not API_KEY:
        raise Exception(
            "OPENROUTER_API_KEY not found. "
            "For local use, add it to .env. "
            "For Streamlit Cloud, add it under Settings → Secrets."
        )

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

USER QUERY:
{user_query}

BOOK DATA:
{book_text}

TOTAL BOOKS FOUND:
{total}

Tasks:
1. Analyze the books.
2. Rank the best recommendations.
3. Suggest a learning path if applicable.
4. Explain your reasoning clearly.
5. Give the response in a friendly format.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=60
    )

    # Convert response to JSON
    try:
        result = response.json()
    except Exception:
        raise Exception(
            f"Invalid JSON response.\n"
            f"Status Code: {response.status_code}\n"
            f"Response: {response.text}"
        )

    # Print response in logs (useful on Streamlit Cloud)
    print("OpenRouter Response:")
    print(result)

    # HTTP error
    if response.status_code != 200:
        error_msg = result.get("error", {}).get(
            "message",
            f"HTTP {response.status_code}"
        )
        raise Exception(f"OpenRouter API Error: {error_msg}")

    # API returned an error object
    if "error" in result:
        raise Exception(result["error"].get("message", "Unknown API Error"))

    # Missing choices
    if "choices" not in result:
        raise Exception(f"Unexpected API Response:\n{result}")

    # Extract answer
    answer = result["choices"][0]["message"]["content"]

    return total, books, answer