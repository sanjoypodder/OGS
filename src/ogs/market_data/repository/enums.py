"""
OGS Smart Money AI

Repository Enums
"""

from __future__ import annotations

from enum import Enum


class RepositoryType(str, Enum):
    """
    Types of repositories supported by OGS.
    """

    IN_MEMORY = "IN_MEMORY"

    DATABASE = "DATABASE"

    FILE_SYSTEM = "FILE_SYSTEM"

    CACHE = "CACHE"

    REMOTE = "REMOTE"

    HYBRID = "HYBRID"

    UNKNOWN = "UNKNOWN"


class RepositoryStatus(str, Enum):
    """
    Current repository status.
    """

    ACTIVE = "ACTIVE"

    READ_ONLY = "READ_ONLY"

    SYNCING = "SYNCING"

    UPDATING = "UPDATING"

    ARCHIVED = "ARCHIVED"

    ERROR = "ERROR"

    UNKNOWN = "UNKNOWN"