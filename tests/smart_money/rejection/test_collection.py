from ogs.smart_money.rejection import (
    RejectionBlockSeries,
)

from tests.factories.rejection_factory import (
    make_bullish_rejection,
)


def test_append():
    series = RejectionBlockSeries()

    series.append(
        make_bullish_rejection()
    )

    assert len(series) == 1


def test_iteration():
    series = RejectionBlockSeries()

    series.append(
        make_bullish_rejection()
    )

    assert list(series)