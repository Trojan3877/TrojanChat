# app/middleware/request_id_middleware.py

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging_config import generate_request_id, set_request_id


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = generate_request_id()
        set_request_id(request_id)

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id

        return response