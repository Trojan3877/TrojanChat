import mlflow

def start_run(run_name: str):
    mlflow.set_experiment("trojanchat-llm")
    return mlflow.start_run(run_name=run_name)

def log_metrics(latency_ms: float, tokens: int):
    mlflow.log_metric("latency_ms", latency_ms)
    mlflow.log_metric("tokens_used", tokens)

def log_params(params: dict):
    for key, value in params.items():
        mlflow.log_param(key, value)