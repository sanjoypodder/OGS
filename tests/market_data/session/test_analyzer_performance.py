"""
Performance tests.
"""

from ogs.market_data.session import (
    Session,
    SessionAnalyzer,
    SessionCollection,
    SessionStatus,
    SessionType,
)


def test_large_collection():

    collection = SessionCollection()

    for i in range(1000):

        collection.add(
            Session(
                session_id=str(i),
                name=f"Session {i}",
                exchange="NSE",
                market="Cash",
                status=SessionStatus.OPEN,
                session_type=SessionType.REGULAR,
            )
        )

    analyzer = SessionAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["session_analysis"]["active_sessions"]
        == 1000
    )