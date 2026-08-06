"""
TradingHours Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import TradingHours
from .enums import (
    TradingHoursStatus,
    TradingHoursType,
)


class TradingHoursFactory:

    @staticmethod
    def create(**kwargs):

        return TradingHours(**kwargs)

    @staticmethod
    def regular(**kwargs):

        return TradingHours(
            trading_hours_type=TradingHoursType.REGULAR,
            status=TradingHoursStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def pre_market(**kwargs):

        return TradingHours(
            trading_hours_type=TradingHoursType.PRE_MARKET,
            status=TradingHoursStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def post_market(**kwargs):

        return TradingHours(
            trading_hours_type=TradingHoursType.POST_MARKET,
            status=TradingHoursStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def overnight(**kwargs):

        return TradingHours(
            trading_hours_type=TradingHoursType.OVERNIGHT,
            status=TradingHoursStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def extended(**kwargs):

        return TradingHours(
            trading_hours_type=TradingHoursType.EXTENDED,
            status=TradingHoursStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def custom(**kwargs):

        return TradingHours(
            trading_hours_type=TradingHoursType.CUSTOM,
            status=TradingHoursStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(obj):

        return deepcopy(obj)