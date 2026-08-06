from ogs.smart_money.breaker import (
    BreakerBlockSeries,
    BreakerBlockStatistics,
)

from tests.factories.breaker_factory import (
    make_bullish_breaker,
    make_bearish_breaker,
)


def test_statistics():
    series = BreakerBlockSeries()

    series.append(make_bullish_breaker())
    series.append(make_bearish_breaker())

    stats = BreakerBlockStatistics(series)

    assert stats.total == 2
    assert stats.bullish == 1
    assert stats.bearish == 1
    assert stats.mitigated == 0
    assert stats.unmitigated == 2