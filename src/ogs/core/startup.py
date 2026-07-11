"""
===========================================================

Module:
    startup.py

Purpose:
    OGS startup sequence.

===========================================================
"""

from ogs.core.environment import EnvironmentManager
from ogs.core.logger import get_logger


class StartupManager:
    """
    Startup sequence manager.
    """

    def __init__(self) -> None:

        self.logger = get_logger()

        self.environment = EnvironmentManager()

    def start(self) -> None:

        self.logger.info("Starting OGS...")

        self.environment.validate()

        self.logger.success("Startup completed.")
