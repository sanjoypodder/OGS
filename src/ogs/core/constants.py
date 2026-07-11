"""
===========================================================

OGS Smart Money AI

Core Constants

===========================================================
"""

from pathlib import Path

# --------------------------------------------------------
# Project Information
# --------------------------------------------------------

APP_NAME = "OGS Smart Money AI"

COMPANY_NAME = "Om Ganapati Solution"

CODENAME = "GARUDA"

VERSION = "0.0.1"

# --------------------------------------------------------
# Directories
# --------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[3]

SRC_DIR = ROOT_DIR / "src"

DOCS_DIR = ROOT_DIR / "docs"

LOG_DIR = ROOT_DIR / "logs"

DATABASE_DIR = ROOT_DIR / "database"

ASSETS_DIR = ROOT_DIR / "assets"

CONFIG_DIR = ROOT_DIR / "config"

TESTS_DIR = ROOT_DIR / "tests"

RELEASES_DIR = ROOT_DIR / "releases"

# --------------------------------------------------------
# Log File
# --------------------------------------------------------

LOG_FILE = LOG_DIR / "ogs.log"

# --------------------------------------------------------
# Database
# --------------------------------------------------------

DATABASE_FILE = DATABASE_DIR / "ogs.db"
