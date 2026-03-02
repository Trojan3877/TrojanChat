from fastapi import FastAPI
from app.middleware.request_id_middleware import RequestIDMiddleware
from app.core.logging_config import configure_logging

app = FastAPI()

configure_logging()
app.add_middleware(RequestIDMiddleware)