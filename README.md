# 🚀 TrojanChat
![CI Pipeline](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml/badge.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-passing-success)
![Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen)

![Docker](https://img.shields.io/badge/docker-ready-blue)
![Kubernetes](https://img.shields.io/badge/k8s-ready-informational)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black)

![OpenClaw](https://img.shields.io/badge/OpenClaw-AI%20Workflow-purple)
![AI Assisted](https://img.shields.io/badge/AI-assisted%20engineering-blueviolet)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Repo Status](https://img.shields.io/badge/status-active-success)
![Version](https://img.shields.io/badge/version-1.0.0-orange)





 TrojanChat is a horizontally scalable, observable, and secure real-time chat platform engineered using production-grade backend architecture patterns.
This system demonstrates:
Distributed WebSocket handling
JWT-based authentication
Role-based authorization (RBAC)
Redis Pub/Sub horizontal scaling
Prometheus metrics exposure
Hardened multi-stage Docker builds
Kubernetes autoscaling deployment
CI/CD with automated security scanning
This project is built to reflect Staff-Level (L6+) systems thinking.

System Architecture
Client (Web / Mobile)
        ↓
Ingress / Load Balancer
        ↓
Kubernetes Cluster
        ↓
TrojanChat Pods (Replicas)
        ↓
Redis Pub/Sub Layer
        ↓
Metrics Endpoint (/metrics)
        ↓
Prometheus → Grafana

Architecture Design Principles
1. Horizontal Scalability
Multiple backend replicas
Redis Pub/Sub for cross-instance message sync
Kubernetes HPA auto-scaling
2. Observability First
Prometheus metrics endpoint
Structured JSON logging
Correlation IDs
Container health tracking
3. Security by Design
JWT Authentication
Role-Based Access Control
Token expiration
Docker non-root execution
CI security scanning (Bandit + Trivy)
4. CI/CD Automation
Lint enforcement
Type checking
Security scans
Coverage tracking
Docker image validation

Quick Start (Local Development)

Clone Repo
Bash

git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat
Create Virtual Environment
Bash

python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # windows
Install Dependencies
Bash

pip install -r requirements.txt
Run Redis (Docker)
Bash
Copy code
docker run -p 6379:6379 redis Set Environment Variables
Bash

export SECRET_KEY="your-secret-key"
export REDIS_URL="redis://localhost:6379"
Start Server
Bash

uvicorn app.main:app --reload
Run With Docker
Bash

docker build -t trojanchat .
docker run -p 8000:8000 -e SECRET_KEY=secret -e REDIS_URL=redis://host.docker.internal:6379 trojanchat

☸ Kubernetes Deployment


kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
This deploys:
3 replicas (minimum)
Autoscaling up to 10 replicas
CPU-based scaling trigger (70% utilization)

Metrics & Observability
TrojanChat exposes:

Project Structure

app/
 ├── core/
 │    ├── security.py
 │    ├── logging_config.py
 │    ├── redis_manager.py
 │    ├── metrics.py
 │
 ├── middleware/
 │    ├── request_id_middleware.py
 │
 ├── dependencies/
 │    ├── auth.py
 │
 ├── main.py
 │
k8s/
 ├── deployment.yaml
 ├── service.yaml
 ├── hpa.yaml

.github/workflows/
 ├── ci.yml



GET /metrics
Prometheus metrics include:
Metric
Type
Description
trojan_active_connections
Gauge
Active WebSocket connections
trojan_messages_total
Counter
Total messages processed
trojan_message_latency_seconds
Histogram
Message processing latency
Example Prometheus scrape config:
YAML
Copy code
scrape_configs:
  - job_name: 'trojan-chat'
    static_configs:
      - targets: ['trojan-chat-service:8000']

Security Model
Authentication
JWT-based token validation
Expiration enforcement
Token verification during WebSocket handshake
Authorization
Role-based access control
Admin endpoints protected
Secure WebSocket validation
Container Hardening
Multi-stage Docker builds
Non-root runtime user
Trivy vulnerability scanning in CI

CI/CD Pipeline
Pipeline enforces:
flake8 lint
black format check
mypy type checking
bandit security scan
pytest coverage
Docker image build
Trivy container scan
PRs fail automatically if violations occur.

Performance & Scaling
Horizontal Scale
Redis Pub/Sub allows:
Multi-replica sync
Distributed WebSocket broadcasting
Load-balanced message handling
Autoscaling
Kubernetes HPA:
Min: 3 pods
Max: 10 pods
CPU trigger: 70%

Why Redis?
Decouples messaging from instance memory
Enables stateless backend
Supports distributed scaling
Why Prometheus?
Cloud-native observability standard
Enables SRE monitoring
Supports latency & load dashboards
Why JWT?
Stateless authentication
Works across replicas
Compatible with OAuth providers
Why Kubernetes?
Production industry standard
Rolling deployments
Health probes
Auto-restart on failure

Failure Scenarios & Resilience
Scenario
Mitigation
Pod crash
Kubernetes auto-restart
High traffic spike
HPA scaling
Single node failure
Replica redundancy
Unauthorized socket
JWT verification
Container vulnerability
Trivy scan in CI
🚀 Enterprise Readiness Summary
TrojanChat demonstrates:
Distributed systems design
Production security
Observability instrumentation
DevSecOps pipeline integration
Cloud-native deployment model
Staff-level architecture reasoning

Extended Q&A (L6 Level)
Q: What happens if 100,000 users connect simultaneously?
A: Kubernetes horizontally scales replicas while Redis synchronizes cross-pod messaging. HPA increases pods based on CPU utilization.
Q: How do you prevent unauthorized access?
A: JWT validation occurs before WebSocket upgrade. Role-based enforcement protects privileged endpoints.
Q: How would you support multi-region deployment?
A: Add Redis clustering or migrate to managed distributed message brokers (e.g., Kafka). Use geo-load balancing.
Q: How is observability handled?
A: Prometheus metrics + structured logs + correlation IDs allow root-cause tracing.
Q: How would you extend this to production cloud?
A:
Deploy on AWS EKS / GKE
Use managed Redis (Elasticache)
Add Ingress + TLS termination
Add WAF for DDoS mitigation
📜 License
MIT License
