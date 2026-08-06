from datetime import UTC, datetime

from ogs.market.analysis.duplicate import Duplicate


def test_duplicate_creation():
    duplicate = Duplicate(
        index=3,
        timestamp=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
    )

    assert duplicate.index == 3


def test_duplicate_string():
    duplicate = Duplicate(
        index=1,
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
    )

    assert "Duplicate" in str(duplicate)