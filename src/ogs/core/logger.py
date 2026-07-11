"""
===========================================================

Module:
    logger.py

Purpose:
    Central logging system for OGS.

===========================================================
"""

from __future__ import annotations

import sys
from loguru import logger

from ogs.core.constants import LOG_DIR, LOG_FILE


def configure_logger() -> None:
    """
    Configure the global application logger.
    """

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        colorize=True,
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )

    logger.add(
        LOG_FILE,
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        level="DEBUG",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )


def get_logger():
    """
    Return the configured logger instance.
    """
    return logger
