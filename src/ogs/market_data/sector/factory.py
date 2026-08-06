"""
===========================================================

OGS Smart Money AI

Sector Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Sector
from .enums import (
    SectorStatus,
    SectorType,
)


class SectorFactory:
    """
    Sector Factory.
    """

    @staticmethod
    def create(
        sector_code: str,
        sector_name: str,
        **kwargs,
    ) -> Sector:

        return Sector(
            sector_code=sector_code,
            sector_name=sector_name,
            **kwargs,
        )

    @staticmethod
    def primary(
        sector_code: str,
        sector_name: str,
        **kwargs,
    ) -> Sector:

        return Sector(
            sector_code=sector_code,
            sector_name=sector_name,
            sector_type=SectorType.PRIMARY,
            status=SectorStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def thematic(
        sector_code: str,
        sector_name: str,
        **kwargs,
    ) -> Sector:

        return Sector(
            sector_code=sector_code,
            sector_name=sector_name,
            sector_type=SectorType.THEMATIC,
            status=SectorStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        sector: Sector,
    ) -> Sector:

        return deepcopy(sector)