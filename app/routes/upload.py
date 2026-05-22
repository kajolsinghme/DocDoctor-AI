from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import upload_pdf_service

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    try:
        result = await upload_pdf_service(pdf_file)
        return {
            "success": True,
            "result": result
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err)
        }