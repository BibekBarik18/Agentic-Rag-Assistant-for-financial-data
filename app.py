import streamlit as st
# import asyncio
import requests
import tempfile
import os
from dotenv import load_dotenv
# from final import graph  

load_dotenv()

config = {"configurable": {"thread_id": "1"}}

st.set_page_config(page_title="RAG Agent", layout="wide")
st.title("Agentic RAG Assistant for finance data")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "config" not in st.session_state:
    st.session_state.config = config

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
            "messages":temp_file_path,
            "query": query,
            "docs_present": True
        }
    else:
        init_state = {
            "messages":"",
            "query": query,
            "docs_present": False
        }

    # Run the LangGraph pipeline
    # state = asyncio.run(graph.ainvoke(init_state,config=st.session_state.config))

    # # Get the assistant's reply
    # response = state["messages"][-1].content

    API_URL="http://127.0.0.1:8001/chat"

    response=requests.post(API_URL,json=init_state)
    # json_data = response.json()
    if response.status_code==200:
        response=response.json()
        st.chat_message("assistant").markdown(response)
    # else:
    #     print(json_data)
    #     st.chat_message("assistant").markdown(json_data)
    st.session_state.messages.append({"role": "assistant", "content": response})
    if uploaded_file:
        os.remove(temp_file_path)
    
