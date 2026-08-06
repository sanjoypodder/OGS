"""
===========================================================

OGS Smart Money AI

SMT Divergence Package Tests

===========================================================
"""

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergence,
    SMTDivergenceAnalyzer,
    SMTDivergenceDirection,
    SMTDivergenceFactory,
    SMTDivergenceSeries,
    SMTDivergenceStatistics,
    SMTDivergenceValidator,
)


def test_package_exports():

    assert SMTDivergence is not None
    assert SMTDivergenceSeries is not None
    assert SMTDivergenceAnalyzer is not None
    assert SMTDivergenceValidator is not None
    assert SMTDivergenceFactory is not None
    assert SMTDivergenceStatistics is not None

    assert SMTDivergenceDirection is not None
    assert SMTComparisonType is not None
    assert SMTConfidence is not None


def test_package_instantiation():

    analyzer = SMTDivergenceAnalyzer()

    validator = SMTDivergenceValidator()

    series = SMTDivergenceSeries()

    stats = SMTDivergenceStatistics(series)

    assert analyzer is not None
    assert validator is not None
    assert series is not None
    assert stats is not None