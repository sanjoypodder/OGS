"""
OGS Smart Money AI

Feed Enums
"""

from __future__ import annotations

from enum import Enum


class FeedType(str, Enum):
    """
    Supported feed types.
    """

    LIVE = "LIVE"

    HISTORICAL = "HISTORICAL"

    SIMULATED = "SIMULATED"

    PAPER = "PAPER"

    UNKNOWN = "UNKNOWN"


class FeedStatus(str, Enum):
    """
    Feed connection status.
    """

    CONNECTED = "CONNECTED"

    DISCONNECTED = "DISCONNECTED"

    PAUSED = "PAUSED"

    ERROR = "ERROR"

    UNKNOWN = "UNKNOWN"