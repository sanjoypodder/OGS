"""
Collection for Symbol objects.
"""

from ogs.framework import (
    BaseAnalyzer,
    BaseCollection,
    BaseValidator,
)
from .domain import Symbol
from .enums import (
    Exchange,
    SymbolType,
)


class SymbolCollection(BaseCollection[Symbol]):
    """
    Collection of Symbol objects.
    """

    def append(self, symbol: Symbol) -> None:
        super().append(symbol)

    def by_exchange(self, exchange: Exchange):
        return SymbolCollection(
            item for item in self
            if item.exchange == exchange
        )

    def by_type(self, symbol_type: SymbolType):
        return SymbolCollection(
            item for item in self
            if item.symbol_type == symbol_type
        )

    def active(self):
        return SymbolCollection(
            item for item in self
            if item.is_active
        )

    def inactive(self):
        return SymbolCollection(
            item for item in self
            if not item.is_active
        )

    def forex(self):
        return self.by_type(SymbolType.FOREX)

    def crypto(self):
        return self.by_type(SymbolType.CRYPTO)

    def stocks(self):
        return self.by_type(SymbolType.STOCK)

    def indices(self):
        return self.by_type(SymbolType.INDEX)

    def commodities(self):
        return self.by_type(SymbolType.COMMODITY)

    def find(self, symbol: str):

        symbol = symbol.upper()

        for item in self:
            if item.symbol == symbol:
                return item

        return None 