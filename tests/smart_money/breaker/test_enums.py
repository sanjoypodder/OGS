from ogs.smart_money.breaker import BreakerBlockDirection


def test_bullish_enum():
    assert BreakerBlockDirection.BULLISH.value == "Bullish"


def test_bearish_enum():
    assert BreakerBlockDirection.BEARISH.value == "Bearish"