from fastapi import APIRouter
from app.services.retrieval_service import retrieve_relevant_chunks
from app.models.schemas import QuestionRequest
from app.services.llm_service import generate_ai_response

router = APIRouter()

@router.post("/ask-questions")
def ask_questions(query : QuestionRequest):
    try:
        results =  retrieve_relevant_chunks(query.query)
        print(results)
        context_parts = []

        for result in results:
            context_parts.append(
                f"""
                Content: {result.page_content}
                Page: {result.metadata["page"]}
                Source: {result.metadata["source"]}
                """
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
            You are a helpful assistant. Please answer the question ONLY from the provided context.

            Context: 
            {context}

            Question: 
            ${query.query}

            If you don't find the answer in the given context the please say: 
            I'm sorry, I do not have enough knowledge.
        """

        print("prompt", prompt)

        response = generate_ai_response(prompt)

        return {
            "success": True,
            "result": response
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err)
    }