from ogs.smart_money.flip_zone.analyzer import FlipZoneAnalyzer
from ogs.smart_money.flip_zone.collection.flip_zone_collection import (
    FlipZoneCollection,
)


def test_empty_analysis():

    analyzer = FlipZoneAnalyzer()

    result = analyzer.analyze([])

    assert isinstance(result, FlipZoneCollection)
    assert len(result) == 0