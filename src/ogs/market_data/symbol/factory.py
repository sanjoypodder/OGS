"""
Factory for Symbol objects.
"""

from .domain import Symbol
from .enums import (
    Currency,
    Exchange,
    SymbolType,
    TradingStatus,
)
from .validator import SymbolValidator


class SymbolFactory:
    """
    Creates validated Symbol instances.
    """

    _validator = SymbolValidator()

    @classmethod
    def create(
        cls,
        symbol: str,
        name: str,
        exchange: Exchange,
        symbol_type: SymbolType,
        base_currency: Currency,
        quote_currency: Currency,
        tick_size: float,
        lot_size: float,
        status: TradingStatus = TradingStatus.ACTIVE,
    ) -> Symbol:

        obj = Symbol(
            symbol=symbol.upper(),
            name=name,
            exchange=exchange,
            symbol_type=symbol_type,
            base_currency=base_currency,
            quote_currency=quote_currency,
            tick_size=tick_size,
            lot_size=lot_size,
            status=status,
        )

        if not cls._validator.validate(obj):
            raise ValueError("Invalid Symbol")

        return obj

    @classmethod
    def forex(
        cls,
        symbol: str,
        base: Currency,
        quote: Currency,
    ) -> Symbol:

        return cls.create(
            symbol=symbol,
            name=symbol,
            exchange=Exchange.FOREX,
            symbol_type=SymbolType.FOREX,
            base_currency=base,
            quote_currency=quote,
            tick_size=0.0001,
            lot_size=100000,
        )

    @classmethod
    def crypto(
        cls,
        symbol: str,
        base: Currency,
        quote: Currency = Currency.USDT,
    ) -> Symbol:

        return cls.create(
            symbol=symbol,
            name=symbol,
            exchange=Exchange.BINANCE,
            symbol_type=SymbolType.CRYPTO,
            base_currency=base,
            quote_currency=quote,
            tick_size=0.01,
            lot_size=1,
        )

    @classmethod
    def stock(
        cls,
        symbol: str,
        name: str,
        exchange: Exchange = Exchange.NSE,
    ) -> Symbol:

        return cls.create(
            symbol=symbol,
            name=name,
            exchange=exchange,
            symbol_type=SymbolType.STOCK,
            base_currency=Currency.INR,
            quote_currency=Currency.INR,
            tick_size=0.05,
            lot_size=1,
        )