"""
OGS Smart Money AI

Broker Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Broker
from .enums import BrokerStatus
from .validator import BrokerValidator


class BrokerFactory(BaseFactory):
    """
    Factory for Broker objects.
    """

    validator = BrokerValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Broker:

        broker = Broker(**kwargs)

        cls.validator(
            broker
        )

        return broker

    @classmethod
    def active(
        cls,
        **kwargs,
    ) -> Broker:

        kwargs.setdefault(
            "status",
            BrokerStatus.ACTIVE,
        )

        return cls.create(
            **kwargs
        )

    @classmethod
    def inactive(
        cls,
        **kwargs,
    ) -> Broker:

        kwargs.setdefault(
            "status",
            BrokerStatus.INACTIVE,
        )

        return cls.create(
            **kwargs
        )

    @classmethod
    def clone(
        cls,
        broker: Broker,
    ) -> Broker:

        clone = deepcopy(
            broker
        )

        cls.validator(
            clone
        )

        return clone