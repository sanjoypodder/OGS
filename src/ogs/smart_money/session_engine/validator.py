"""
OGS Smart Money AI
------------------

Session Engine Validator

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Session
from .enums import (
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


class SessionValidator(BaseValidator):
    """
    Validates Session objects.
    """

    def validate(
        self,
        session: Session,
    ) -> bool:

        if session is None:
            return False

        if not session.symbol:
            return False

        if not isinstance(session.session, SessionType):
            return False

        if not isinstance(session.state, SessionState):
            return False

        if not isinstance(session.trading_day, TradingDay):
            return False

        if not isinstance(session.timezone, TimeZoneType):
            return False

        if session.start_time is None:
            return False

        if session.end_time is None:
            return False

        if session.end_time <= session.start_time:
            return False

        if session.duration_seconds <= 0:
            return False

        return True