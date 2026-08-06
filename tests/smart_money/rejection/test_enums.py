from ogs.smart_money.rejection import (
    RejectionBlockDirection,
)


def test_bullish_enum():
    assert RejectionBlockDirection.BULLISH.value == "Bullish"


def test_bearish_enum():
    assert RejectionBlockDirection.BEARISH.value == "Bearish"