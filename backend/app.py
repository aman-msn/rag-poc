# backend/app.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from backend.rag_pipeline import query_rag_system

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(payload: QueryRequest):
    response, _ = query_rag_system(payload.question)
    return {"answer": response}
