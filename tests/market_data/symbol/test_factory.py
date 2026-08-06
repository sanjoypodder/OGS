"""
Tests for SymbolFactory.
"""

import pytest

from ogs.market_data.symbol import (
    Currency,
    Exchange,
    SymbolFactory,
    SymbolType,
)


def test_create_symbol():

    symbol = SymbolFactory.create(
        symbol="EURUSD",
        name="Euro vs US Dollar",
        exchange=Exchange.FOREX,
        symbol_type=SymbolType.FOREX,
        base_currency=Currency.EUR,
        quote_currency=Currency.USD,
        tick_size=0.0001,
        lot_size=100000,
    )

    assert symbol.symbol == "EURUSD"


def test_symbol_uppercase():

    symbol = SymbolFactory.create(
        symbol="eurusd",
        name="Euro vs US Dollar",
        exchange=Exchange.FOREX,
        symbol_type=SymbolType.FOREX,
        base_currency=Currency.EUR,
        quote_currency=Currency.USD,
        tick_size=0.0001,
        lot_size=100000,
    )

    assert symbol.symbol == "EURUSD"


def test_forex_factory():

    symbol = SymbolFactory.forex(
        "EURUSD",
        Currency.EUR,
        Currency.USD,
    )

    assert symbol.is_forex


def test_crypto_factory():

    symbol = SymbolFactory.crypto(
        "BTCUSDT",
        Currency.BTC,
    )

    assert symbol.is_crypto


def test_stock_factory():

    symbol = SymbolFactory.stock(
        "TCS",
        "Tata Consultancy Services",
    )

    assert symbol.is_stock


def test_invalid_factory():

    with pytest.raises(ValueError):

        SymbolFactory.create(
            symbol="",
            name="",
            exchange=Exchange.FOREX,
            symbol_type=SymbolType.FOREX,
            base_currency=Currency.EUR,
            quote_currency=Currency.USD,
            tick_size=0,
            lot_size=0,
        )