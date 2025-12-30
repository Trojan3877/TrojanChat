import time

class AnalyticsService:
    def track_latency(self, start_time: float) -> float:
        return (time.time() - start_time) * 1000