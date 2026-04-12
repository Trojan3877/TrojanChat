# Architecture Overview

User → Frontend (Next.js)
     → FastAPI Backend
     → LangGraph AI Pipeline
        → Qdrant Vector DB
        → Cohere Embeddings
        → Groq LLM
     → Response