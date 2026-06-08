
---

# 📄 DocDoctor AI

**RAG-Based AI Document Intelligence System**

🔗 Live Demo: [https://doc-doctor-ai.vercel.app/](https://doc-doctor-ai.vercel.app/)

---

## Overview

DocDoctor AI is a full-stack AI system that allows users to upload PDF documents and interact with them using natural language queries.

It uses a Retrieval-Augmented Generation (RAG) pipeline to generate accurate, context-grounded responses with document-level citations.

---

## Features

* Upload PDF documents and chat with their content
* AI-powered question answering using Gemini LLM
* Context-aware responses using RAG architecture
* Source citations (page + document reference)
* Semantic search over vectorized document chunks
* Real-time chat interface
* Clean and responsive UI

---

## How it Works

1. User uploads a PDF
2. Document is split into chunks (LangChain text splitter)
3. Chunks are converted into embeddings (Gemini embeddings)
4. Stored in ChromaDB (vector database)
5. User asks a question
6. Relevant chunks are retrieved using semantic search
7. Gemini LLM generates final answer using retrieved context

---

## Tech Stack

**Frontend:** Next.js, TypeScript, Tailwind CSS, Axios
**Backend:** FastAPI, Python
**AI / LLM:** Gemini API, LangChain
**Vector DB:** ChromaDB
**Architecture:** RAG (Retrieval-Augmented Generation)
**Deployment:** Vercel (Frontend), Render (Backend)

---

## Example

**User:** What is this resume about?
**AI:** This resume belongs to Kajol Singh and describes her experience in Full Stack Development and AI systems.

---

## Highlights

* Built a production-ready full-stack AI application
* Designed and implemented custom RAG pipeline from scratch
* Integrated LLM with semantic retrieval for grounded answers
* Implemented scalable vector search using ChromaDB
* Deployed frontend and backend in production environment

---

## Deployment

* Frontend: Vercel
* Backend: Render

---

## Author

**Kajol Singh**

---

If you want, I can next:

* make this README **more “viral GitHub style” (with badges + UI screenshots section)**
* or optimize it for **recruiter GitHub scanning (very important for placements)**
