# TrojanChat — Engineering Metrics

This document defines the technical, reliability, performance, and ML metrics
used to evaluate TrojanChat as a production-grade system.

---

## 1. System Reliability

| Metric | Target | Description |
|------|--------|-------------|
| Uptime | ≥ 99.9% | Measured via container health checks |
| API Error Rate | < 1% | 5xx responses over total requests |
| Restart Rate | < 1/day | Container restarts per 24h |

---

## 2. Performance Metrics

| Metric | Target | Description |
|------|--------|-------------|
| API Latency (p95) | < 200ms | End-to-end request latency |
| Message Throughput | 1,000+ msg/sec | Concurrent chat messages |
| Cold Start Time | < 3s | Docker container boot time |

---

## 3. Scalability Metrics

| Metric | Target | Description |
|------|--------|-------------|
| Concurrent Users | 50k+ | Horizontal scaling supported |
| DB Read Latency | < 20ms | MongoDB indexed queries |
| Cache Hit Rate | > 85% | Redis-backed message caching |

---

## 4. ML / AI Metrics (Optional GPU Acceleration)

| Metric | Target | Description |
|------|--------|-------------|
| Inference Latency | < 150ms | GPU or CPU fallback |
| Model Accuracy | ≥ 92% | Toxicity / moderation classification |
| GPU Utilization | 70–90% | Efficient CUDA usage |

---

## 5. Security Metrics

| Metric | Target |
|------|--------|
| Auth Coverage | 100% |
| JWT Expiration | ≤ 60 min |
| Rate Limit Violations | < 0.1% |
| Dependency CVEs | 0 Critical |

---

## 6. Observability

| Metric | Tool |
|------|------|
| Metrics | Prometheus |
| Logging | Loguru |
| Alerts | Render / Prometheus |
| Tracing | Planned (OpenTelemetry) |

---

## 7. Deployment Metrics

| Metric | Target |
|------|--------|
| CI Success Rate | ≥ 99% |
| Rollback Time | < 60s |
| Image Size | < 1.2GB |

---

## 8. Continuous Improvement

Metrics are reviewed weekly. Regressions trigger alerts and automated rollback.
New features must define measurable success criteria before merge.

---

_Last Updated: 2025_


