"""
===========================================================

OGS Smart Money AI

Session Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Session
from .enums import (
    SessionStatus,
    SessionType,
)


class SessionCollection(
    BaseCollection[Session],
):

    @property
    def items(self):
        return self._items

    def add(
        self,
        session: Session,
    ) -> None:

        self._items.append(session)

    def find(
        self,
        session_id: str,
    ) -> Session | None:

        for session in self._items:
            if session.session_id == session_id:
                return session

        return None

    def active(self):

        return [
            s
            for s in self._items
            if s.status == SessionStatus.OPEN
        ]

    def closed(self):

        return [
            s
            for s in self._items
            if s.status == SessionStatus.CLOSED
        ]

    def regular(self):

        return [
            s
            for s in self._items
            if s.session_type == SessionType.REGULAR
        ]

    def to_list(self):

        return list(self._items)