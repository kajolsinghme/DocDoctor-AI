from fastapi import APIRouter
from app.services.retrieval_service import retrieve_relevant_chunks
from app.models.schemas import QuestionRequest
from app.services.llm_service import generate_ai_response

router = APIRouter()

@router.post("/ask-questions")
def ask_questions(query : QuestionRequest):
    try:
        results =  retrieve_relevant_chunks(query.query)
        print("RESULTS")
        for r in results:
            print(r.metadata)
        unique_sources = set()
        context_parts = []

        for result in results:
            unique_sources.add((
               result.metadata["page"],
                result.metadata["source"]
            ))
           
            context_parts.append(
                f"""
                Content: {result.page_content} 
                Page: {result.metadata["page"]}
                Source: {result.metadata["source"]}
                """
            )

        context = "\n\n".join(context_parts)

        sources = [
            {
                "source": source,
                "page": page
            }
            for source, page in unique_sources
        ]

        prompt = f"""
            You are DocDoctor AI, a helpful assistant that answers questions based on uploaded documents.
            If the user greets you, asks who you are, or asks what you can do, respond naturally as DocDoctor AI and explain that you help users understand and ask questions about their uploaded documents.
            Answer based on the provided context.   
            Answer based on the provided context.
            Answer using plain text only.
            You may make reasonable inferences when strongly supported by the context.

            For example:
            - If tools such as Lucidchart or Draw.io are mentioned, it is reasonable to infer experience creating diagrams and flows.
            - If a programming language is listed as familiar, it is reasonable to infer basic working knowledge.

            Clearly distinguish facts from inferences.

            If the answer cannot be determined or reasonably inferred from the context, say:
            "I'm sorry, I do not have enough information."
            Do not use:
            - Markdown
            - Bullet points
            - Asterisks (*)
            - Headings
            - Numbered lists

            Provide a concise natural-language answer.

            Context:
            {context}

            Question:
            {query.query}
        """


        response = generate_ai_response(prompt)

        return {
            "success": True,
            "result": response,
            "sources": sources
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err)
    }