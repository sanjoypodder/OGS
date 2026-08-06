"""
===========================================================

OGS Smart Money AI

Session Validator

===========================================================
"""

from __future__ import annotations

from datetime import time

from ogs.smart_money.base.validator import BaseValidator

from .domain import Session
from .enums import (
    SessionStatus,
    SessionType,
)


class SessionValidator(
    BaseValidator[Session],
):
    """
    Session Validator.
    """

    def validate(
        self,
        value: Session,
    ) -> None:

        if not value.session_id.strip():
            raise ValueError("Invalid session_id.")

        if not value.name.strip():
            raise ValueError("Invalid session name.")

        if not value.exchange.strip():
            raise ValueError("Invalid exchange.")

        if not value.market.strip():
            raise ValueError("Invalid market.")

        if not isinstance(
            value.session_type,
            SessionType,
        ):
            raise ValueError("Invalid session type.")

        if not isinstance(
            value.status,
            SessionStatus,
        ):
            raise ValueError("Invalid session status.")

        if (
            value.start_time is not None
            and not isinstance(
                value.start_time,
                time,
            )
        ):
            raise ValueError("Invalid start_time.")

        if (
            value.end_time is not None
            and not isinstance(
                value.end_time,
                time,
            )
        ):
            raise ValueError("Invalid end_time.")

        if not value.timezone.strip():
            raise ValueError("Invalid timezone.")