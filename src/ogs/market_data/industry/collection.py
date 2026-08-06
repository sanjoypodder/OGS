"""
===========================================================

OGS Smart Money AI

Industry Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Industry
from .enums import IndustryType


class IndustryCollection(
    BaseCollection[Industry],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        industry: Industry,
    ) -> None:

        self._items.append(industry)

    def find(
        self,
        industry_code: str,
    ) -> Industry | None:

        for industry in self._items:

            if (
                industry.industry_code
                == industry_code
            ):
                return industry

        return None

    def by_type(
        self,
        industry_type: IndustryType,
    ):

        return [
            industry
            for industry in self._items
            if (
                industry.industry_type
                == industry_type
            )
        ]

    def active(self):

        return [
            industry
            for industry in self._items
            if industry.is_active
        ]

    def to_list(self):

        return list(self._items)