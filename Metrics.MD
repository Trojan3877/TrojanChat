# 📊 TrojanChat Metrics

Performance targets measured during local and Render-hosted testing.

---

## API Performance

| Metric | Value | Measurement Method |
|---|---|---|
| Avg Response Latency | ~1.2 s | End-to-end (query → response) |
| Retrieval Top-K Accuracy | ~85% | Cosine similarity, top-3 documents |
| API Uptime | 99% | Render dashboard (free tier) |
| Max Throughput | 500 req/min | Single FastAPI instance, wrk benchmark |
| Indexed Documents | 1,000+ | USC football knowledge base |

---

## Cache Performance

| Metric | Value |
|---|---|
| Cache Hit Rate (warm) | ~40% on repeated queries |
| Redis Fail-Open | Yes — cache errors do not block responses |
| Cache TTL | 3,600 s (configurable via `CACHE_TTL` env var) |

---

## Observability

Prometheus metrics are exposed at `/metrics` via `prometheus-client`. Key counters:

- `cache_hits_total`
- `cache_misses_total`
- `cache_errors_total`

These can be scraped by any Prometheus-compatible monitoring stack (Grafana, Datadog, etc.).
