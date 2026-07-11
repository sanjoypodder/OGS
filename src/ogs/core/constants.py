"""
===========================================================

Module:
    constants.py

Purpose:
    Global constants and project paths.

Author:
    Om Ganapati Solution

Project:
    OGS Smart Money AI

===========================================================
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

SRC_DIR = PROJECT_ROOT / "src"

DOCS_DIR = PROJECT_ROOT / "docs"

LOG_DIR = PROJECT_ROOT / "logs"

DATABASE_DIR = PROJECT_ROOT / "database"

CONFIG_DIR = PROJECT_ROOT / "config"

TESTS_DIR = PROJECT_ROOT / "tests"

KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"

ASSETS_DIR = PROJECT_ROOT / "assets"

RELEASES_DIR = PROJECT_ROOT / "releases"

TOOLS_DIR = PROJECT_ROOT / "tools"

SCRIPTS_DIR = PROJECT_ROOT / "scripts"

LOG_FILE = LOG_DIR / "ogs.log"

DATABASE_FILE = DATABASE_DIR / "ogs.db"

DEFAULT_SYMBOL = "XAUUSD"

DEFAULT_TIMEFRAME = "5m"

DEFAULT_TIMEZONE = "Asia/Kolkata"

APP_NAME = "OGS Smart Money AI"

COMPANY = "Om Ganapati Solution"

CODENAME = "GARUDA"
