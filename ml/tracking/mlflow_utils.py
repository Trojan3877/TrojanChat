import mlflow

def log_chat_metrics(latency_ms: float, tokens: int, prompt_version: str):
    mlflow.log_metric("latency_ms", latency_ms)
    mlflow.log_metric("tokens_used", tokens)
    mlflow.log_param("prompt_version", prompt_version)