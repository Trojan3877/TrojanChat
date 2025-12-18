# 🚀 TrojanChat Deployment Guide

This document explains how to deploy TrojanChat locally, on Render, and with NVIDIA GPU acceleration for AI workloads.

---

## 🧱 Deployment Overview

TrojanChat is designed to be:
- Containerized with Docker
- Cloud-deployable on Render
- GPU-accelerated via NVIDIA CUDA (optional)
- Scalable with stateless API design

---

## 🖥️ Local Development (CPU)

### Requirements
- Python 3.10+
- Docker (optional)
- Git

### Steps
```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat
pip install -r requirements.txt
python main.py

🐳 Docker Deployment
Build Image
docker build -t trojanchat .

Run Container
docker run -p 8000:8000 trojanchat

☁️ Render Deployment (Production)
1️⃣ Create Render Web Service

Runtime: Docker

Branch: main

Region: Oregon (recommended)

Instance Type: Starter or Standard

2️⃣ Environment Variables

Set in Render dashboard:

PORT=8000
ENV=production
JWT_SECRET=your-secret-key

⚡ NVIDIA CUDA (GPU Acceleration)

TrojanChat supports GPU acceleration for AI inference.

Requirements

NVIDIA GPU (RTX 30xx+ recommended)

NVIDIA Container Toolkit

Build GPU Image
docker build -f Dockerfile.cuda -t trojanchat-gpu .

Run with GPU
docker run --gpus all -p 8000:8000 trojanchat-gpu

📊 Monitoring & Logs

Render dashboard logs

Docker logs:

docker logs <container_id>
