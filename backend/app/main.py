from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

# Import routers (we will create these next)
from app.api.chat import router as chat_router

# --------------------------------------------------
# App Initialization
# --------------------------------------------------
app = FastAPI(
    title="TrojanChat 2.0 AI",
    description="AI-powered USC fan chat platform with RAG and real-time insights",
    version="1.0.0"
)

# --------------------------------------------------
# Middleware (CORS for frontend connection)
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------
@app.get("/")
async def root():
    return {
        "message": "TrojanChat 2.0 AI is running 🚀",
        "status": "healthy"
    }

# --------------------------------------------------
# Health Check Endpoint (important for deployment)
# --------------------------------------------------
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "trojanchat-backend"
    }

# --------------------------------------------------
# Simple Latency Test Endpoint (for metrics)
# --------------------------------------------------
@app