![Uploading image.png…]()





# Trojan Chat

![Last Commit](https://img.shields.io/github/last-commit/Trojan3877/TrojanChat)  
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)  
![Platform: Android](https://img.shields.io/badge/platform-Android-brightgreen.svg)  
![Kotlin](https://img.shields.io/badge/kotlin-1.7.10-purple.svg)  
![Ktor](https://img.shields.io/badge/ktor-2.3.0-blue.svg)  
![Gradle](https://img.shields.io/badge/gradle-7.0-blue.svg)

---

## 🚀 Android Frontend

The Android client uses Kotlin + OkHttp for WebSocket communication.

### Prerequisites
- Android Studio Flamingo or later
- Android SDK 33

### Setup & Run
1. Open `TrojanChat-Android` in Android Studio.  
2. Sync Gradle.  
3. Run the `app` module on an emulator or device.  
4. Chat messages will be sent to/received from `ws://10.0.2.2:8080/chat`.  

---

## ⚙️ Kotlin Backend

The server is built with Ktor and handles WebSocket connections on port 8080.

### Prerequisites
- JDK 17+  
- Gradle 7+

### Setup & Run
```bash
cd TrojanChatServerKotlin
./gradlew run














# TrojanChat

![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub repo stars](https://img.shields.io/github/stars/Trojan3877/TrojanChat?style=social)
![GitHub forks](https://img.shields.io/github/forks/Trojan3877/TrojanChat?style=social)
![Build passing](https://img.shields.io/github/actions/workflow/status/Trojan3877/TrojanChat/ci.yml?branch=main)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

---

## Overview

**TrojanChat** is a full-stack, real-time chat application featuring:
- **User authentication** (JWT-based)
- **Multiple chat rooms**
- **Real-time messaging** via Socket.io
- **Persistent message storage** in MongoDB
- **Responsive frontend** using vanilla JavaScript, HTML & CSS
- **Dockerized deployment** with Docker Compose

---

## Architecture

![Architecture Diagram](docs/architecture.png)

1. **Frontend**  
   - `client/index.html`, `client/app.js`, `client/style.css`
   - Connects to backend via Socket.io with JWT authentication

2. **Backend**  
   - `server/index.js` (Express + Socket.io)
   - `server/models/User.js` (User schema)
   - `server/models/Message.js` (Message schema)
   - `server/auth.js` (Register/Login routes)
   - JWT middleware protects socket connections

3. **Database**  
   - MongoDB stores user accounts and chat messages

4. **Deployment**  
   - Docker Compose brings up MongoDB, backend, and frontend containers

---

## Getting Started (Local Development)

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Trojan3877/TrojanChat.git
   cd TrojanChat
