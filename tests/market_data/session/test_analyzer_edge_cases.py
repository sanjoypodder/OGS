"""
Analyzer edge cases.
"""

from ogs.market_data.session import (
    SessionAnalyzer,
    SessionCollection,
)


def test_empty_collection():

    analyzer = SessionAnalyzer()

    result = analyzer.analyze(
        SessionCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = SessionAnalyzer()

    result = analyzer.analyze(
        SessionCollection()
    )

    distribution = result["distribution_analysis"]["session_type"]

    assert isinstance(distribution, dict)