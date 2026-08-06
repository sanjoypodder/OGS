"""
===========================================================

OGS Smart Money AI

Industry Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Industry
from .enums import (
    IndustryStatus,
    IndustryType,
)


class IndustryFactory:
    """
    Industry Factory.
    """

    @staticmethod
    def create(
        industry_code: str,
        industry_name: str,
        sector_code: str,
        **kwargs,
    ) -> Industry:

        return Industry(
            industry_code=industry_code,
            industry_name=industry_name,
            sector_code=sector_code,
            **kwargs,
        )

    @staticmethod
    def manufacturing(
        industry_code: str,
        industry_name: str,
        sector_code: str,
        **kwargs,
    ) -> Industry:

        return Industry(
            industry_code=industry_code,
            industry_name=industry_name,
            sector_code=sector_code,
            industry_type=IndustryType.MANUFACTURING,
            status=IndustryStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def technology(
        industry_code: str,
        industry_name: str,
        sector_code: str,
        **kwargs,
    ) -> Industry:

        return Industry(
            industry_code=industry_code,
            industry_name=industry_name,
            sector_code=sector_code,
            industry_type=IndustryType.TECHNOLOGY,
            status=IndustryStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        industry: Industry,
    ) -> Industry:

        return deepcopy(industry)