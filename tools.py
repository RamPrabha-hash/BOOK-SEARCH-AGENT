import requests

def search_books(query, start_index=0):

    url = "https://www.googleapis.com/books/v1/volumes"

    params = {
        "q": query,
        "startIndex": start_index,
        "maxResults": 10
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    total = data.get("totalItems", 0)

    books = []

    for item in data.get("items", []):

        info = item.get("volumeInfo", {})

        books.append({
            "title": info.get("title", "Unknown"),
            "author": ", ".join(
                info.get("authors", ["Unknown"])
            )
        })

    return total, books