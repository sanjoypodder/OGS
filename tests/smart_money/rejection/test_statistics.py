from ogs.smart_money.rejection import (
    RejectionBlockSeries,
    RejectionBlockStatistics,
)

from tests.factories.rejection_factory import (
    make_bearish_rejection,
    make_bullish_rejection,
)


def test_statistics():
    series = RejectionBlockSeries()

    series.append(
        make_bullish_rejection()
    )

    series.append(
        make_bearish_rejection()
    )

    stats = RejectionBlockStatistics(
        series
    )

    assert stats.total == 2
    assert stats.bullish == 1
    assert stats.bearish == 1
    assert stats.confirmed == 2
    assert stats.unconfirmed == 0