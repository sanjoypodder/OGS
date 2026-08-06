"""
OGS Smart Money AI

Quote Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Quote
from .enums import (
    QuoteStatus,
    QuoteType,
)
from .validator import QuoteValidator


class QuoteFactory(BaseFactory):
    """
    Factory for Quote objects.
    """

    _validator = QuoteValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Quote:

        quote = Quote(**kwargs)

        cls._validator.validate(
            quote
        )

        return quote

    @classmethod
    def live(
        cls,
        name: str,
    ) -> Quote:

        return cls.create(
            name=name,
            quote_type=QuoteType.LIVE,
            status=QuoteStatus.ACTIVE,
        )

    @classmethod
    def historical(
        cls,
        name: str,
    ) -> Quote:

        return cls.create(
            name=name,
            quote_type=QuoteType.HISTORICAL,
            status=QuoteStatus.ACTIVE,
        )

    @classmethod
    def simulated(
        cls,
        name: str,
    ) -> Quote:

        return cls.create(
            name=name,
            quote_type=QuoteType.SIMULATED,
            status=QuoteStatus.ACTIVE,
        )

    @classmethod
    def clone(
        cls,
        quote: Quote,
    ) -> Quote:

        return deepcopy(quote)