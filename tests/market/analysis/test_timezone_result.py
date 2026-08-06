from ogs.market.analysis.timezone_result import TimezoneResult


def test_total():
    result = TimezoneResult(
        normalized=8,
        skipped=2,
    )

    assert result.total == 10


def test_values():
    result = TimezoneResult(
        normalized=3,
        skipped=1,
    )

    assert result.normalized == 3
    assert result.skipped == 1