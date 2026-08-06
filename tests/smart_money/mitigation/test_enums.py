from ogs.smart_money.mitigation import (
    MitigationBlockDirection,
)


def test_bullish_enum():
    assert MitigationBlockDirection.BULLISH.value == "Bullish"


def test_bearish_enum():
    assert MitigationBlockDirection.BEARISH.value == "Bearish"