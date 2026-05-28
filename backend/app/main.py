from fastapi import FastAPI
from backend.app.routes.upload import router as upload_router
from backend.app.routes.chat import router as chat_router

app = FastAPI()

app.include_router(upload_router, prefix='/api')

app.include_router(chat_router, prefix='/api')