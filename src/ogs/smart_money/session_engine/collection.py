"""
OGS Smart Money AI
------------------

Session Engine Collection

Stores multiple Session objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from collections.abc import Iterable

from ogs.smart_money.base.collection import BaseCollection

from .domain import Session
from .enums import (
    SessionState,
    SessionType,
    TradingDay,
)


class SessionSeries(
    BaseCollection[Session],
):
    """
    Collection of Session objects.
    """

    def __init__(
        self,
        items: Iterable[Session] | None = None,
    ) -> None:

        super().__init__(items)

    def append(
        self,
        session: Session,
    ) -> None:
        """
        Append a Session.
        """
        self._items.append(session)

    def latest(
        self,
        count: int = 1,
    ) -> list[Session]:
        """
        Return latest sessions.
        """
        return self._items[-count:]

    def active(
        self,
    ) -> list[Session]:
        """
        Return active sessions.
        """
        return [
            session
            for session in self._items
            if session.active
        ]

    def tradable(
        self,
    ) -> list[Session]:
        """
        Return tradable sessions.
        """
        return [
            session
            for session in self._items
            if session.tradable
        ]

    def by_session(
        self,
        session_type: SessionType,
    ) -> list[Session]:
        """
        Filter by session type.
        """
        return [
            session
            for session in self._items
            if session.session == session_type
        ]

    def by_state(
        self,
        state: SessionState,
    ) -> list[Session]:
        """
        Filter by session state.
        """
        return [
            session
            for session in self._items
            if session.state == state
        ]

    def by_day(
        self,
        trading_day: TradingDay,
    ) -> list[Session]:
        """
        Filter by trading day.
        """
        return [
            session
            for session in self._items
            if session.trading_day == trading_day
        ]