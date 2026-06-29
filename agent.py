import os
import requests
from dotenv import load_dotenv

from tools import search_books
from planner import decide_action

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b:free")


def run_agent(user_query, start_index=0):

    # Check API Key
    if not API_KEY:
        raise Exception(
            "OPENROUTER_API_KEY not found. "
            "Add it to .env (local) or Streamlit Secrets (cloud)."
        )

    # Decide action
    action = decide_action(user_query)

    # Search books
    total, books = search_books(user_query, start_index)

    # Convert books into text
    book_text = "\n".join(
        [
            f"{b['title']} - {b['author']}"
            for b in books
        ]
    )

    # Prompt
    prompt = f"""
You are an Agentic AI Book Mentor.

You are NOT allowed to answer directly.

You are given tool output.

ACTION:
{action}

USER QUERY:
{user_query}

BOOK DATA:
{book_text}

TOTAL BOOKS FOUND:
{total}

Tasks:
1. Analyze the books.
2. Rank the best recommendations.
3. Suggest a learning path if needed.
4. Explain your reasoning.
5. Keep the answer concise and friendly.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://book-search-agent.streamlit.app",
        "X-Title": "Book Search Agent"
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

    # Parse JSON safely
    try:
        result = response.json()
    except Exception:
        raise Exception(
            f"Invalid response from OpenRouter.\n"
            f"Status Code: {response.status_code}\n"
            f"Response: {response.text}"
        )

    # Print response in Streamlit logs
    print(result)

    # Handle API errors
    if response.status_code != 200:
        raise Exception(
            result.get("error", {}).get(
                "message",
                f"HTTP Error {response.status_code}"
            )
        )

    if "error" in result:
        raise Exception(result["error"]["message"])

    if "choices" not in result:
        raise Exception(f"Unexpected API response: {result}")

    answer = result["choices"][0]["message"]["content"]

    return total, books, answer