import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
handler = logging.StreamHandler(sys.stdout)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('>>>>')

import os

os.makedirs('./logs', exist_ok=True)

logger = logging.getLogger('sitebot')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch_format = logging.Formatter('%(asctime)s : [%(name)s] : [%(levelname)s] : %(message)s')
ch.setFormatter(ch_format)

fh = logging.FileHandler(f'./logs/main_thread.log')
fh_format = logging.Formatter('%(asctime)s : [%(name)s] : [%(levelname)s] : %(message)s')
fh.setFormatter(fh_format)

logger.addHandler(ch)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
