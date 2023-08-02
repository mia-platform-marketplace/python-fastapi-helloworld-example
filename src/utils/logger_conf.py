import os
import sys
import logging


logger = logging.getLogger('mialogger')

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(os.environ.get('LOG_LEVEL', logging.DEBUG))

formatter = logging.Formatter('%(levelname)s:\t%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
