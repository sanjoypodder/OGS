"""
OGS Smart Money AI
------------------

Session Engine Factory

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from datetime import datetime

from .domain import Session
from .enums import (
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)
from .validator import SessionValidator


class SessionFactory:
    """
    Factory for creating validated Session objects.
    """

    _validator = SessionValidator()

    @classmethod
    def create(
        cls,
        symbol: str,
        session: SessionType,
        state: SessionState,
        trading_day: TradingDay,
        start_time: datetime,
        end_time: datetime,
        timezone: TimeZoneType = TimeZoneType.UTC,
        active: bool = False,
        tradable: bool = False,
    ) -> Session:
        """
        Create a validated Session object.
        """

        obj = Session(
            symbol=symbol,
            session=session,
            state=state,
            trading_day=trading_day,
            timezone=timezone,
            start_time=start_time,
            end_time=end_time,
            active=active,
            tradable=tradable,
        )

        if not cls._validator.validate(obj):
            raise ValueError("Invalid Session.")

        return obj