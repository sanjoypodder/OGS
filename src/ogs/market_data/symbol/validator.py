"""
Validator for Symbol domain.
"""

from ogs.framework import (
    BaseAnalyzer,
    BaseCollection,
    BaseValidator,
)

from .domain import Symbol
from .enums import (
    Currency,
    Exchange,
    SymbolType,
    TradingStatus,
)


class SymbolValidator(BaseValidator):
    """
    Validates Symbol objects.
    """

    def validate(self, symbol: Symbol) -> bool:

        if symbol is None:
            return False

        if not isinstance(symbol, Symbol):
            return False

        if not symbol.symbol.strip():
            return False

        if not symbol.name.strip():
            return False

        if not isinstance(symbol.exchange, Exchange):
            return False

        if not isinstance(symbol.symbol_type, SymbolType):
            return False

        if not isinstance(symbol.base_currency, Currency):
            return False

        if not isinstance(symbol.quote_currency, Currency):
            return False

        if not isinstance(symbol.status, TradingStatus):
            return False

        if symbol.tick_size <= 0:
            return False

        if symbol.lot_size <= 0:
            return False

        return True