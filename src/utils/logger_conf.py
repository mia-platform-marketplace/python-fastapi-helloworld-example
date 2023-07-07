import os
import sys
import logging


# Stop uvicorn log propagation otherwise we would have duplicate logs
uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.propagate = False


logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get('LOG_LEVEL', logging.DEBUG),
    format="%(levelname)s:\t%(message)s"
)
