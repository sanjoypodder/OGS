from tests.factories.breaker_factory import (
    make_bearish_breaker,
    make_bullish_breaker,
)


def test_bullish_properties():
    breaker = make_bullish_breaker()

    assert breaker.is_bullish
    assert not breaker.is_bearish
    assert breaker.size == 6
    assert breaker.is_mitigated is False


def test_bearish_properties():
    breaker = make_bearish_breaker()

    assert breaker.is_bearish
    assert not breaker.is_bullish
    assert breaker.size == 7