"""
Analyzer distribution tests.
"""

from ogs.market_data.session import (
    Session,
    SessionAnalyzer,
    SessionCollection,
    SessionStatus,
    SessionType,
)


def test_distribution_detection():

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

    collection.add(
        Session(
            session_id="2",
            name="Pre",
            exchange="NSE",
            market="Cash",
            status=SessionStatus.CLOSED,
            session_type=SessionType.PRE_MARKET,
        )
    )

    analyzer = SessionAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert distribution["session_type"]["REGULAR"] == 1
    assert distribution["session_type"]["PRE_MARKET"] == 1