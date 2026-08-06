"""
OGS Smart Money AI

Quote Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Quote
from .enums import (
    QuoteStatus,
    QuoteType,
)


class QuoteValidator(BaseValidator):
    """
    Validator for Quote objects.
    """

    def validate(
        self,
        quote: Quote,
    ) -> None:

        if not isinstance(quote, Quote):
            raise TypeError(
                "Expected Quote instance."
            )

        if not quote.name.strip():
            raise ValueError(
                "Quote name cannot be empty."
            )

        if not isinstance(
            quote.quote_type,
            QuoteType,
        ):
            raise ValueError(
                "Invalid quote type."
            )

        if not isinstance(
            quote.status,
            QuoteStatus,
        ):
            raise ValueError(
                "Invalid quote status."
            )

        numeric_fields = (
            quote.bid,
            quote.ask,
            quote.last,
            quote.bid_size,
            quote.ask_size,
            quote.open,
            quote.high,
            quote.low,
            quote.close,
            quote.volume,
        )

        if any(value < 0 for value in numeric_fields):
            raise ValueError(
                "Numeric values cannot be negative."
            )

        if not isinstance(
            quote.timestamp,
            datetime,
        ):
            raise ValueError(
                "Invalid timestamp."
            )

    def __call__(
        self,
        quote: Quote,
    ) -> None:
        self.validate(quote)