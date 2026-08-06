"""
Tests for CorporateEvent analyzer.
"""

from ogs.market_data.corporate_event import (
    CorporateEvent,
    CorporateEventAnalyzer,
    CorporateEventCollection,
    CorporateEventStatus,
    CorporateEventType,
)


def test_analyze():

    collection = CorporateEventCollection()

    collection.add(
        CorporateEvent(
            corporate_event_id="EV001",
            exchange="NSE",
            market="Equity",
            instrument="INFY",
            event_name="Dividend",
            corporate_event_type=CorporateEventType.DIVIDEND,
            status=CorporateEventStatus.ACTIVE,
        )
    )

    analyzer = CorporateEventAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "corporate_event_analysis" in result
    assert "distribution_analysis" in result