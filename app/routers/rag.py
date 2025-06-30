from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag_pipeline import ask_question

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_endpoint(request: AskRequest):
    try:
        answer = ask_question(request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))