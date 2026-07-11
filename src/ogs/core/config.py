"""
===========================================================

Module:
    config.py

Purpose:
    Central application configuration.

Author:
    Om Ganapati Solution

Project:
    OGS Smart Money AI

===========================================================
"""

from dataclasses import dataclass, field

from ogs.core.constants import (
    APP_NAME,
    CODENAME,
    COMPANY,
    DEFAULT_SYMBOL,
    DEFAULT_TIMEFRAME,
    DEFAULT_TIMEZONE,
)
from ogs.core.version import VERSION


@dataclass(slots=True)
class AppConfig:
    """
    Global application configuration.
    """

    app_name: str = APP_NAME

    company: str = COMPANY

    codename: str = CODENAME

    version: str = field(default_factory=lambda: VERSION.full)

    debug: bool = True

    log_level: str = "INFO"

    theme: str = "Dark"

    timezone: str = DEFAULT_TIMEZONE

    default_symbol: str = DEFAULT_SYMBOL

    default_timeframe: str = DEFAULT_TIMEFRAME


CONFIG = AppConfig()
