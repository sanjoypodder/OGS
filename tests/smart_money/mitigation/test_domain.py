from tests.factories.mitigation_factory import (
    make_bearish_mitigation,
    make_bullish_mitigation,
)


def test_bullish_properties():
    mitigation = make_bullish_mitigation()

    assert mitigation.is_bullish
    assert not mitigation.is_bearish
    assert mitigation.size == 6
    assert mitigation.is_mitigated


def test_bearish_properties():
    mitigation = make_bearish_mitigation()

    assert mitigation.is_bearish
    assert not mitigation.is_bullish
    assert mitigation.size == 7