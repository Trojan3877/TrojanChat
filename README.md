# 🏈 Trojan Chat

[![MCP Ready](https://img.shields.io/badge/MCP-Compatible-blue)](https://modelcontextprotocol.io)
[![n8n Automation](https://img.shields.io/badge/n8n-Automation-green)](https://n8n.io)
[![Build Status](https://img.shields.io/badge/CI-CD-orange)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A real-time chat application for **USC Trojan fans** to discuss games, recruiting, and staff updates.  
Now fully **MCP-compatible** and **n8n automation-ready** for smart integrations with AI agents and workflows.

---

## 🔹 Features
- ✅ Create and join themed rooms (game-day, recruiting, staff)  
- ✅ Post & fetch chat messages  
- ✅ AI Agent (MCP) support for structured access  
- ✅ n8n workflows for Slack alerts & Google Sheets logging  
- ✅ Ready for containerization (Docker support)  

---

## 🔹 Project Structure
├── mcp_config.json # MCP tool definitions
├── mcp_adapter.py # Adapter for MCP requests
├── n8n_webhook.py # Webhook server for n8n
├── trojan_chat_workflow.json # Ready-to-import n8n workflow
├── app/ # (Frontend/Backend chat app code)
├── requirements.txt # Dependencies
└── README.md # Documentation

##  Quickstart
```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat
# For terminal frontend
cd CPP
g++ main.cpp -o trojanchat && ./trojanchat

Architecture
flowchart TD
  Client Terminal ← WebSocket → Server Backend

<img width="1979" height="1180" alt="image" src="https://github.com/user-attachments/assets/cfe9c727-e9d9-437f-b0e9-75b23d81ef00" />




##  Overview
- **Purpose:** Real-time chat platform for USC football fans.
- **Core Value:** Lightweight, efficient, and modular design.
- **Why It Matters:** Demonstrates OOP, cross-platform deployment, and real-time backend logic.


1. **Cross-Platform Mobile**  
   - Android & iOS with React Native  
   - 🚀 Fastlane + GitHub Actions mobile CI  

2. **Scalable Backend**  
   - Go microservice (Gorilla Mux + Firebase)  
   - Dockerized & deployable via Kubernetes + Helm  

3. **Analytics & Monitoring**  
   - Google Analytics & Firebase Analytics integration  
   - Prometheus + Grafana dashboards  

4. **DevOps Automation**  
   - DVC data/versioning  
   - GitHub Actions CI/CD (lint, test, build, deploy)  
   - Ansible for infra configuration  
   - Terraform for cloud provisioning  

5. **Polished UX & Governance**  
   - Interactive Dashboard with Chart.js  
   - CHANGELOG, CONTRIBUTING, SECURITY, CODEOWNERS  

---

## Quickstart

```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat

# Local setup
cp .env.example .env 
scripts/setup_local.sh

# Run backend & frontend
docker-compose up -d

# K8s deploy (dev)
kubectl apply -f k8s/
helm upgrade --install trojanchat helm/trojanchat

# Full prod deploy
make deploy


├── CPP/
├── backend/
├── android/
├── server/
├── client/
└── README.md







