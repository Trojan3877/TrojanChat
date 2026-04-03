# app/core/metrics.py

from prometheus_client import Counter, Gauge, Histogram

active_connections = Gauge("trojan_active_connections", "Active WebSocket Connections")
messages_sent = Counter("trojan_messages_total", "Total Messages Sent")
message_latency = Histogram("trojan_message_latency_seconds", "Message Latency")

# Inference cache metrics
cache_hits = Counter("trojan_cache_hits_total", "Inference cache hits")
cache_misses = Counter("trojan_cache_misses_total", "Inference cache misses")
cache_errors = Counter("trojan_cache_errors_total", "Redis cache errors")