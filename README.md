# TrojanChat 🚀

![Python](https://img.shields.io/badge/python-3.10-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![CUDA](https://img.shields.io/badge/NVIDIA-CUDA-green)
![CI](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview
TrojanChat is a production-grade, scalable chat platform designed with
modern backend, cloud, and ML engineering practices.

## Architecture
![Architecture](docs/architecture.png)

## Tech Stack
- FastAPI (Async API)
- MongoDB + Redis
- Docker + CUDA
- Prometheus Metrics
- JWT Authentication
- Render Deployment

## Quickstart (Local)
```bash
git clone https://github.com/Trojan3877/TrojanChat
cd TrojanChat
docker-compose up --build
Visit: http://localhost:10000

Deployment (Render)

Connect GitHub repo

Select Dockerfile

Set environment variables

Deploy 🚀

GPU Support

If NVIDIA GPU is available, CUDA is auto-detected.

Metrics

See metrics.md

Logs

See dailylog.md

License

MIT

