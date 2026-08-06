"""
OGS Smart Money AI

Quote Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Quote
from .enums import QuoteStatus, QuoteType


class QuoteCollection(BaseCollection[Quote]):
    """
    Collection of Quote objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Quote]:
        """
        Compatibility property for existing tests.
        """
        return self._items

    def add(self, quote: Quote) -> None:
        self.append(quote)

    def active(self) -> list[Quote]:
        return [
            q
            for q in self
            if q.status == QuoteStatus.ACTIVE
        ]

    def inactive(self) -> list[Quote]:
        return [
            q
            for q in self
            if q.status != QuoteStatus.ACTIVE
        ]

    def by_type(
        self,
        quote_type: QuoteType,
    ) -> list[Quote]:
        return [
            q
            for q in self
            if q.quote_type == quote_type
        ]

    def by_provider(
        self,
        provider: str,
    ) -> list[Quote]:
        return [
            q
            for q in self
            if q.provider == provider
        ]

    def by_symbol(
        self,
        symbol: str,
    ) -> list[Quote]:
        return [
            q
            for q in self
            if q.symbol == symbol
        ]

    def find(
        self,
        name: str,
    ) -> Quote | None:
        return next(
            (
                q
                for q in self
                if q.name == name
            ),
            None,
        )

    def total_active(self) -> int:
        return len(self.active())

    def to_list(self) -> list[dict]:
        return [
            q.to_dict()
            for q in self
        ]