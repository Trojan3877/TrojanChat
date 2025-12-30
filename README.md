TrojanChat 🚀



TrojanChat is a **production-ready, L7/L8-quality conversational AI platform** designed for real-time USC football discussions.  
It demonstrates **modern LLM system design**, **ML observability**, and **clean UI/UX**, following engineering standards used at Big Tech and Big AI companies.



Tech Stack

- **LLM**: OpenAI GPT-4.1 (Responses API)
- **Backend**: Python 3.11
- **LLM Experiment Tracking**: MLflow
- **UI**: Streamlit (Chat + Metrics Dashboard)
- **Testing**: Pytest
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

[![CI](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Trojan3877/TrojanChat/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/Trojan3877/TrojanChat)
![Last Commit](https://img.shields.io/github/last-commit/Trojan3877/TrojanChat)
![Repo Size](https://img.shields.io/github/repo-size/Trojan3877/TrojanChat)
![Issues](https://img.shields.io/github/issues/Trojan3877/TrojanChat)
![Stars](https://img.shields.io/github/stars/Trojan3877/TrojanChat?style=social)



 Architecture Overview

TrojanChat follows a **clean, layered architecture** designed for scalability and maintainability: 
User (Streamlit UI) ↓ Chat Service (Business Logic) ↓ Prompt Templates ↓ GPT-4.1 LLM (Responses API) ↓ MLflow (Latency, Tokens, Prompt Versions)
**Key design principles:**
- Thin service layers
- No framework lock-in
- Prompt versioning
- Observability first
- Testable components


 Project Structure
TrojanChat/ ├── app/ │   ├── api/                # Controllers & health checks │   ├── core/               # LLM client, config, prompts │   ├── services/           # Chat, moderation, analytics │   └── main.py │ ├── ml/ │   ├── experiments/        # Prompt experiments │   ├── tracking/           # MLflow utilities │   └── metrics.py │ ├── streamlit_app/ │   ├── pages/              # Chat UI + Metrics Dashboard │   ├── state.py │   └── dashboard.py │ ├── tests/                  # Pytest unit tests ├── .github/workflows/      # CI pipeline ├── Dockerfile ├── requirements.txt ├── .env.example └── README.md



MLflow Usage (Production-Grade)

TrojanChat tracks **LLM inference quality** using MLflow:

- Latency (ms)
- Token usage
- Prompt version
- Model version

This enables:
- Prompt A/B testing
- Performance regression detection
- Cost monitoring

MLflow runs are logged **outside notebooks**, matching industry practice.

Streamlit UI

Chat Interface
- Real-time conversational UI
- Session-aware message history
- Clean UX with minimal overhead

Metrics Dashboard
- Latency trends
- Token usage visualization
- Model observability for production readiness


 Testing Strategy

- Unit tests for core services
- LLM client interface validation
- Business-logic isolation via mocks

This ensures **safe refactoring and scaling**.


Local Setup
 Clone Repository
```bash
git clone https://github.com/Trojan3877/TrojanChat.git
cd TrojanChat

Create Environment

Bash
cp .env.example .env
Add your OpenAI API key:


OPENAI_API_KEY=sk-xxxx
Install Dependencies

Bash
pip install -r requirements.txt
Run Streamlit App

Bash
streamlit run streamlit_app/dashboard.py
🐳 Docker Run
Copy code
Bash
docker build -t trojanchat .
docker run -p 8501:8501 trojanchat

Why This Is L7 / L8 Quality
✔ Production-ready architecture
✔ Observability with MLflow
✔ Clean separation of concerns
✔ Real CI/CD
✔ Test coverage
✔ No over-engineering or AI-generated clutter
This project demonstrates senior-level engineering judgment, not just model usage.
Roadmap
Firebase / Auth integration
Mobile client (iOS / Android)
Vector memory (RAG)
Multi-model routing
Monetization Layer


Engineering Q&A (Recruiter & Senior Reviewer Focused)

What problem does TrojanChat solve?
TrojanChat demonstrates how to design a production-grade LLM application that goes beyond a toy chatbot.
It focuses on clean system boundaries, observability, and maintainability, using a real domain (sports discussion) to showcase scalable design.

Why GPT-4.1 and not an open-source model?
GPT-4.1 is used to demonstrate:
Enterprise-grade reasoning quality
Stable inference behavior
Compatibility with modern production APIs (Responses API)
The architecture intentionally abstracts the LLM client, making it trivial to swap in:
Open-source models
Anthropic
Self-hosted inference endpoints
This mirrors real-world multi-model routing strategies.

How is prompt quality evaluated?
Prompt quality is evaluated using MLflow, tracking:
Latency (ms)
Token usage
Prompt version
Model version
Prompt experiments are run outside notebooks, enabling:
Reproducible evaluations
Regression detection
Cost-performance analysis
This approach matches industry LLM experimentation workflows.

Why MLflow instead of logging to files or dashboards only?
MLflow provides:
Versioned experiments
Structured metrics
Historical comparisons
Model/prompt traceability
This is critical in LLM systems where prompt changes can silently degrade performance.

How does TrojanChat handle scalability concerns?
TrojanChat is designed to scale via:
Stateless service layers
Session abstraction
Clear separation between UI, services, and LLM logic
In production, this design supports:
Horizontal scaling
Async inference
Load-balanced LLM gateways
Multi-region deployment

Why Streamlit for the UI?
Streamlit is used intentionally for:
Rapid iteration
Low UI overhead
Clear demonstration of system behavior
The UI is not tightly coupled to backend logic, making it easy to replace with:
React
Mobile clients
External APIs

How is reliability ensured?
Reliability is enforced through:
Unit tests for core services
Mocked LLM dependencies
GitHub Actions CI on every push and PR
This ensures:
Safe refactoring
Predictable behavior
Continuous verification

What makes this project L7/L8 quality?
TrojanChat demonstrates engineering judgment, not just features:
Clear boundaries
Minimal abstractions
Observability-first design
Testability
CI/CD discipline
No over-engineering
This aligns with expectations for Senior / Staff-level engineers.

What would you add next in a real production environment?
Planned next steps include:
Vector-based memory (RAG)
Auth + user identity
Rate limiting
Cost tracking per session
Model routing
Mobile clients
Monetization hooks

Who is this project for?
This project is designed to demonstrate readiness for:
AI / ML Engineer roles
Software Engineer (LLM systems)
Applied AI teams
Big Tech / Big AI companies

Final Note
TrojanChat intentionally avoids:
Over-commented AI code
Fake complexity
Unnecessary frameworks
Instead, it focuses on clarity, correctness, and scalability — the traits evaluated at L7/L8 interviews.



License
MIT License — free to use, modify, and deploy.
Author
Corey Leath
Aspiring AI / ML Engineer
GitHub: https://github.com/Trojan3877
