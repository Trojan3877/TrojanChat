# 🏗️ TrojanChat — System Design Document

## Overview

TrojanChat is a **scalable, production-grade chat platform** designed for high concurrency, real-time communication, and future AI-driven enhancements.

This document outlines the **architecture, data flow, scalability strategy, and deployment design** used to bring TrojanChat to L7-level engineering quality.

---

## 🎯 Design Goals

- Real-time chat with low latency
- Horizontal scalability
- Fault tolerance
- Secure user authentication
- AI/ML extensibility
- Cloud & GPU compatibility (NVIDIA CUDA)
- Clean separation of concerns

---

## 🧱 High-Level Architecture

User
  ↓
Next.js Frontend (Vercel)
  ↓
FastAPI Backend (Render)
  ↓
LangGraph Orchestrator
  ├── Memory lookup
  ├── Retrieval from Qdrant
  ├── Prompt assembly
  ├── Groq LLM response
  └── Langfuse tracing
  ↓
Response returned to UI