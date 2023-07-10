from starlette.middleware.base import BaseHTTPMiddleware

from src.utils.logger_conf import logging


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request
    """

    async def dispatch(self, request, call_next):
        request.state.logging = logging
        response = await call_next(request)
        return response
