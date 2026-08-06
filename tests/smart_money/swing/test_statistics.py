"""
===========================================================

OGS Smart Money AI

Swing Statistics Tests

===========================================================
"""

from ogs.smart_money.swing import SwingStatistics


def test_statistics_creation():

    statistics = SwingStatistics()

    assert statistics is not None