import time
from app.core.llm_client import LLMClient
from ml.tracking.mlflow_utils import start_run, log_metrics, log_params
from ml.metrics import token_count

def run_prompt_experiment(prompt: str, api_key: str):
    llm = LLMClient(api_key)
    with start_run("prompt-eval-v1"):
        start = time.time()
        output = llm.generate(prompt)
        latency = (time.time() - start) * 1000

        log_params({
            "model": "gpt-4.1",
            "prompt_version": "v1"
        })
        log_metrics(latency, token_count(output))

    return output