"""
Tests for Symbol domain.
"""

from ogs.market_data.symbol import (
    Symbol,
    SymbolType,
    Exchange,
    Currency,
    TradingStatus,
)


def create_symbol():

    return Symbol(
        symbol="EURUSD",
        name="Euro vs US Dollar",
        exchange=Exchange.FOREX,
        symbol_type=SymbolType.FOREX,
        base_currency=Currency.EUR,
        quote_currency=Currency.USD,
        tick_size=0.0001,
        lot_size=100000,
        status=TradingStatus.ACTIVE,
    )


def test_create_symbol():

    symbol = create_symbol()

    assert symbol.symbol == "EURUSD"


def test_is_active():

    symbol = create_symbol()

    assert symbol.is_active


def test_is_forex():

    symbol = create_symbol()

    assert symbol.is_forex


def test_not_crypto():

    symbol = create_symbol()

    assert not symbol.is_crypto


def test_not_stock():

    symbol = create_symbol()

    assert not symbol.is_stock


def test_not_index():

    symbol = create_symbol()

    assert not symbol.is_index


def test_not_commodity():

    symbol = create_symbol()

    assert not symbol.is_commodity


def test_display_name():

    symbol = create_symbol()

    assert symbol.display_name == "EURUSD (FOREX)"


def test_status():

    symbol = create_symbol()

    assert symbol.status is TradingStatus.ACTIVE