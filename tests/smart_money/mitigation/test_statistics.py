from ogs.smart_money.mitigation import (
    MitigationBlockSeries,
    MitigationBlockStatistics,
)

from tests.factories.mitigation_factory import (
    make_bearish_mitigation,
    make_bullish_mitigation,
)


def test_statistics():
    series = MitigationBlockSeries()

    series.append(
        make_bullish_mitigation()
    )

    series.append(
        make_bearish_mitigation()
    )

    stats = MitigationBlockStatistics(
        series
    )

    assert stats.total == 2
    assert stats.bullish == 1
    assert stats.bearish == 1
    assert stats.mitigated == 2
    assert stats.unmitigated == 0