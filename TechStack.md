# 🛠️ TrojanChat – Tech Stack Overview

This document outlines the technologies and tools used in the design and development of the TrojanChat application, as well as technologies planned for future integration.

---

## 💻 Core Development

| Technology     | Purpose                                  |
|----------------|------------------------------------------|
| C++            | Core application logic and structure     |
| OOP Principles | Modular class-based architecture         |
| Makefile       | (Optional) Compilation management        |
| Git & GitHub   | Version control and source collaboration |

---

## 📁 Project Architecture

- `src/`: Contains all C++ logic files and class definitions
- `data/`: Stores chat history and saved session data (File I/O)
- `docs/`: System diagrams and development documentation

---

## 🔄 Future Integration Plans

| Technology       | Purpose                                      |
|------------------|----------------------------------------------|
| Firebase Realtime DB | Cloud-based chat message storage         |
| Android/iOS App  | Mobile access to chatrooms                   |
| Web Frontend (React) | UI for web-based users (Phase 3)         |
| Google Auth or OAuth | Secure user login system                 |

---

## 🔐 Security Considerations

- Admin roles will include moderation controls
- Future updates will incorporate authentication & message validation
- User flagging system planned for abuse prevention

---

## 🧠 Developer Notes

This app is currently in terminal-only mode and simulates multi-user chat interaction using object-oriented design in C++. All messages are saved locally in `.txt` files for now but are structured in a way that can easily map to JSON or cloud databases for future upgrades.
