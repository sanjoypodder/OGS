"""
===========================================================

OGS Smart Money AI

Session Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Session
from .enums import (
    SessionStatus,
    SessionType,
)


class SessionFactory:
    """
    Session Factory.
    """

    @staticmethod
    def create(
        session_id: str,
        name: str,
        exchange: str,
        market: str,
        **kwargs,
    ) -> Session:

        return Session(
            session_id=session_id,
            name=name,
            exchange=exchange,
            market=market,
            **kwargs,
        )

    @staticmethod
    def regular(
        session_id: str,
        name: str,
        exchange: str,
        market: str,
        **kwargs,
    ) -> Session:

        return Session(
            session_id=session_id,
            name=name,
            exchange=exchange,
            market=market,
            session_type=SessionType.REGULAR,
            status=SessionStatus.OPEN,
            **kwargs,
        )

    @staticmethod
    def clone(
        session: Session,
    ) -> Session:

        return deepcopy(session)