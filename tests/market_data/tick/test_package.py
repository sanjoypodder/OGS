"""
Package tests for Tick module.
"""

from ogs.market_data.tick import (
    ProviderType,
    Tick,
    TickType,
)


def test_tick_import():

    assert Tick is not None


def test_tick_type_import():

    assert TickType is not None


def test_provider_type_import():

    assert ProviderType is not None


def test_tick_type_members():

    assert TickType.BID.value == "BID"
    assert TickType.ASK.value == "ASK"
    assert TickType.LAST.value == "LAST"
    assert TickType.MID.value == "MID"


def test_provider_members():

    assert ProviderType.FYERS.value == "FYERS"
    assert ProviderType.BINANCE.value == "BINANCE"
    assert ProviderType.BACKTEST.value == "BACKTEST"
    assert ProviderType.UNKNOWN.value == "UNKNOWN"