from starlette.middleware.base import BaseHTTPMiddleware

from src.utils.logger_conf import logger
from src.lib.mia_platform_client import MiaPlatformClient


class MiaPlatformClientMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request
    """

    async def dispatch(self, request, call_next):
        keys = [key.replace('_', '-') for key in request.headers.keys()]
        values = request.headers.values()

        request.state.mia_platform_client = MiaPlatformClient(
            dict(zip(keys, values)),
            logger
        )

        response = await call_next(request)
        return response
