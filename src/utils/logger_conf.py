import os
import sys
import logging


# Stop uvicorn log propagation otherwise we would have duplicate logs
uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.propagate = False

# Set asyncio log level to warning for less verbose logging
asyncio_logger = logging.getLogger('asyncio')
asyncio_logger.setLevel(logging.WARNING)


logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get('LOG_LEVEL', logging.DEBUG),
    format="%(levelname)s:\t%(message)s"
)
