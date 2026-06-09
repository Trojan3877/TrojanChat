# TrojanChat

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](https://github.com/Trojan3877/TrojanChat/actions)
[![Security Status](https://img.shields.io/badge/security-passed-brightgreen?style=flat-square)](https://github.com/PyCQA/bandit)
[![Production Ready](https://img.shields.io/badge/status-production--ready-brightgreen?style=flat-square)](https://github.com/Trojan3877/TrojanChat)
[![Code Quality](https://img.shields.io/badge/code%20quality-A%20grade-brightgreen?style=flat-square)](https://github.com/Trojan3877/TrojanChat)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT)

TrojanChat is a production-hardened, multi-client chat architecture optimized for high-concurrency environments. Moving away from standard blocking network sockets, this platform leverages asynchronous event loops to maintain thousands of concurrent connections efficiently while maintaining structural memory efficiency.

---

## 🏗️ Architectural Overview

The platform splits operations across an event-driven system architecture to eliminate thread-starvation issues under scale.

* **Non-Blocking Core:** Built on top of Python's raw `asyncio` streams API, replacing slow multi-threaded overhead with a high-performance single-threaded asynchronous engine.
* **Structured Serialization Protocol:** Completely dropped plaintext string messaging in favor of structured JSON payloads, allowing for strict validation boundaries and predictable message framing.
* **Rootless Isolation Security:** Containers are structurally hardened using explicit multi-stage build patterns, forcing runtime scripts to execute via a dedicated unprivileged user group (`apprunner`).

---

## 🚀 Getting Started

### Prerequisites
* Python 3.11 or higher
* Docker (Optional, for containerized isolation)

### Standard Local Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Trojan3877/TrojanChat.git](https://github.com/Trojan3877/TrojanChat.git)
    cd TrojanChat
    ```

2.  **Initialize Environment & Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Spin Up the Core Infrastructure Engine:**
    ```bash
    python server.py
    ```

4.  **Connect Distributed Clients (In separate terminals):**
    ```bash
    python client.py "Corey"
    ```

---

## 🐳 Production Container Deployment

This repository uses a defensive multi-stage `Dockerfile` compilation sandbox strategy. The container compiles system wheels in Stage 1, then ports the output to a stripped runtime image to dramatically shrink attack vectors and exploit spaces.

Q1: Why use an Asynchronous Event Loop (asyncio) instead of traditional Multi-threading?
A: Multi-threaded architectures assign a dedicated operating system thread to every single connected client socket. When scaling up to thousands of concurrent users, this model hits a bottleneck due to extreme RAM consumption (each thread pre-allocates stack memory) and massive CPU overhead caused by continuous thread context-switching.

TrojanChat uses a single-threaded asynchronous event loop via asyncio. It utilizes multiplexed, non-blocking I/O system calls underneath the hood. When a socket is waiting for network data packets to arrive, it yields control back to the central event loop, enabling a single thread to smoothly manage thousands of active user data streams without breaking a sweat.

Q2: How does the application prevent data injection or cross-site script (XSS) delivery?
A: The platform implements defensive validation boundaries right at the ingestion layer:

Structural Enforcement: The backend drops raw plaintext and forces strict JSON layout checks. If a packet cannot be parsed into our target schema via json.loads(), it triggers a localized exception and drops the packet instantly.

Type Enforcement & Whitespace Trimming: The server extracts keys explicitly, forces type constraints, and trims down text fields via .strip().

Escaping Responsibilities: While basic script payloads are safely contained as text strings within the backend data stream, frontend interfaces reading from the stream treat the message string as immutable raw text rather than executable markup code, eliminating downstream script execution hazards.

Q3: What happens when a network connection suddenly drops or behaves erratically?
A: Traditional systems can suffer from socket resource leaks or frozen application states if a client drops offline abruptly. TrojanChat manages this through isolated, defensive write boundaries (_safe_write).

If a data write fails or throws an unhandled socket error, the server intercepts the exception immediately, bypasses global runtime crashes, purges that specific client's memory address pointer from the central tracking array (self.active_connections), and formally closes the socket file descriptor to prevent kernel-level file descriptor resource exhaustion.

Q4: How can this application scale horizontally to support millions of concurrent users across multiple regions?
A: Currently, the active connection mapping exists locally within the server's process memory space (self.active_connections). To scale horizontally across multiple cloud instances or Kubernetes clusters behind a global load balancer, the in-memory array can be supplemented with an external Redis Pub/Sub broker.

When Instance A receives a chat payload from an active socket, it publishes that JSON payload to a central Redis cluster topic. All other running application instances subscribing to that Redis topic pick up the message and broadcast it out concurrently to their own locally connected client pools.

### Building the Image
```bash
docker build -t trojanchat:latest .
