"""
Tests for Session analyzer.
"""

from ogs.market_data.session import (
    Session,
    SessionAnalyzer,
    SessionCollection,
    SessionStatus,
    SessionType,
)


def test_analyze():

    collection = SessionCollection()

    collection.add(
        Session(
            session_id="1",
            name="Regular",
            exchange="NSE",
            market="Cash",
            status=SessionStatus.OPEN,
            session_type=SessionType.REGULAR,
        )
    )

    analyzer = SessionAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "session_analysis" in result
    assert "distribution_analysis" in result