from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.router import agent_router
from app.agent.tool_registry import TOOLS
from app.exceptions import global_exception_handler

class QueryRequest(BaseModel):
    question:str


app = FastAPI(
    title="InfraBot API",
    version="1.0.0"
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

@app.get("/")
def root():
    return {
        "message": "Welcome to InfraBot 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/query")
def query(request:QueryRequest):
    answer=agent_router.route(request.question)
    return {
        "answer":answer
    }


@app.get("/tools")
def get_tools():
    available_tools=[]
    for tool_name ,tool in TOOLS.items():
        available_tools.append({
            "name":tool["name"],
            "description":tool["description"],
        })
    return available_tools
