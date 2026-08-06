"""
Tests for SymbolValidator.
"""

import pytest

from ogs.market_data.symbol import (
    Currency,
    Exchange,
    Symbol,
    SymbolType,
    SymbolValidator,
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


def test_validator_accepts_valid_symbol():

    validator = SymbolValidator()

    assert validator.validate(create_symbol())


def test_validator_callable():

    validator = SymbolValidator()

    assert validator(create_symbol())


def test_validator_none():

    validator = SymbolValidator()

    assert validator.validate(None) is False


def test_invalid_symbol_name():

    validator = SymbolValidator()

    symbol = create_symbol()

    symbol = symbol.__class__(
        symbol="",
        name=symbol.name,
        exchange=symbol.exchange,
        symbol_type=symbol.symbol_type,
        base_currency=symbol.base_currency,
        quote_currency=symbol.quote_currency,
        tick_size=symbol.tick_size,
        lot_size=symbol.lot_size,
        status=symbol.status,
    )

    assert validator.validate(symbol) is False


def test_invalid_tick_size():

    validator = SymbolValidator()

    symbol = symbol = Symbol(
        symbol="EURUSD",
        name="Euro vs US Dollar",
        exchange=Exchange.FOREX,
        symbol_type=SymbolType.FOREX,
        base_currency=Currency.EUR,
        quote_currency=Currency.USD,
        tick_size=0,
        lot_size=100000,
        status=TradingStatus.ACTIVE,
    )

    assert validator.validate(symbol) is False


def test_invalid_lot_size():

    validator = SymbolValidator()

    symbol = Symbol(
        symbol="EURUSD",
        name="Euro vs US Dollar",
        exchange=Exchange.FOREX,
        symbol_type=SymbolType.FOREX,
        base_currency=Currency.EUR,
        quote_currency=Currency.USD,
        tick_size=0.0001,
        lot_size=0,
        status=TradingStatus.ACTIVE,
    )

    assert validator.validate(symbol) is False