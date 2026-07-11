"""
===========================================================

Module:
    application.py

Purpose:
    Main application controller for OGS Smart Money AI.

===========================================================
"""

from __future__ import annotations

from ogs.core.config import config
from ogs.core.logger import configure_logger, get_logger


class Application:
    """
    Main application controller.
    """

    def __init__(self) -> None:

        configure_logger()

        self.logger = get_logger()

    def initialize(self) -> None:

        self.logger.info("Initializing OGS Smart Money AI...")

    def run(self) -> None:

        self.initialize()

        print("=" * 60)
        print(config.app_name)
        print(config.company)
        print(f"Version : {config.version}")
        print(f"Codename: {config.codename}")
        print("=" * 60)

        self.logger.success("OGS Started Successfully")

    def shutdown(self) -> None:

        self.logger.info("Shutting down OGS Smart Money AI...")
