"""
OGS FinOS

Unit Tests

OTE Factory
"""

from ogs.smart_money.ote.analyzer import (
    OTEAnalyzer,
)
from ogs.smart_money.ote.factory import (
    OTEFactory,
)


def test_create_analyzer():

    analyzer = (
        OTEFactory.create_analyzer()
    )

    assert isinstance(
        analyzer,
        OTEAnalyzer,
    )


def test_factory_returns_new_instance():

    analyzer1 = (
        OTEFactory.create_analyzer()
    )

    analyzer2 = (
        OTEFactory.create_analyzer()
    )

    assert analyzer1 is not analyzer2