from ogs.smart_money.mitigation import (
    MitigationBlockSeries,
)

from tests.factories.mitigation_factory import (
    make_bullish_mitigation,
)


def test_append():
    series = MitigationBlockSeries()

    series.append(
        make_bullish_mitigation()
    )

    assert len(series) == 1


def test_iteration():
    series = MitigationBlockSeries()

    series.append(
        make_bullish_mitigation()
    )

    assert list(series)