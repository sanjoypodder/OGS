"""
Domain model for tradable market symbols.
"""

from dataclasses import dataclass

from .enums import (
    Currency,
    Exchange,
    SymbolType,
    TradingStatus,
)


@dataclass(frozen=True, slots=True)
class Symbol:
    """
    Represents a tradable financial instrument.
    """

    symbol: str
    name: str
    exchange: Exchange
    symbol_type: SymbolType
    base_currency: Currency
    quote_currency: Currency
    tick_size: float
    lot_size: float
    status: TradingStatus = TradingStatus.ACTIVE

    @property
    def is_active(self) -> bool:
        return self.status == TradingStatus.ACTIVE

    @property
    def is_forex(self) -> bool:
        return self.symbol_type == SymbolType.FOREX

    @property
    def is_crypto(self) -> bool:
        return self.symbol_type == SymbolType.CRYPTO

    @property
    def is_stock(self) -> bool:
        return self.symbol_type == SymbolType.STOCK

    @property
    def is_index(self) -> bool:
        return self.symbol_type == SymbolType.INDEX

    @property
    def is_commodity(self) -> bool:
        return self.symbol_type == SymbolType.COMMODITY

    @property
    def display_name(self) -> str:
        return f"{self.symbol} ({self.exchange.value})"