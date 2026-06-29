import streamlit as st

from agent import run_agent
from memory import add_memory

st.set_page_config(
    page_title="Agentic Book Mentor",
    page_icon="📚"
)

st.title("📚 Agentic Book Mentor")

query = st.text_input(
    "Enter Topic / Goal",
    placeholder=
    "Python roadmap, AI books, compare books..."
)

if st.button("Run Agent"):

    if query:

        add_memory(query)

        with st.spinner(
            "Agent Thinking..."
        ):

            total, books, response = run_agent(
                query
            )

            st.success(
                f"Total Books Found: {total}"
            )

            st.subheader(
                "Retrieved Books"
            )

            for book in books:

                st.write(
                    f"📘 {book['title']}"
                )

                st.write(
                    f"✍️ {book['author']}"
                )

            st.markdown("---")

            st.subheader(
                "🤖 Agent Analysis"
            )

            st.markdown(response)