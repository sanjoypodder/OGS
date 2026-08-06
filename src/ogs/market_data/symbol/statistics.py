"""
Statistics for Symbol collections.
"""

from .collection import SymbolCollection


class SymbolStatistics:
    """
    Statistics for SymbolCollection.
    """

    def __init__(self, collection: SymbolCollection):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def active_count(self):

        return len(self.collection.active())

    @property
    def inactive_count(self):

        return len(self.collection.inactive())

    @property
    def forex_count(self):

        return len(self.collection.forex())

    @property
    def crypto_count(self):

        return len(self.collection.crypto())

    @property
    def stock_count(self):

        return len(self.collection.stocks())

    @property
    def index_count(self):

        return len(self.collection.indices())

    @property
    def commodity_count(self):

        return len(self.collection.commodities())

    @property
    def exchanges(self):

        return sorted(
            {
                item.exchange.value
                for item in self.collection
            }
        )

    @property
    def symbols(self):

        return sorted(
            item.symbol
            for item in self.collection
        )