from ogs.smart_money.breaker import BreakerBlockSeries
from tests.factories.breaker_factory import (
    make_bullish_breaker,
)


def test_append():
    series = BreakerBlockSeries()

    series.append(make_bullish_breaker())

    assert len(series) == 1


def test_iteration():
    series = BreakerBlockSeries()

    series.append(make_bullish_breaker())

    assert list(series)