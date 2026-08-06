"""
===========================================================

OGS Smart Money AI

Trading Sessions

===========================================================
"""

from __future__ import annotations

from datetime import time
from enum import StrEnum


class TradingSession(StrEnum):
    """
    Supported institutional trading sessions.
    """

    ASIAN = "Asian"

    LONDON = "London"

    NEW_YORK = "New York"

    SYDNEY = "Sydney"

    OVERLAP = "Overlap"

    CLOSED = "Closed"

    @property
    def start(self) -> time:

        mapping = {
            TradingSession.SYDNEY: time(21, 0),
            TradingSession.ASIAN: time(0, 0),
            TradingSession.LONDON: time(8, 0),
            TradingSession.NEW_YORK: time(13, 0),
            TradingSession.OVERLAP: time(13, 0),
            TradingSession.CLOSED: time(0, 0),
        }

        return mapping[self]

    @property
    def end(self) -> time:

        mapping = {
            TradingSession.SYDNEY: time(6, 0),
            TradingSession.ASIAN: time(9, 0),
            TradingSession.LONDON: time(17, 0),
            TradingSession.NEW_YORK: time(22, 0),
            TradingSession.OVERLAP: time(17, 0),
            TradingSession.CLOSED: time(0, 0),
        }

        return mapping[self]

    @property
    def is_active(self) -> bool:
        return self != TradingSession.CLOSED

    @property
    def label(self) -> str:
        return self.value