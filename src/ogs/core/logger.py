"""
===========================================================

Module:
    logger.py

Purpose:
    Central logging system for OGS Smart Money AI.

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

import sys

from loguru import logger

from ogs.core.constants import LOG_DIR, LOG_FILE

_CONFIGURED = False


def configure_logger() -> None:
    """
    Configure the global application logger.

    Safe to call multiple times.
    """

    global _CONFIGURED

    if _CONFIGURED:
        return

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
        level="DEBUG",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )

    _CONFIGURED = True


def get_logger():
    """
    Return the global logger instance.
    """

    if not _CONFIGURED:
        configure_logger()

    return logger
