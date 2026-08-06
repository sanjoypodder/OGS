"""
===========================================================

Module:
    environment.py

Purpose:
    Validate the runtime environment before starting OGS.

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

import importlib
import platform
import sys

from ogs.core.constants import (
    CONFIG_DIR,
    DATABASE_DIR,
    DOCS_DIR,
    KNOWLEDGE_DIR,
    LOG_DIR,
    PROJECT_ROOT,
    RELEASES_DIR,
    SCRIPTS_DIR,
    TESTS_DIR,
    TOOLS_DIR,
)
from ogs.core.exceptions import EnvironmentError
from ogs.core.logger import get_logger


class EnvironmentManager:
    """
    Validate the OGS runtime environment.
    """

    REQUIRED_DIRECTORIES = [
        LOG_DIR,
        DATABASE_DIR,
        CONFIG_DIR,
        DOCS_DIR,
        KNOWLEDGE_DIR,
        TESTS_DIR,
        TOOLS_DIR,
        RELEASES_DIR,
        SCRIPTS_DIR,
    ]

    REQUIRED_PACKAGES = [
        "loguru",
    ]

    MINIMUM_PYTHON = (3, 14)

    def __init__(self) -> None:
        self.logger = get_logger()

    def validate(self) -> None:
        """
        Run every validation.
        """

        self.logger.info("Running environment validation...")

        self._check_python()

        self._check_project()

        self._check_directories()

        self._check_packages()

        self._check_permissions()

        self._check_virtual_environment()

        self.logger.success("Environment validation completed.")

    def _check_python(self) -> None:

        if sys.version_info < self.MINIMUM_PYTHON:
            raise EnvironmentError(
                f"Python {self.MINIMUM_PYTHON[0]}.{self.MINIMUM_PYTHON[1]} or higher is required."
            )

        self.logger.info(f"Python : {platform.python_version()}")

    def _check_project(self) -> None:

        if not PROJECT_ROOT.exists():
            raise EnvironmentError("Project root not found.")

        self.logger.info(f"Project : {PROJECT_ROOT}")

    def _check_directories(self) -> None:

        for directory in self.REQUIRED_DIRECTORIES:
            directory.mkdir(parents=True, exist_ok=True)

            self.logger.info(f"Directory OK : {directory.name}")

    def _check_packages(self) -> None:

        for package in self.REQUIRED_PACKAGES:
            try:
                importlib.import_module(package)

                self.logger.info(f"Package OK : {package}")

            except ModuleNotFoundError as ex:
                raise EnvironmentError(f"Missing package: {package}") from ex

    def _check_permissions(self) -> None:

        test_file = LOG_DIR / ".permission"

        try:
            test_file.write_text("ogs")

            test_file.unlink()

        except Exception as ex:
            raise EnvironmentError("Write permission failed.") from ex

        self.logger.info("Write Permission : OK")

    def _check_virtual_environment(self) -> None:

        in_venv = hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix

        if in_venv:
            self.logger.info("Virtual Environment : Active")

        else:
            self.logger.warning("Virtual Environment : Not Active")
