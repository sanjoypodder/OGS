from ogs.smart_money.flip_zone.analyzer import FlipZoneAnalyzer
from ogs.smart_money.flip_zone.factory import FlipZoneFactory


def test_factory():

    analyzer = FlipZoneFactory.create_analyzer()

    assert isinstance(analyzer, FlipZoneAnalyzer)