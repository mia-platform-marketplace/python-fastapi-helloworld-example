import time
from starlette.middleware.base import BaseHTTPMiddleware

from src.utils.logger import logger


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request and logs request info
    """

    async def dispatch(self, request, call_next):
        excluded_paths = [
            '/-/ready',
            '/-/healthz',
            '/-/check-up',
        ]

        if request.url.path not in excluded_paths:
            logger.debug(f"{request.method} {request.url.path}")
            start_time = time.time()

        request.state.logger = logger
        response = await call_next(request)

        if request.url.path not in excluded_paths:
            duration = time.time() - start_time
            logger.debug(
                f"{request.method} {request.url.path} {response.status_code} {duration:.6f}s"
            )

        return response
