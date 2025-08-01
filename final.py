from typing import Annotated
from typing import TypedDict
from langgraph.graph.message import add_messages
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph,START,END

import asyncio
load_dotenv()

class RagState(TypedDict):
    messages:Annotated[list,add_messages]
    query: str
    docs_present:bool

def ingestion_agent(state: RagState) -> RagState:
    """Ingestion Agent loads, splits, and embeds documents"""

    print("In the ingestion agent")
    raw_docs = state["messages"][-1].content
    
    docs=CSVLoader(raw_docs).load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splits = splitter.split_documents(docs[:2])

    embeddings=OllamaEmbeddings(model="llama3.2:1b")
    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local("./data/faiss_index")

    state["docs_present"]=False
    return state

def retrieval_agent(state: RagState) -> RagState:
    """Retrieval Agent fetches relevant chunks based on the current query"""
    print("In the retrieval agent")
    query = state["query"]

    # Retrieve top results
    embeddings=OllamaEmbeddings(model="llama3.2:1b")
    vectorstore = FAISS.load_local(
            "./data/faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

    retriever = vectorstore.as_retriever()
    results = retriever.get_relevant_documents(query)
    top_chunks=""
    for r in results[:4]:
        top_chunks += r.page_content 

    state["messages"].append(top_chunks)
    return state

async def main(state:RagState)->RagState:
        client=MultiServerMCPClient(
            {
                "tools":{
                    "url":"http://localhost:8000/mcp",
                    "transport":"streamable_http",
                }
            }
        )

        tools=await client.get_tools()
        llm = ChatGroq(model="llama-3.3-70b-versatile")
        agent=create_react_agent(
            llm,tools
        )
        
        response=await agent.ainvoke(
        {"messages":[{"role":"user","content":f"""Use the following context to answer the query.
                      
        Use the tools only if necessary, else answer using the provided data.
        Context:
        {state["messages"][-1].content}

        Query:
        {state["query"]}

        
        If you use the tools mention the values and the steps that you used to get the answer.
        Answer as helpfully and concisely as possible."""}]}
        )
        state["messages"].append(response["messages"][-1].content)

        return state

async def llm_response_agent(state: RagState) -> RagState:
    """LLMResponseAgent generates an answer using retrieved chunks and user query."""

    print("In the llm agent")
    state=await main(state)
    return state

def choose(state:RagState)->str:
    return state['docs_present']

builder=StateGraph(RagState)

builder.add_node("ingestion",ingestion_agent)
builder.add_node("retriever",retrieval_agent)
builder.add_node("llm",llm_response_agent)

builder.add_conditional_edges(
    START,
    choose,
    {
        True:"ingestion",
        False:"retriever",
    }
)
builder.add_edge("ingestion","retriever")
builder.add_edge("retriever","llm")
builder.add_edge("llm",END)

graph=builder.compile()

# state=asyncio.run(graph.ainvoke({'messages':"snp500_companies_description.csv",'docs_present':True,'query':"what is the debt to equity value of company A"}))

# print(state["messages"][-1].content)