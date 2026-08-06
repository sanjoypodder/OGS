"""
OGS FinOS

Unit Tests

Dealing Range Factory
"""

from ogs.smart_money.dealing_range.analyzer import (
    DealingRangeAnalyzer,
)
from ogs.smart_money.dealing_range.factory import (
    DealingRangeFactory,
)


def test_create_analyzer():

    analyzer = (
        DealingRangeFactory.create_analyzer()
    )

    assert isinstance(
        analyzer,
        DealingRangeAnalyzer,
    )


def test_factory_returns_new_instance():

    analyzer1 = (
        DealingRangeFactory.create_analyzer()
    )

    analyzer2 = (
        DealingRangeFactory.create_analyzer()
    )

    assert analyzer1 is not analyzer2