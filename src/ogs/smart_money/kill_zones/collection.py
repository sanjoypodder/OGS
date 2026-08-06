"""
OGS Smart Money AI
------------------

Kill Zone Collection

Stores multiple Kill Zone objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from collections.abc import Iterable

from ogs.smart_money.base.collection import BaseCollection

from .domain import KillZone
from .enums import (
    KillZoneStatus,
    KillZoneType,
    SessionType,
)


class KillZoneSeries(
    BaseCollection[KillZone],
):
    """
    Collection of Kill Zone objects.
    """

    def __init__(
        self,
        items: Iterable[KillZone] | None = None,
    ) -> None:

        super().__init__(items)

    def append(
        self,
        zone: KillZone,
    ) -> None:
        """
        Append a Kill Zone.
        """
        self._items.append(zone)

    def latest(
        self,
        count: int = 1,
    ) -> list[KillZone]:
        """
        Return latest Kill Zones.
        """
        return self._items[-count:]

    def active(
        self,
    ) -> list[KillZone]:
        """
        Return all active Kill Zones.
        """
        return [
            zone
            for zone in self._items
            if zone.active
        ]

    def by_zone(
        self,
        zone_type: KillZoneType,
    ) -> list[KillZone]:
        """
        Filter by Kill Zone type.
        """
        return [
            zone
            for zone in self._items
            if zone.zone == zone_type
        ]

    def by_session(
        self,
        session: SessionType,
    ) -> list[KillZone]:
        """
        Filter by trading session.
        """
        return [
            zone
            for zone in self._items
            if zone.session == session
        ]

    def by_status(
        self,
        status: KillZoneStatus,
    ) -> list[KillZone]:
        """
        Filter by Kill Zone status.
        """
        return [
            zone
            for zone in self._items
            if zone.status == status
        ]