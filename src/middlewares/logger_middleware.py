import time
from starlette.middleware.base import BaseHTTPMiddleware


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request and logs request info
    """

    def __init__(self, app, logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request, call_next):
        excluded_paths = [
            '/-/ready',
            '/-/healthz',
            '/-/check-up',
        ]

        if request.url.path not in excluded_paths:
            self.logger.debug(f"{request.method} {request.url.path}")
            start_time = time.time()

        request.state.logger = self.logger
        response = await call_next(request)

        if request.url.path not in excluded_paths:
            duration = time.time() - start_time
            self.logger.debug(
                f"{request.method} {request.url.path} {response.status_code} {duration:.6f}s"
            )

        return response
