# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("📊 Azure SQL + RAG Assistant")
query = st.text_input("Enter your question")

if st.button("Ask"):
    if query.strip() != "":
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": query}
            )
            st.markdown("### 💡 Answer")
            st.write(response.json().get("answer"))
