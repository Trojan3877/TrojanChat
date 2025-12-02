<h1 align="center">🔥 TrojanChat — Real-Time Multi-Platform Chat System</h1>

<p align="center">
  <strong>A production-style, multi-client distributed chat application built with FastAPI, WebSockets, Kotlin, JavaScript, and Python.</strong>
</p>

<p align="center">
  <!-- Backend -->
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=flat-square" />
  <img src="https://img.shields.io/badge/WebSockets-RealTime-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Uvicorn-ASGI%20Server-purple?style=flat-square" />

  <!-- Frontend -->
  <img src="https://img.shields.io/badge/HTML-Web-red?style=flat-square" />
  <img src="https://img.shields.io/badge/CSS-Styling-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/JavaScript-Frontend-yellow?style=flat-square" />

  <!-- Terminal -->
  <img src="https://img.shields.io/badge/Python-CLI-blue?style=flat-square" />

  <!-- Android -->
  <img src="https://img.shields.io/badge/Android-Kotlin-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Coroutines-Async-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/OkHttp-Networking-orange?style=flat-square" />

  <!-- DevOps -->
  <img src="https://img.shields.io/badge/Docker-Ready-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-gray?style=flat-square" />
  
  <!-- Tests -->
  <img src="https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/coverage-90%25-blue?style=flat-square" />

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" />
</p>

---

# 📌 Overview

**TrojanChat** is a real-time, multi-platform chat system designed with production-level engineering practices.  
It features:

- 🚀 **FastAPI WebSocket backend**  
- 🖥 **Web client (HTML/CSS/JS)**  
- 🖥 **Terminal real-time chat client**  
- 📱 **Android Kotlin client**  
- 📦 **Docker-ready deployment**  
- 🧪 **Automated test suite (pytest + WebSocket tests)**  
- 🧩 **Clean architecture & modular design**

This project demonstrates real distributed-system thinking, multi-client support, and full-stack engineering.

---

# 🏗 Architecture

<p align="center">
  <img src="docs/architecture_dark.png" width="90%" />
</p>

### **Core Architecture Components**
- **FastAPI WebSocket Server** → manages real-time connections  
- **Broadcast Hub** → relays messages across all connected clients  
- **Web Client** → lightweight frontend UI  
- **Terminal Client** → real-time CLI experience  
- **Android Client** → mobile chat app (Kotlin + Coroutines)  

---

# 🔄 System Flow

<p align="center">
  <img src="docs/flowchart.png" width="80%" />
</p>

---

# 🚀 Quick Start

### **1. Clone the Repository**
```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat

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
🚀 Quick Start
1. Clone the Repository
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat

2. Setup Python Environment
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows

3. Install Backend Dependencies
pip install -r backend/requirements.txt

4. Start the Real-Time Backend Server
uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload


The backend is now running at:
👉 http://localhost:8000

WebSocket endpoint:
👉 ws://localhost:8000/ws/chat

5. Run the Web Client

Open:

client/web/index.html


in your browser.
This is a full real-time web chat UI.

6. Run the Terminal Client
python client/terminal/cli.py



