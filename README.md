<p align="center">
  <img src="docs/banner.png" width="100%" />
</p>

<h1 align="center">TrojanChat</h1>
<p align="center">
  <strong>Real-Time Multi-Platform Chat Application</strong><br>
  Web • Terminal • Android • FastAPI • WebSockets • Docker  
</p>

<p align="center">

  <!-- Backend -->
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=flat-square" />
  <img src="https://img.shields.io/badge/WebSockets-RealTime-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Uvicorn-ASGI%20Server-purple?style=flat-square" />
  <img src="https://img.shields.io/badge/Pydantic-Validation-blue?style=flat-square" />

  <!-- Frontend -->
  <img src="https://img.shields.io/badge/HTML-Web-red?style=flat-square" />
  <img src="https://img.shields.io/badge/CSS-Styling-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/JavaScript-Frontend-yellow?style=flat-square" />

  <!-- Terminal -->
  <img src="https://img.shields.io/badge/Python-CLI-blue?style=flat-square" />

  <!-- Android -->
  <img src="https://img.shields.io/badge/Android-Kotlin-green?style=flat-square" />
  <img src="https://img.shields.io/badge/OkHttp-Networking-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Coroutines-Async-blue?style=flat-square" />

  <!-- DevOps -->
  <img src="https://img.shields.io/badge/Docker-Ready-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI/CD-gray?style=flat-square" />

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" />

</p>


---

# 🚀 Overview

**TrojanChat** is a fully modern, real-time chat application designed with a **Big Tech architecture**.  
It includes:

- **FastAPI backend** (REST + WebSockets)
- **Web Client** (real-time, JS + WebSockets)
- **Terminal Client** (real-time, async WebSockets)
- **Android Client** (Kotlin + OkHttp)
- **Dockerized backend**
- **Clean architecture (services/routes/config)**
- **Production-grade folder structure**
- **Automated tests with pytest**

This repo demonstrates **software engineering maturity**, multi-platform development, API design, real-time communication, and scalable system architecture.

---
<p align="center">
  <img src="docs/architecture_dark.png" width="90%" />
</p>

**System Flow:**

1. Clients (Web, Terminal, Android) connect via **WebSocket** for live messaging  
2. Backend broadcasts to all connected clients  
3. REST API provides message history + health checks  
4. Optional DB/Firebase/Redis layer can be plugged in for persistence  

---

# 💻 Tech Stack

### **Backend**
- FastAPI
- WebSockets
- Python 3.11
- Uvicorn
- Pydantic
- Docker
- pytest

### **Clients**
- **Web**: HTML, CSS, JavaScript (WebSockets)
- **Terminal**: Python + websockets + asyncio
- **Android**: Kotlin + OkHttp + Coroutines

### **DevOps**
- Dockerfile (production-ready)
- `.env.example` for secure configuration
- Modular folder structure
- Test suite with pytest

---

# ⭐ Features

- 🔥 **True real-time messaging** (WebSockets)
- 🌐 **Multi-platform chat** (Web, Terminal, Android)
- 🧱 **Scalable architecture** ready for DB, Redis, Firebase
- 🧪 **Automated test suite**
- 🐳 **Docker-ready backend**
- 📡 **REST + WebSockets hybrid design**
- 🚀 **Clean + extensible folder structure**

---

# 📁 Folder Structure
TrojanChat/
│
├── backend/
│ ├── api.py
│ ├── config.py
│ ├── routes/
│ │ ├── chat_routes.py
│ │ └── ws_routes.py
│ ├── services/
│ │ └── chat_service.py
│ ├── requirements.txt
│
├── client/
│ ├── web/
│ │ ├── index.html
│ │ ├── styles.css
│ │ └── chat.js
│ ├── terminal/
│ │ └── cli.py
│ └── android/
│ ├── app/
│ └── MainActivity.kt
│
├── docs/
│ ├── architecture_dark.png
│ ├── flowchart.png
│ └── banner.png
│
├── tests/
│ └── test_chat_service.py
│
├── .gitignore
├── .env.example
├── Dockerfile
├── README.md
├── LICENSE


---
<p align="center">
  <img src="docs/flowchart.png" width="80%" />
</p>


# 🖼 Screenshots

### Web Client (Real-Time)
<p align="center">
  <img src="docs/screenshots/web_client.png" width="70%" />
</p>

### Terminal Client (Real-Time)
<p align="center">
  <img src="docs/screenshots/terminal_client.png" width="70%" />
</p>

### Android Client (Mobile)
<p align="center">
  <img src="docs/screenshots/android_app.png" width="40%" />
</p>

# ⚙️ Backend Setup

### Install dependencies
```bash
pip install -r backend/requirements.txt
uvicorn backend.api:app --host 0.0.0.0 --port 8000
http://localhost:8000
ws://localhost:8000/ws/chat
client/web/index.html
python client/terminal/cli.py
client/android/app/
ws://10.0.2.2:8000/ws/chat




