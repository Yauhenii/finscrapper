import logging
from app import settings


def setup_logger() -> None:
    logger = logging.getLogger(settings.logging.name)

    logger.setLevel(settings.logging.LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
