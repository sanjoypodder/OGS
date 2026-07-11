"""
===========================================================

Module:
    shutdown.py

Purpose:
    Graceful shutdown manager.

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

from ogs.core.logger import get_logger


class ShutdownManager:
    """
    Handles graceful shutdown of OGS.
    """

    def __init__(self) -> None:
        self.logger = get_logger()

    def shutdown(self) -> None:
        """
        Shutdown the application.
        """

        self.logger.info("Shutting down OGS...")

        # Future:
        # Close database
        # Stop engines
        # Stop market data
        # Flush logs

        self.logger.success("OGS shutdown completed.")