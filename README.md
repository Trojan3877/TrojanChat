<p align="center">
  <img src="https://raw.githubusercontent.com/Trojan3877/assets/main/trojanchat_banner_dark.png" width="100%" />
</p>

<h1 align="center">TrojanChat</h1>
<p align="center">A cross-platform, real-time chat application built for USC fans (and scalable for production use).</p>

---

# 🚀 Overview

**TrojanChat** is a multi-platform real-time chat application designed to let USC football fans connect, discuss recruiting, games, staff changes, and more.  
The project is built with production readiness in mind, including:

- Multi-platform client support (Web, Terminal, Android, iOS, Desktop)
- Modular backend API
- Real-time messaging layer (Firebase or socket-ready)
- Scalable architecture for future growth
- Clean, documented code
- Big Tech–style engineering practices

---

# 🛠 Tech Stack

**Backend:**
- Python / FastAPI or Node.js (future upgrade)
- WebSockets / Firebase Realtime Database (chooseable)
- RESTful API (expandable)

**Frontend Clients:**
- Web (HTML/JS)
- Android Kotlin client
- Terminal chat client
- Windows desktop client (future)

**Tools:**
- Docker-ready
- CI/CD planned (GitHub Actions)
- Architecture Diagrams
- MIT License

---

# ⭐ Features

- Real-time messaging
- Multiple clients (terminal, web, mobile)
- Secure authentication (upgradeable)
- USC fan–focused UI (future)
- Modular backend API
- Chat rooms (coming soon)
- Message history + persistence (future)

---

# 🏗 Architecture

Below is a simplified architecture for TrojanChat:

                +------------------------+
                |      Web Client        |
                +------------------------+
                            |
                +------------------------+
                |    Android Client      |
                +------------------------+
                            |
                +------------------------+
                |  Terminal / Desktop    |
                +------------------------+
                            |
                            v
              +-----------------------------+
              |         Backend API         |
              |  (FastAPI / Node.js)        |
              +--------------+--------------+
                             |
                             v
              +-----------------------------+
              |   Realtime Storage Layer    |
              | (Firebase / WebSockets)     |
              +-----------------------------+

---

# 📦 Installation

Clone the repo:

```bash
git clone https://github.com/Trojan3877/TrojanChat
cd TrojanChat
pip install -r requirements.txt
Open project in Android Studio
Build > Make Project
python client/terminal/main.py
Open client/web/index.html in browser
uvicorn backend.api:app --reload
http://localhost:8000

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/aff03b98-26c4-43db-884d-249229ac898c" />





