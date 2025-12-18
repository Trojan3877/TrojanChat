# TrojanChat 🏈💬  
**A Production-Grade, Real-Time Chat Platform with ML-Assisted Moderation**

![Build](https://img.shields.io/github/actions/workflow/status/Trojan3877/TrojanChat/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![CUDA](https://img.shields.io/badge/NVIDIA-CUDA%20Ready-brightgreen)
![License](https://img.shields.io/github/license/Trojan3877/TrojanChat)
![Last Commit](https://img.shields.io/github/last-commit/Trojan3877/TrojanChat)

---

## 📌 Overview

**TrojanChat** is a real-time, scalable chat platform designed for high-traffic communities (e.g., sports fandoms, live events, campus networks).  
It supports **WebSocket-based messaging**, **JWT authentication**, **moderation via ML inference**, and **GPU acceleration (NVIDIA CUDA)**.

This project is engineered to **production standards** and aligned with **L6–L7 Big Tech system design expectations**.

---

## 🧠 Key Features

- ⚡ Real-time chat via WebSockets
- 🔐 JWT-based authentication
- 🧠 ML-assisted content moderation (GPU-accelerated)
- 🚀 NVIDIA CUDA support with CPU fallback
- 🧩 Modular service-oriented architecture
- 📊 Production metrics & observability
- 🐳 Dockerized for local & cloud deployment
- ☁️ Deployable on **Render**
- 🧪 CI-tested with GitHub Actions

---

## 🏗️ System Architecture

Client (Web / Mobile)
|
REST + WebSocket
|
FastAPI Gateway
|
| Auth | Chat | ML | Persistence |
Redis Cache
|
PostgreSQL
|
Optional GPU (CUDA Inference)

### Design Highlights
- Stateless API layer for horizontal scaling
- WebSocket fan-out optimized for low latency
- ML moderation isolated for safety and performance
- GPU detection at runtime with graceful fallback

---

## 🛠️ Tech Stack

| Layer            | Technology |
|------------------|------------|
| Backend API      | FastAPI |
| Realtime         | WebSockets |
| Database         | PostgreSQL |
| Cache            | Redis |
| Auth             | JWT |
| ML Inference     | PyTorch |
| GPU              | NVIDIA CUDA |
| Containerization | Docker |
| CI/CD            | GitHub Actions |
| Hosting          | Render |

---

## ⚡ Quickstart (Local)

```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
http://localhost:8000/docs
docker build -t trojanchat .
docker run -p 8000:8000 trojanchat
Requirements

NVIDIA GPU

CUDA Toolkit installed

nvidia-container-toolkit

docker build -f docker/Dockerfile.cuda -t trojanchat-gpu .
docker run --gpus all -p 8000:8000 trojanchat-gpu

TrojanChat includes a render.yaml for one-click deployment:

FastAPI web service

PostgreSQL database

Redis cache

GPU-backed inference can be deployed on supported Render instances or external GPU services.


