# BOOK-SEARCH-AGENT
WEB HOST LINK: https://book-search-agent-en5ezyjnrk4v8niyk6wfgm.streamlit.app/

# 📚 Book Search Agent – AI-Powered Intelligent Book Discovery Assistant

## Overview

The **Book Search Agent** is an AI-powered application that helps users discover books through natural language conversations. Instead of searching with exact titles or author names, users can simply describe what they are looking for—for example, *"I want a beginner-friendly Python book"* or *"Recommend mystery novels similar to Sherlock Holmes"*—and the agent intelligently interprets the request to provide relevant recommendations.

The application combines Large Language Models (LLMs) with real-time book information retrieval to deliver accurate, personalized, and context-aware book suggestions. It follows an agentic AI workflow where the AI reasons about the user's request, decides which tools to use, gathers information, and generates a well-structured response.

---

## Key Features

* 🔍 **Natural Language Book Search**

  * Search for books using conversational queries instead of exact keywords.

* 🤖 **AI-Powered Recommendations**

  * Understands user intent and recommends books based on topics, genres, authors, or reading goals.

* 📖 **Real-Time Book Information**

  * Retrieves live book details including:

    * Title
    * Author
    * Publication Year
    * Description
    * Ratings (when available)
    * Cover Image
    * Publisher
    * ISBN

* 🧠 **Context-Aware Conversations**

  * Maintains conversation history so follow-up questions like *"Recommend another one"* or *"Only beginner books"* are understood without repeating the entire query.

* 🎯 Intelligent Planning

  * The agent analyzes the user's request, determines the required action, invokes the appropriate tools, and produces a concise, relevant response.

* 📊 Structured Results

  * Displays search results in a clean table format, making it easy to compare multiple books.

* 💬 Interactive Chat Interface

  * Built with Streamlit to provide a responsive and user-friendly web interface.

---

## How It Works

1. The user enters a book-related query.
2. The AI agent analyzes the request and identifies the user's intent.
3. A planning module determines the appropriate action.
4. The search tool retrieves book information from an online book database/API.
5. The AI evaluates the retrieved information.
6. Relevant books are organized into a structured table.
7. The final response is displayed in an easy-to-read conversational format.

---

## Technologies Used

* **Python** – Core application development
* **Streamlit** – Interactive web interface
* **OpenRouter API** – Access to Large Language Models
* **Python-dotenv** – Secure API key management
* **Requests** – API communication
* **JSON Memory** – Conversation history storage
* **Agentic AI Workflow** – Planning, reasoning, tool execution, and response generation

---

## Architecture

User Query

↓

AI Agent

↓

Planner

↓

Book Search Tool

↓

Book Database/API

↓

Structured Results

↓

AI Response

↓

Streamlit Interface

---

## Benefits

* Saves users time by eliminating manual searches.
* Provides intelligent recommendations based on user intent.
* Supports conversational interactions rather than keyword-only searches.
* Delivers organized and readable search results.
* Demonstrates modern Agentic AI concepts such as planning, memory, reasoning, and tool usage.

---

## Applications

* Digital Libraries
* Educational Platforms
* Book Recommendation Systems
* Online Bookstores
* Learning Management Systems
* Personal Reading Assistants
* Research and Academic Book Discovery

---

## Future Enhancements

* Personalized recommendations based on reading history.
* User authentication and individual reading profiles.
* Wishlist and favorite book management.
* Integration with Goodreads and Amazon Books.
* Semantic search using vector embeddings.
* Multi-language book recommendations.
* Voice-based search using speech recognition.
* Reading progress tracking and analytics.
* AI-generated book summaries.
* PDF and eBook availability detection.

---

## Conclusion

The **Book Search Agent** showcases how Agentic AI can transform traditional book searching into an intelligent, conversational experience. By integrating Large Language Models, real-time information retrieval, conversational memory, and autonomous decision-making, the system provides users with fast, accurate, and personalized book recommendations through a modern, interactive interface. It demonstrates practical applications of AI agents in information retrieval while offering an intuitive and engaging user experience.
