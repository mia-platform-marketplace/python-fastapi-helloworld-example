import os
import sys
import logging
from starlette.middleware.base import BaseHTTPMiddleware


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request
    """

    async def dispatch(self, request, call_next):
        logging.basicConfig(
            stream=sys.stdout,
            level=os.environ.get('LOG_LEVEL', logging.DEBUG),
            format="%(asctime)s %(levelname)s %(message)s"
        )

        request.state.logging = logging
        response = await call_next(request)
        return response
