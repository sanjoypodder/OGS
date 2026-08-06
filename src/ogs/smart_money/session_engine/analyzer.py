"""
OGS Smart Money AI
------------------

Session Engine Analyzer

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from datetime import datetime, time

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import SessionSeries
from .domain import Session
from .enums import (
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


class SessionAnalyzer(BaseAnalyzer):
    """
    Trading Session Analyzer.
    """

    DEFAULT_TIMEZONE = TimeZoneType.UTC

    SESSION_SCHEDULE = {

        SessionType.ASIAN: (
            time(0, 0),
            time(3, 0),
        ),

        SessionType.LONDON: (
            time(7, 0),
            time(10, 0),
        ),

        SessionType.NEW_YORK: (
            time(12, 0),
            time(15, 0),
        ),

        SessionType.LONDON_CLOSE: (
            time(15, 0),
            time(17, 0),
        ),
    }

    DAY_MAPPING = {
        0: TradingDay.MONDAY,
        1: TradingDay.TUESDAY,
        2: TradingDay.WEDNESDAY,
        3: TradingDay.THURSDAY,
        4: TradingDay.FRIDAY,
        5: TradingDay.SATURDAY,
        6: TradingDay.SUNDAY,
    }

    def analyze(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> SessionSeries:

        series = SessionSeries()

        trading_day = self.DAY_MAPPING[
            timestamp.weekday()
        ]

        current = timestamp.time()

        weekend = trading_day in (
            TradingDay.SATURDAY,
            TradingDay.SUNDAY,
        )

        for session_type, (
            start,
            end,
        ) in self.SESSION_SCHEDULE.items():

            start_dt = datetime.combine(
                timestamp.date(),
                start,
            )

            end_dt = datetime.combine(
                timestamp.date(),
                end,
            )

            if start <= current <= end:

                state = SessionState.ACTIVE

                active = True

            elif current < start:

                state = SessionState.PRE_OPEN

                active = False

            else:

                state = SessionState.CLOSED

                active = False

            tradable = (
                active
                and
                not weekend
            )

            series.append(

                Session(

                    symbol=symbol,

                    session=session_type,

                    state=state,

                    trading_day=trading_day,

                    timezone=self.DEFAULT_TIMEZONE,

                    start_time=start_dt,

                    end_time=end_dt,

                    active=active,

                    tradable=tradable,
                )

            )

        return series

    def active(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> Session | None:

        series = self.analyze(
            symbol,
            timestamp,
        )

        for session in series:

            if session.active:
                return session

        return None

    def tradable(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> list[Session]:

        series = self.analyze(
            symbol,
            timestamp,
        )

        return [
            session
            for session in series
            if session.tradable
        ]

    def closed(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> list[Session]:

        series = self.analyze(
            symbol,
            timestamp,
        )

        return [
            session
            for session in series
            if session.state is SessionState.CLOSED
        ]

    def pre_open(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> list[Session]:

        series = self.analyze(
            symbol,
            timestamp,
        )

        return [
            session
            for session in series
            if session.state is SessionState.PRE_OPEN
        ]