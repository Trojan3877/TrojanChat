https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-1fa8-61f7-a78f-ff9fcd56ab9b/raw?se=2025-06-06T03%3A00%3A30Z&sp=r&sv=2024-08-04&sr=b&scid=ae05e7d3-aab3-5b1e-9f6c-b35edf604e39&skoid=ec8eb293-a61a-47e0-abd0-6051cc94b050&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-06-06T02%3A41%3A38Z&ske=2025-06-07T02%3A41%3A38Z&sks=b&skv=2024-08-04&sig=s76rmuWXJX9/M/IDyn28JXhaV/stC7MXJh8hoS82XeU%3D

> Adjust the Docker Compose commands/acronyms if you place `server` and `client` at different relative paths.

---

### 🚀 How to Integrate These Files:

1. **Create a new `server/` directory** in your repo and add:
   - `index.js`
   - `models/Message.js`
   - `models/User.js`
   - `auth.js`
   - `.env.example`
   - `Dockerfile`
   - `package.json`
   - (optional) `tests/` subfolder with `auth.test.js`
2. **Create a new `client/` directory** (or rename your existing front-end folder to `client/`) and add:
   - `index.html`
   - `app.js`
   - `style.css`
   - `Dockerfile`
   - `package.json` (optional)
3. Add `docker-compose.yml` at the repository root.
4. **Populate environment variables** in `/server/.env` (copy `.env.example` → `.env`).
5. **Install dependencies**:
   ```bash
   cd server
   npm install
   cd ../client
   npm install  # if using live-server for local dev















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
