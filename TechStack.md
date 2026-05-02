# 🛠️ TrojanChat – Tech Stack

This document outlines the technologies powering TrojanChat 2.0 AI.

---

## 🖥️ Frontend

| Technology | Purpose |
|---|---|
| Next.js 14 | React framework with App Router |
| TypeScript | Type-safe component development |
| CSS-in-JS (inline styles) | Scoped UI styling |

---

## ⚙️ Backend

| Technology | Purpose |
|---|---|
| FastAPI | Async REST API + WebSocket support |
| Python 3.12 | Runtime |
| Pydantic v2 | Request/response schema validation |
| Uvicorn | ASGI server |

---

## 🧠 AI / ML

| Technology | Purpose |
|---|---|
| Groq | Ultra-low-latency LLM inference |
| Cohere | Text embeddings for semantic search |
| LangGraph | RAG workflow orchestration |
| Qdrant | Vector database for document retrieval |

---

## 💾 Data & Caching

| Technology | Purpose |
|---|---|
| Redis | Inference result caching (fail-open) |
| In-memory store | Chat message history (dev mode) |

---

## 📊 Observability

| Technology | Purpose |
|---|---|
| Prometheus (prometheus-client) | API latency, cache hit/miss metrics |
| Structured logging | JSON logs via Python `logging` |

---

## 🐳 DevOps

| Technology | Purpose |
|---|---|
| Docker | Containerized local and production deployments |
| Docker Compose | Multi-service orchestration (API + Qdrant + Redis) |
| GitHub Actions | CI/CD — lint, test, build on every push |
| Render | Cloud deployment target |

---

## 🗓️ Planned Additions

| Technology | Purpose |
|---|---|
| JWT / OAuth | User authentication |
| React Native | Cross-platform mobile app |
| Server-Sent Events | Streaming AI responses |
| PostgreSQL | Persistent chat history |
