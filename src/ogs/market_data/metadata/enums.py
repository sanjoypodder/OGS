"""
OGS Smart Money AI

Metadata Enums
"""

from __future__ import annotations

from enum import Enum


class MetadataType(Enum):
    """
    Metadata classification.
    """

    UNKNOWN = "UNKNOWN"

    SYSTEM = "SYSTEM"

    USER = "USER"

    MARKET = "MARKET"

    SMART_MONEY = "SMART_MONEY"

    AI = "AI"

    RISK = "RISK"

    STRATEGY = "STRATEGY"

    CUSTOM = "CUSTOM"


class MetadataStatus(Enum):
    """
    Metadata status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"


class MetadataValueType(Enum):
    """
    Supported metadata value types.
    """

    STRING = "STRING"

    INTEGER = "INTEGER"

    FLOAT = "FLOAT"

    BOOLEAN = "BOOLEAN"

    DATE = "DATE"

    DATETIME = "DATETIME"

    JSON = "JSON"

    LIST = "LIST"

    OBJECT = "OBJECT"