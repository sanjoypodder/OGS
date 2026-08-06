"""
OGS Smart Money AI

Portfolio Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Portfolio
from .enums import (
    PortfolioStatus,
    PortfolioType,
)
from .validator import PortfolioValidator


class PortfolioFactory(BaseFactory):
    """
    Factory for Portfolio objects.
    """

    validator = PortfolioValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Portfolio:

        portfolio = Portfolio(**kwargs)

        cls.validator(portfolio)

        return portfolio

    @classmethod
    def live(
        cls,
        **kwargs,
    ) -> Portfolio:

        kwargs["portfolio_type"] = PortfolioType.LIVE
        kwargs.setdefault(
            "status",
            PortfolioStatus.ACTIVE,
        )

        return cls.create(**kwargs)

    @classmethod
    def paper(
        cls,
        **kwargs,
    ) -> Portfolio:

        kwargs["portfolio_type"] = PortfolioType.PAPER
        kwargs.setdefault(
            "status",
            PortfolioStatus.ACTIVE,
        )

        return cls.create(**kwargs)

    @classmethod
    def backtest(
        cls,
        **kwargs,
    ) -> Portfolio:

        kwargs["portfolio_type"] = PortfolioType.BACKTEST
        kwargs.setdefault(
            "status",
            PortfolioStatus.ACTIVE,
        )

        return cls.create(**kwargs)

    @classmethod
    def clone(
        cls,
        portfolio: Portfolio,
    ) -> Portfolio:

        clone = deepcopy(portfolio)

        cls.validator(clone)

        return clone