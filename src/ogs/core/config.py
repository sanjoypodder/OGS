"""
===========================================================

Module:
    config.py

Purpose:
    Central configuration manager for OGS.

Author:
    Om Ganapati Solution

Project:
    OGS Smart Money AI

===========================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AppConfig:
    """
    Global application configuration.

    This class stores all configurable settings
    used throughout the application.
    """

    app_name: str = "OGS Smart Money AI"

    company: str = "Om Ganapati Solution"

    version: str = "0.0.1"

    codename: str = "GARUDA"

    theme: str = "Dark"

    timezone: str = "Asia/Kolkata"

    default_symbol: str = "XAUUSD"

    default_timeframe: str = "5m"

    log_level: str = "INFO"

    debug_mode: bool = True


config = AppConfig()
