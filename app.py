import streamlit as st
import asyncio
import tempfile
import os
from dotenv import load_dotenv
from final import graph  # <-- replace with your file name (without .py extension)

load_dotenv()

st.set_page_config(page_title="RAG Agent", layout="wide")
st.title("Agentic RAG Assistant for finance data")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

# File input for CSV
with st.sidebar:
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
query = st.chat_input("Ask a question about your document")

if query:
    # Save uploaded file locally
    if uploaded_file:
        file_path = f"./{uploaded_file.name}"
        with tempfile.NamedTemporaryFile(delete=False,suffix=".csv") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path=temp_file.name
    else:
        temp_file_path=None

    # Show user query
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Prepare state for LangGraph
    if uploaded_file:
        init_state = {
            "messages": [{"role": "user", "content": temp_file_path}],
            "query": query,
            "docs_present": True
        }
    else:
        init_state = {
            "query": query,
            "docs_present": False
        }

    # Run the LangGraph pipeline
    state = asyncio.run(graph.ainvoke(init_state))

    # Get the assistant's reply
    response = state["messages"][-1].content
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    if uploaded_file:
        os.remove(temp_file_path)
    
