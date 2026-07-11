"""
Central Logger
"""

from __future__ import annotations

import sys

from loguru import logger

from ogs.core.constants import LOG_FILE, LOG_DIR


def configure_logger() -> None:

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        colorize=True,
    )

    logger.add(
        LOG_FILE,
        level="DEBUG",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
    )


def get_logger():
    return logger
