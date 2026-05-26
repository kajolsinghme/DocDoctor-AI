from fastapi import APIRouter
from app.services.retrieval_service import retrieve_relevant_chunks
from app.models.schemas import QuestionRequest

router = APIRouter()

@router.post("/ask-questions")
async def ask_questions(query : QuestionRequest):
    try:
        result = await retrieve_relevant_chunks(query.query)
        return {
            "success": True,
            "result": result
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err)
    }