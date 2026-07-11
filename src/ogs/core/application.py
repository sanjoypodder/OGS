"""
===========================================================

Module:
    application.py

Purpose:
    Main Application Kernel for OGS.

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

from ogs.core.logger import get_logger
from ogs.core.service_container import ServiceContainer
from ogs.core.shutdown import ShutdownManager
from ogs.core.startup import StartupManager
from ogs.models.application_state import ApplicationState


class Application:
    """
    Main application kernel.

    Coordinates all major components of OGS.
    """

    def __init__(self) -> None:

        self.logger = get_logger()

        self.state = ApplicationState.STOPPED

        self.container = ServiceContainer()

        self.startup = StartupManager()

        self.shutdown_manager = ShutdownManager()

    @property
    def application_state(self) -> ApplicationState:
        """
        Return current application state.
        """

        return self.state

    def initialize(self) -> None:
        """
        Initialize OGS.
        """

        self.state = ApplicationState.INITIALIZING

        self.logger.info("Application Initializing...")

        self.container.register("logger", self.logger)

        self.container.register("startup", self.startup)

        self.container.register(
            "shutdown",
            self.shutdown_manager,
        )

    def run(self) -> None:
        """
        Start OGS.
        """

        self.initialize()

        self.startup.start()

        self.state = ApplicationState.RUNNING

        self.logger.success("OGS Kernel Running")

    def shutdown(self) -> None:
        """
        Shutdown OGS.
        """

        self.state = ApplicationState.SHUTTING_DOWN

        self.shutdown_manager.shutdown()

        self.container.clear()

        self.state = ApplicationState.STOPPED

        self.logger.success("OGS Stopped Successfully")