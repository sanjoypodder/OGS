"""
OGS FinOS

Flip Zone Collection

Container for Flip Zone objects.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from ogs.smart_money.flip_zone.domain.flip_zone import FlipZone
from ogs.smart_money.flip_zone.enums.flip_zone_status import FlipZoneStatus
from ogs.smart_money.flip_zone.enums.flip_zone_type import FlipZoneType


class FlipZoneCollection:
    """
    Collection of FlipZone objects.
    """

    def __init__(self, flip_zones: Iterable[FlipZone] | None = None) -> None:
        self._flip_zones: list[FlipZone] = list(flip_zones or [])

    def add(self, flip_zone: FlipZone) -> None:
        """
        Add a Flip Zone to the collection.
        """
        self._flip_zones.append(flip_zone)

    def extend(self, flip_zones: Iterable[FlipZone]) -> None:
        """
        Add multiple Flip Zones.
        """
        self._flip_zones.extend(flip_zones)

    def clear(self) -> None:
        """
        Remove all Flip Zones.
        """
        self._flip_zones.clear()

    def get_by_id(self, flip_zone_id: str) -> FlipZone | None:
        """
        Retrieve a Flip Zone by its unique ID.
        """
        return next(
            (zone for zone in self._flip_zones if zone.id == flip_zone_id),
            None,
        )

    def filter_by_type(
        self,
        flip_zone_type: FlipZoneType,
    ) -> list[FlipZone]:
        """
        Return all Flip Zones of the given type.
        """
        return [
            zone
            for zone in self._flip_zones
            if zone.type == flip_zone_type
        ]

    def filter_by_status(
        self,
        status: FlipZoneStatus,
    ) -> list[FlipZone]:
        """
        Return all Flip Zones with the specified status.
        """
        return [
            zone
            for zone in self._flip_zones
            if zone.status == status
        ]

    @property
    def bullish(self) -> list[FlipZone]:
        """
        Return all Bullish Flip Zones.
        """
        return self.filter_by_type(FlipZoneType.BULLISH)

    @property
    def bearish(self) -> list[FlipZone]:
        """
        Return all Bearish Flip Zones.
        """
        return self.filter_by_type(FlipZoneType.BEARISH)

    @property
    def active(self) -> list[FlipZone]:
        """
        Return all active Flip Zones.
        """
        return self.filter_by_status(FlipZoneStatus.ACTIVE)

    @property
    def confirmed(self) -> list[FlipZone]:
        """
        Return all confirmed Flip Zones.
        """
        return self.filter_by_status(FlipZoneStatus.CONFIRMED)

    @property
    def invalidated(self) -> list[FlipZone]:
        """
        Return all invalidated Flip Zones.
        """
        return self.filter_by_status(FlipZoneStatus.INVALIDATED)

    def __len__(self) -> int:
        return len(self._flip_zones)

    def __iter__(self) -> Iterator[FlipZone]:
        return iter(self._flip_zones)

    def __getitem__(self, index: int) -> FlipZone:
        return self._flip_zones[index]

    def __contains__(self, flip_zone: FlipZone) -> bool:
        return flip_zone in self._flip_zones

    def __bool__(self) -> bool:
        return bool(self._flip_zones)

    def to_list(self) -> list[FlipZone]:
        """
        Return a shallow copy of the collection.
        """
        return list(self._flip_zones)