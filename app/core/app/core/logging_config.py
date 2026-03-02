# app/core/logging_config.py

import logging
import sys
import uuid
from contextvars import ContextVar
from pythonjsonlogger import jsonlogger

# Context variable for correlation ID
request_id_context: ContextVar[str] = ContextVar("request_id", default=None)


def generate_request_id() -> str:
    return str(uuid.uuid4())


def set_request_id(request_id: str):
    request_id_context.set(request_id)


def get_request_id() -> str:
    return request_id_context.get()


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = get_request_id()
        return True


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s %(request_id)s"
    )

    handler.setFormatter(formatter)

    handler.addFilter(RequestIdFilter())

    logger.addHandler(handler)