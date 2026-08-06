from decimal import Decimal

import pytest

from ogs.market.price import Price
from ogs.market.symbol import Symbol


def test_price_creation():
    p = Price(Symbol.XAUUSD, 3337.257)

    assert p.value == Decimal("3337.26")


def test_precision():
    p = Price(Symbol.EURUSD, 1.123456)

    assert p.value == Decimal("1.12346")


def test_add():
    p1 = Price(Symbol.XAUUSD, 10)

    p2 = Price(Symbol.XAUUSD, 5)

    assert (p1 + p2).value == Decimal("15.00")


def test_subtract():
    p1 = Price(Symbol.XAUUSD, 10)

    p2 = Price(Symbol.XAUUSD, 4)

    assert (p1 - p2).value == Decimal("6.00")


def test_tick():
    p = Price(Symbol.XAUUSD, 100)

    assert p.tick_size == Decimal("0.01")


def test_pip():
    p = Price(Symbol.XAUUSD, 100)

    assert p.pip_size == Decimal("0.10")


def test_invalid_symbol():
    gold = Price(Symbol.XAUUSD, 10)

    eur = Price(Symbol.EURUSD, 10)

    with pytest.raises(ValueError):
        _ = gold + eur