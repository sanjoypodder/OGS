"""
OGS Smart Money AI
------------------

Session Engine Statistics

Provides statistical information about Session objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from .collection import SessionSeries
from .domain import Session
from .enums import (
    SessionState,
    SessionType,
    TradingDay,
)


class SessionStatistics:
    """
    Statistics for Session collections.
    """

    def __init__(
        self,
        series: SessionSeries,
    ) -> None:

        self._series = series

    @property
    def count(self) -> int:
        return len(self._series)

    @property
    def active_count(self) -> int:
        return sum(
            session.active
            for session in self._series
        )

    @property
    def tradable_count(self) -> int:
        return sum(
            session.tradable
            for session in self._series
        )

    @property
    def closed_count(self) -> int:
        return sum(
            session.state == SessionState.CLOSED
            for session in self._series
        )

    @property
    def pre_open_count(self) -> int:
        return sum(
            session.state == SessionState.PRE_OPEN
            for session in self._series
        )

    @property
    def asian_count(self) -> int:
        return sum(
            session.session == SessionType.ASIAN
            for session in self._series
        )

    @property
    def london_count(self) -> int:
        return sum(
            session.session == SessionType.LONDON
            for session in self._series
        )

    @property
    def new_york_count(self) -> int:
        return sum(
            session.session == SessionType.NEW_YORK
            for session in self._series
        )

    @property
    def london_close_count(self) -> int:
        return sum(
            session.session == SessionType.LONDON_CLOSE
            for session in self._series
        )

    @property
    def monday_count(self) -> int:
        return sum(
            session.trading_day == TradingDay.MONDAY
            for session in self._series
        )

    @property
    def friday_count(self) -> int:
        return sum(
            session.trading_day == TradingDay.FRIDAY
            for session in self._series
        )

    @property
    def average_duration_minutes(self) -> float:

        if len(self._series) == 0:
            return 0.0

        return (
            sum(
                session.duration_minutes
                for session in self._series
            )
            / len(self._series)
        )

    @property
    def latest(self) -> Session | None:

        if len(self._series) == 0:
            return None

        return self._series.last

    @property
    def oldest(self) -> Session | None:

        if len(self._series) == 0:
            return None

        return self._series.first

    @property
    def current_active(self) -> Session | None:

        for session in self._series:

            if session.active:
                return session

        return None