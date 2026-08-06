"""
OGS Smart Money AI
------------------

Kill Zone Factory

Creates validated Kill Zone objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from datetime import datetime

from .domain import KillZone
from .enums import (
    KillZoneStatus,
    KillZoneType,
    SessionType,
    TimeZoneType,
)
from .validator import KillZoneValidator


class KillZoneFactory:
    """
    Factory for creating validated KillZone objects.
    """

    _validator = KillZoneValidator()

    @classmethod
    def create(
        cls,
        symbol: str,
        zone: KillZoneType,
        session: SessionType,
        status: KillZoneStatus,
        start_time: datetime,
        end_time: datetime,
        timezone: TimeZoneType = TimeZoneType.UTC,
        active: bool = False,
    ) -> KillZone:
        """
        Create a validated KillZone.
        """

        kill_zone = KillZone(
            symbol=symbol,
            zone=zone,
            session=session,
            status=status,
            start_time=start_time,
            end_time=end_time,
            timezone=timezone,
            active=active,
        )

        if not cls._validator.validate(kill_zone):
            raise ValueError("Invalid Kill Zone.")

        return kill_zone