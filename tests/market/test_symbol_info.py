from decimal import Decimal

from ogs.market import SYMBOLS
from ogs.market import Symbol


def test_registry_contains_xauusd():
    assert Symbol.XAUUSD in SYMBOLS


def test_gold_precision():
    assert SYMBOLS[Symbol.XAUUSD].price_precision == 2


def test_gold_tick_size():
    assert SYMBOLS[Symbol.XAUUSD].tick_size == Decimal("0.01")


def test_forex_contract_size():
    assert SYMBOLS[Symbol.EURUSD].contract_size == 100000


def test_crypto_contract_size():
    assert SYMBOLS[Symbol.BTCUSD].contract_size == 1


def test_display_name():
    assert str(SYMBOLS[Symbol.XAUUSD]) == "Gold Spot"