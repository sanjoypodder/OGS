"""
===========================================================

OGS Smart Money AI

Screener Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Screener
from .enums import (
    ScreenerStatus,
    ScreenerType,
)


class ScreenerFactory:
    """
    Screener Factory.
    """

    @staticmethod
    def create(
        screener_id: str,
        screener_name: str,
        **kwargs,
    ) -> Screener:

        return Screener(
            screener_id=screener_id,
            screener_name=screener_name,
            **kwargs,
        )

    @staticmethod
    def smart_money(
        screener_id: str,
        screener_name: str,
        **kwargs,
    ) -> Screener:

        return Screener(
            screener_id=screener_id,
            screener_name=screener_name,
            screener_type=ScreenerType.SMART_MONEY,
            status=ScreenerStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def ai(
        screener_id: str,
        screener_name: str,
        **kwargs,
    ) -> Screener:

        return Screener(
            screener_id=screener_id,
            screener_name=screener_name,
            screener_type=ScreenerType.AI,
            status=ScreenerStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        screener: Screener,
    ) -> Screener:

        return deepcopy(screener)