# 🤝 Contributing to TrojanChat

Thank you for your interest in contributing to **TrojanChat**!  
This project is designed to meet **production-grade, enterprise-level engineering standards**.

---

## 📌 Code of Conduct

By participating, you agree to maintain a respectful, inclusive, and professional environment.

- Be respectful and constructive
- No harassment or discrimination
- Assume positive intent
- Focus on technical merit

---

## 🧭 Project Philosophy

TrojanChat prioritizes:

- **Performance first** (low latency, high throughput)
- **Security by design**
- **Scalability**
- **Observability**
- **Clean, readable code**
- **Clear documentation**

---

## 🛠️ Development Setup

### Prerequisites
- Linux / macOS / WSL (Windows supported via Docker)
- C++20 compatible compiler (GCC 11+, Clang 14+)
- Python 3.10+
- Docker
- NVIDIA GPU (optional, for CUDA acceleration)

### Clone the Repository
```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat
Build (Local)
mkdir build && cd build
cmake ..
make

Run (Docker)
docker compose up --build

🧪 Testing

All contributions must include tests.

Run Unit Tests
ctest --output-on-failure

Python Tests
pytest tests/

📐 Coding Standards
C++

Follow Google C++ Style Guide

Use RAII for memory safety

Avoid raw pointers when possible

Prefer std::unique_ptr / std::shared_ptr

All public functions must be documented

Python

Follow PEP8

Use type hints

Modular design

No logic in global scope

🧩 Commit Message Format

Use Conventional Commits:

type(scope): short description

feat(api): add websocket authentication
fix(cache): resolve redis connection leak
docs(readme): update deployment instructions

🔁 Pull Request Process

Fork the repository

Create a feature branch

git checkout -b feat/my-feature


Write code + tests

Run all tests locally

Submit PR with:

Clear description

Linked issue (if applicable)

Screenshots/logs (if UI or performance change)

📊 Performance Expectations

All changes must:

Maintain or improve latency

Avoid unnecessary memory allocation

Be benchmarked when performance-critical

Benchmarks live in metrics.md.

🧠 Architecture Awareness

Contributors are expected to review:

SYSTEM_DESIGN.md

Architecture diagrams

Data flow documentation

Changes impacting architecture must be documented.

🔐 Security

Never commit secrets

Use .env.example

Report vulnerabilities privately

📬 Contact

Maintainer: Corey Leath
GitHub: https://github.com/Trojan3877

Thank you for helping build TrojanChat into a world-class system 🚀
