"""
Analyzer for Symbol collections.
"""

from ogs.framework import (
    BaseAnalyzer,
    BaseCollection,
    BaseValidator,
)

from .collection import SymbolCollection


class SymbolAnalyzer(BaseAnalyzer):
    """
    Analyzer for SymbolCollection.
    """

    def analyze(self, collection: SymbolCollection):

        return {
            "count": len(collection),
            "active": len(self.active(collection)),
            "inactive": len(self.inactive(collection)),
            "forex": len(self.forex(collection)),
            "crypto": len(self.crypto(collection)),
            "stocks": len(self.stocks(collection)),
            "indices": len(self.indices(collection)),
            "commodities": len(self.commodities(collection)),
        }

    def active(self, collection: SymbolCollection):

        return collection.active()

    def inactive(self, collection: SymbolCollection):

        return collection.inactive()

    def forex(self, collection: SymbolCollection):

        return collection.forex()

    def crypto(self, collection: SymbolCollection):

        return collection.crypto()

    def stocks(self, collection: SymbolCollection):

        return collection.stocks()

    def indices(self, collection: SymbolCollection):

        return collection.indices()

    def commodities(self, collection: SymbolCollection):

        return collection.commodities()

    def exchanges(self, collection: SymbolCollection):

        return sorted(
            {
                item.exchange.value
                for item in collection
            }
        )

    def symbols(self, collection: SymbolCollection):

        return sorted(
            item.symbol
            for item in collection
        )

    def find(self, collection: SymbolCollection, symbol: str):

        return collection.find(symbol)