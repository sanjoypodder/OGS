"""
===========================================================

OGS Smart Money AI

Index Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Index
from .enums import (
    IndexStatus,
    IndexType,
)


class IndexFactory:
    """
    Index Factory.
    """

    @staticmethod
    def create(
        index_code: str,
        index_name: str,
        exchange: str,
        **kwargs,
    ) -> Index:

        return Index(
            index_code=index_code,
            index_name=index_name,
            exchange=exchange,
            **kwargs,
        )

    @staticmethod
    def market_index(
        index_code: str,
        index_name: str,
        exchange: str,
        **kwargs,
    ) -> Index:

        return Index(
            index_code=index_code,
            index_name=index_name,
            exchange=exchange,
            index_type=IndexType.BROAD_MARKET,
            status=IndexStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def sector_index(
        index_code: str,
        index_name: str,
        exchange: str,
        **kwargs,
    ) -> Index:

        return Index(
            index_code=index_code,
            index_name=index_name,
            exchange=exchange,
            index_type=IndexType.SECTOR,
            status=IndexStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        index: Index,
    ) -> Index:

        return deepcopy(index)