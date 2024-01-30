import os
import sys
import logging
from dotenv import load_dotenv


load_dotenv('default.env')


def get_logger(logger_name='mialogger'):
    logging.basicConfig(
        stream=sys.stdout,
        level=os.environ.get('LOG_LEVEL', logging.DEBUG),
    )

    # Clear any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Add a new handler with a filter
    handler = logging.StreamHandler(sys.stdout)
    handler.addFilter(lambda record: record.name.startswith(logger_name))

    logging.root.addHandler(handler)

    logger = logging.getLogger(logger_name)
    logger.propagate = False

    return logger
