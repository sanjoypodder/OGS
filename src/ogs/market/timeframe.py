"""
===========================================================

Module:
    timeframe.py

Purpose:
    Trading Timeframe Definitions

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class Timeframe(StrEnum):
    """
    Supported trading timeframes.
    """

    M1 = "1m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"

    H1 = "1h"
    H4 = "4h"

    D1 = "1d"

    W1 = "1w"

    MN1 = "1M"

    @property
    def minutes(self) -> int:
        mapping = {
            Timeframe.M1: 1,
            Timeframe.M5: 5,
            Timeframe.M15: 15,
            Timeframe.M30: 30,
            Timeframe.H1: 60,
            Timeframe.H4: 240,
            Timeframe.D1: 1440,
            Timeframe.W1: 10080,
            Timeframe.MN1: 43200,
        }
        return mapping[self]

    @property
    def seconds(self) -> int:
        return self.minutes * 60

    @property
    def label(self) -> str:
        labels = {
            Timeframe.M1: "1 Minute",
            Timeframe.M5: "5 Minutes",
            Timeframe.M15: "15 Minutes",
            Timeframe.M30: "30 Minutes",
            Timeframe.H1: "1 Hour",
            Timeframe.H4: "4 Hours",
            Timeframe.D1: "1 Day",
            Timeframe.W1: "1 Week",
            Timeframe.MN1: "1 Month",
        }
        return labels[self]

    @property
    def is_intraday(self) -> bool:
        return self in {
            Timeframe.M1,
            Timeframe.M5,
            Timeframe.M15,
            Timeframe.M30,
            Timeframe.H1,
            Timeframe.H4,
        }

    @property
    def is_higher_timeframe(self) -> bool:
        return self in {
            Timeframe.D1,
            Timeframe.W1,
            Timeframe.MN1,
        }

    @property
    def next_higher(self) -> Timeframe | None:
        mapping = {
            Timeframe.M1: Timeframe.M5,
            Timeframe.M5: Timeframe.M15,
            Timeframe.M15: Timeframe.M30,
            Timeframe.M30: Timeframe.H1,
            Timeframe.H1: Timeframe.H4,
            Timeframe.H4: Timeframe.D1,
            Timeframe.D1: Timeframe.W1,
            Timeframe.W1: Timeframe.MN1,
            Timeframe.MN1: None,
        }
        return mapping[self]
