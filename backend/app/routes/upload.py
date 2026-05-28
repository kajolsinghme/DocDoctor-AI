from fastapi import APIRouter, UploadFile, File
from backend.app.services.pdf_service import upload_pdf_service

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    try:
        await upload_pdf_service(pdf_file)
        return {
            "success": True,
            "result": "PDF uploaded successfully"
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err)
        }