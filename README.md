[![CI](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml/badge.svg)](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-pubsub-red?logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Kubernetes](https://img.shields.io/badge/k8s-manifests-informational)
![Prometheus](https://img.shields.io/badge/metrics-prometheus-E6522C?logo=prometheus&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

# TrojanChat

TrojanChat is a real-time chat platform designed to showcase backend systems thinking through WebSocket communication, authentication, metrics instrumentation, deployment assets, and scalable messaging patterns.

This repository is intended to demonstrate production-style service architecture for a chat application, with a focus on engineering patterns rather than only UI polish.

---

## Overview

TrojanChat is built to highlight several capabilities that matter in backend and platform work:

- real-time chat behavior
- service-oriented architecture
- metrics and observability
- deployment-readiness through Docker and Kubernetes assets
- security-oriented design patterns such as JWT-based auth and role-based access control
- support for both API-style execution and Streamlit-based interaction

The project is especially useful as a portfolio signal because it shows distributed systems concepts in a domain that recruiters understand quickly.

---

## What is implemented today

The repository currently presents the following areas of functionality:

- real-time messaging architecture
- JWT-oriented authentication flow
- role-aware authorization patterns
- Redis-backed pub/sub style messaging support
- Prometheus metrics exposure
- Docker-based container execution
- Kubernetes deployment manifests
- CI workflow integration
- a Streamlit app for an easier local demo path

This gives the project value beyond a basic chat demo because it combines application logic, infrastructure concepts, and operational visibility.

---

## Architecture

```text
Client / UI
    ↓
FastAPI / application layer
    ↓
WebSocket chat handling
    ↓
Redis pub/sub for multi-instance communication
    ↓
Metrics endpoint
    ↓
Prometheus / monitoring stack
At a high level, TrojanChat is framed as a horizontally scalable chat service rather than a single-process toy implementation.
Why this repo is a strong portfolio signal
This repository demonstrates engineering decisions that are useful in both backend and AI-adjacent infrastructure roles:
stateful real-time communication patterns
separation of security, messaging, and observability concerns
infrastructure-aware application design
deployment artifacts that suggest cloud portability
a demo-friendly local path through Streamlit
a service mindset rather than a one-file project structure
For recruiters, it helps show that you can think about systems, not just scripts.
Quick start
Bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
pip install -r requirements-dev.txt
Run the Streamlit app:
Bash
streamlit run streamlit_app.py
Run the backend API server:
Bash
docker run -p 6379:6379 redis

export SECRET_KEY="your-secret-key"
export REDIS_URL="redis://localhost:6379"

uvicorn app.main:app --reload
Local verification checklist
A reviewer can validate the project with a few quick steps:
Bash
# Start Redis
docker run -p 6379:6379 redis

# Start API
uvicorn app.main:app --reload

# Run Streamlit demo
streamlit run streamlit_app.py

# Run tests
pytest tests/ -q

# Inspect metrics
curl http://localhost:8000/metrics
This section is included intentionally to strengthen proof and reproducibility.
Metrics and evidence
The repository describes Prometheus metrics such as:
active WebSocket connections
total messages processed
message latency histograms
cache hit and miss behavior
error counters
Current portfolio-safe evidence:
metrics are part of the project design
observability is treated as a first-class concern in the README and structure
Docker and Kubernetes manifests are present
CI is wired into the repository
the project includes a real-time system design story rather than only static CRUD behavior.