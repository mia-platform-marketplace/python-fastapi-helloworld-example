import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from src.middlewares.logger_middleware import LoggerMiddleware
from src.middlewares.mia_platform_client_middleware import MiaPlatformClientMiddleware

from src.apis.core.liveness import liveness_handler
from src.apis.core.readiness import readiness_handler
from src.apis.core.checkup import checkup_handler
from src.apis.hello_world import hello_world_handler


load_dotenv('default.env')

app = FastAPI(
    openapi_url="/documentation/json",
    docs_url=None,
    redoc_url=None
)

# Middlewares
app.add_middleware(LoggerMiddleware)
app.add_middleware(MiaPlatformClientMiddleware)

# Core
app.include_router(liveness_handler.router)
app.include_router(readiness_handler.router)
app.include_router(checkup_handler.router)

# Hello World
app.include_router(hello_world_handler.router)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=int(os.environ.get('HTTP_PORT', 3000)),
        log_config=None
    )
