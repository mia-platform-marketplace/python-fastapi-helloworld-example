from starlette.middleware.base import BaseHTTPMiddleware

from src.lib.mia_platform_client import MiaPlatformClient


class MiaPlatformClientMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the logger to the request
    """

    def __init__(self, app, logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request, call_next):
        request.state.mia_platform_client = MiaPlatformClient(
            dict(request.headers.items()),
            self.logger
        )

        response = await call_next(request)
        return response
