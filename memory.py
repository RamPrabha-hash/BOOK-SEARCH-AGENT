import json
import os

MEMORY_FILE = "memory.json"

def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {"history": []}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_memory(user_query):

    memory = load_memory()

    memory["history"].append(user_query)

    save_memory(memory)

def get_memory():

    return load_memory()["history"]