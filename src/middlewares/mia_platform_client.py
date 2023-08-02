from starlette.middleware.base import BaseHTTPMiddleware

from src.utils.logger_conf import logger
from src.lib.mia_platform_client import MiaPlatformClient


class MiaPlatformClientMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request
    """

    async def dispatch(self, request, call_next):
        request.state.mia_platform_client = MiaPlatformClient(
            dict(request.headers.items()),
            logger
        )

        response = await call_next(request)
        return response
