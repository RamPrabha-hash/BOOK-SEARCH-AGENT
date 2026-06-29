def decide_action(user_query):

    query = user_query.lower()

    if "roadmap" in query:
        return "roadmap"

    elif "compare" in query:
        return "compare"

    else:
        return "recommend"