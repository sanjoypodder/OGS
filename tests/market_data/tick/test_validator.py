"""
Tests for TickValidator.
"""

from datetime import datetime

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)
from ogs.market_data.tick.validator import TickValidator


def create_tick():

    return Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=1.1000,
        ask=1.1002,
        last=1.1001,
        volume=100,
        provider=ProviderType.FYERS,
    )


def test_validator_accepts_valid_tick():

    validator = TickValidator()

    assert validator.validate(create_tick())


def test_validator_callable():

    validator = TickValidator()

    assert validator(create_tick())


def test_none_tick():

    validator = TickValidator()

    assert validator.validate(None) is False


def test_empty_symbol():

    validator = TickValidator()

    tick = Tick(
        symbol="",
        timestamp=datetime.now(),
        bid=1,
        ask=2,
        last=1.5,
        volume=10,
        provider=ProviderType.FYERS,
    )

    assert validator.validate(tick) is False


def test_negative_bid():

    validator = TickValidator()

    tick = Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=-1,
        ask=2,
        last=1,
        volume=10,
        provider=ProviderType.FYERS,
    )

    assert validator.validate(tick) is False


def test_negative_ask():

    validator = TickValidator()

    tick = Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=1,
        ask=-2,
        last=1,
        volume=10,
        provider=ProviderType.FYERS,
    )

    assert validator.validate(tick) is False


def test_negative_last():

    validator = TickValidator()

    tick = Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=1,
        ask=2,
        last=-1,
        volume=10,
        provider=ProviderType.FYERS,
    )

    assert validator.validate(tick) is False


def test_negative_volume():

    validator = TickValidator()

    tick = Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=1,
        ask=2,
        last=1.5,
        volume=-1,
        provider=ProviderType.FYERS,
    )

    assert validator.validate(tick) is False


def test_bid_greater_than_ask():

    validator = TickValidator()

    tick = Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=2,
        ask=1,
        last=1.5,
        volume=10,
        provider=ProviderType.FYERS,
    )

    assert validator.validate(tick) is False