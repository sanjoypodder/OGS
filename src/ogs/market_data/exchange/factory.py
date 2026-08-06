"""
OGS Smart Money AI

Exchange Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Exchange
from .enums import ExchangeStatus
from .validator import ExchangeValidator


class ExchangeFactory(BaseFactory):
    """
    Factory for Exchange objects.
    """

    validator = ExchangeValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Exchange:

        exchange = Exchange(**kwargs)

        cls.validator(exchange)

        return exchange

    @classmethod
    def open(
        cls,
        **kwargs,
    ) -> Exchange:

        kwargs.setdefault(
            "status",
            ExchangeStatus.OPEN,
        )

        return cls.create(**kwargs)

    @classmethod
    def closed(
        cls,
        **kwargs,
    ) -> Exchange:

        kwargs.setdefault(
            "status",
            ExchangeStatus.CLOSED,
        )

        return cls.create(**kwargs)

    @classmethod
    def clone(
        cls,
        exchange: Exchange,
    ) -> Exchange:

        clone = deepcopy(exchange)

        cls.validator(clone)

        return clone