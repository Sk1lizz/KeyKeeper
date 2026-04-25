# 

""""""

import logging
import sys

from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.utils.paths import get_log_dir
from src.utils.constants import (
    LOG_CONSOLE_LEVEL,
    LOG_FILE_LEVEL,
    LOG_FORMAT,
    LOG_DATE_FORMAT,
    LOG_FILE,
    LOG_MAX_BYTES,
    LOG_BACKUP_COUNT
)

def setup_logger() -> logging.Logger:
    """"""

    logger = logging.getLogger("KeyKeeper")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(LOG_CONSOLE_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_dir = get_log_dir()
    log_file = log_dir / LOG_FILE

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8"
    )

    file_handler.setLevel(LOG_FILE_LEVEL)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()