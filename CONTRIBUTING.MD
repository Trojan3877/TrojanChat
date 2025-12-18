# 🤝 Contributing to TrojanChat

Thank you for your interest in contributing to **TrojanChat** 🎉  
This document outlines the standards, workflows, and expectations for contributors.

TrojanChat follows **Big Tech–style engineering practices** to ensure quality, maintainability, and security.

---

## 🧭 Code of Conduct

All contributors are expected to:
- Be respectful and professional
- Collaborate constructively
- Follow ethical engineering practices
- Avoid harassment, discrimination, or abusive behavior

---

## 🛠️ Development Environment

### Requirements
- Python 3.10+
- Git
- Docker (optional but recommended)
- NVIDIA GPU (optional for CUDA workloads)

### Recommended Tools
- VS Code
- GitHub CLI
- Docker Desktop
- Postman / HTTPie

---

## 🌱 Branching Strategy

We use a **trunk-based development** model:

- `main` → production-ready
- Feature branches → `feature/<short-description>`
- Bug fixes → `fix/<short-description>`

Example:
```bash
git checkout -b feature/chat-rate-limiting
