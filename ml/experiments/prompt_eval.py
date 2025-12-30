import time
from app.core.llm_client import LLMClient
from ml.tracking.mlflow_utils import log_chat_metrics

def run_experiment(prompt: str):
    llm = LLMClient(api_key="DUMMY")
    start = time.time()
    output = llm.generate(prompt)
    latency = (time.time() - start) * 1000

    log_chat_metrics(latency, len(output.split()), "v1")
    return output