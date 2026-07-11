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

from ogs.core.version import VERSION


@dataclass(slots=True)
class AppConfig:
    """
    Global application configuration.
    """

    app_name: str = "OGS Smart Money AI"

    company: str = "Om Ganapati Solution"

    codename: str = "GARUDA"

    version: str = field(default_factory=lambda: VERSION.full)

    debug: bool = True

    log_level: str = "INFO"

    theme: str = "Dark"

    timezone: str = "Asia/Kolkata"

    default_symbol: str = "XAUUSD"

    default_timeframe: str = "5m"


CONFIG = AppConfig()
