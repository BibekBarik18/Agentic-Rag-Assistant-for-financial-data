from fastapi import FastAPI
from final import graph 
from pydantic import BaseModel
# from final import call_graph
import tempfile
import asyncio

app=FastAPI()

class RagState(BaseModel):
    messages:str
    query:str
    docs_present:bool

@app.post("/chat")
async def root(state:RagState)->str:  
    print(state)
    init_state = {
            "messages":state.messages,
            "query": state.query,
            "docs_present": state.docs_present
        }
    state = await graph.ainvoke(init_state,config={"configurable": {"thread_id": "1"}})
    print("...........")
    print(state)
    print("...........")
    response =state["messages"][-1].content
    return response