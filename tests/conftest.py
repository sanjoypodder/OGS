"""
===========================================================

OGS Smart Money AI

Shared Pytest Configuration

Global reusable fixtures for the complete test suite.

===========================================================
"""

from __future__ import annotations

import pytest

from ogs.core.logger import configure_logger

from ogs.market import Timeframe

from tests.fixtures import (
    SymbolFactory,
    PriceFactory,
    CandleFactory,
    SwingFactory,
)


# ==========================================================
# Session Setup
# ==========================================================

@pytest.fixture(scope="session", autouse=True)
def configure_test_logger():
    """
    Configure the application logger once for the entire
    pytest session.
    """
    configure_logger()
    yield


# ==========================================================
# Symbol Fixtures
# ==========================================================

@pytest.fixture
def symbol():
    """Default testing symbol."""
    return SymbolFactory.default()


@pytest.fixture
def btc_symbol():
    return SymbolFactory.btc()


@pytest.fixture
def eth_symbol():
    return SymbolFactory.eth()


@pytest.fixture
def gold_symbol():
    return SymbolFactory.gold()


@pytest.fixture
def silver_symbol():
    return SymbolFactory.silver()


@pytest.fixture
def eurusd_symbol():
    return SymbolFactory.eurusd()


@pytest.fixture
def gbpusd_symbol():
    return SymbolFactory.gbpusd()


@pytest.fixture
def usdjpy_symbol():
    return SymbolFactory.usdjpy()


# ==========================================================
# Price Fixtures
# ==========================================================

@pytest.fixture
def price():
    """Default BTC price."""
    return PriceFactory.btc()


@pytest.fixture
def btc_price():
    return PriceFactory.btc()


@pytest.fixture
def eth_price():
    return PriceFactory.eth()


@pytest.fixture
def gold_price():
    return PriceFactory.gold()


@pytest.fixture
def silver_price():
    return PriceFactory.silver()


@pytest.fixture
def eurusd_price():
    return PriceFactory.eurusd()


@pytest.fixture
def gbpusd_price():
    return PriceFactory.gbpusd()


@pytest.fixture
def usdjpy_price():
    return PriceFactory.usdjpy()


# ==========================================================
# Candle Fixtures
# ==========================================================

@pytest.fixture
def candle():
    """Default BTC candle."""
    return CandleFactory.btc()


@pytest.fixture
def sample_candle():
    """
    Backward-compatible fixture for older tests.
    """
    return CandleFactory.btc()


@pytest.fixture
def bullish_candle():
    return CandleFactory.bullish()


@pytest.fixture
def bearish_candle():
    return CandleFactory.bearish()


@pytest.fixture
def doji_candle():
    return CandleFactory.doji()


@pytest.fixture
def gold_candle():
    return CandleFactory.gold()


@pytest.fixture
def eurusd_candle():
    return CandleFactory.eurusd()


@pytest.fixture
def candle_series():
    return CandleFactory.sequence(20)


@pytest.fixture
def m5_candle_series():
    return CandleFactory.sequence(
        count=20,
        timeframe=Timeframe.M5,
    )


@pytest.fixture
def h1_candle_series():
    return CandleFactory.sequence(
        count=20,
        timeframe=Timeframe.H1,
    )


# ==========================================================
# Swing Fixtures
# ==========================================================

@pytest.fixture
def swing():
    return SwingFactory.high()


@pytest.fixture
def high_swing():
    return SwingFactory.high()


@pytest.fixture
def low_swing():
    return SwingFactory.low()


@pytest.fixture
def higher_high():
    return SwingFactory.higher_high()


@pytest.fixture
def higher_low():
    return SwingFactory.higher_low()


@pytest.fixture
def lower_high():
    return SwingFactory.lower_high()


@pytest.fixture
def lower_low():
    return SwingFactory.lower_low()


@pytest.fixture
def strong_high():
    return SwingFactory.strong_high()


@pytest.fixture
def weak_high():
    return SwingFactory.weak_high()


@pytest.fixture
def strong_low():
    return SwingFactory.strong_low()


@pytest.fixture
def weak_low():
    return SwingFactory.weak_low()


@pytest.fixture
def swing_series():
    return SwingFactory.sequence()


# ==========================================================
# Utility Fixtures
# ==========================================================

@pytest.fixture
def empty_series():
    """Empty list used in collection tests."""
    return []


@pytest.fixture
def pivot_depth():
    """Default pivot depth for analyzer tests."""
    return 2