"""
Tests for QuoteFactory.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteFactory,
    QuoteStatus,
    QuoteType,
)


def test_create():

    q = QuoteFactory.create(
        name="TEST",
        bid=100,
        ask=101,
        last=100.5,
    )

    assert isinstance(q, Quote)
    assert q.name == "TEST"


def test_live_factory():

    q = QuoteFactory.live("LIVE")

    assert q.quote_type == QuoteType.LIVE
    assert q.status == QuoteStatus.ACTIVE


def test_historical_factory():

    q = QuoteFactory.historical("HIST")

    assert q.quote_type == QuoteType.HISTORICAL
    assert q.status == QuoteStatus.ACTIVE


def test_simulated_factory():

    q = QuoteFactory.simulated("SIM")

    assert q.quote_type == QuoteType.SIMULATED
    assert q.status == QuoteStatus.ACTIVE


def test_clone():

    q1 = QuoteFactory.create(
        name="ABC",
        bid=10,
        ask=11,
    )

    q2 = QuoteFactory.clone(q1)

    assert q1 == q2
    assert q1 is not q2


def test_clone_independent():

    q1 = QuoteFactory.create(name="ABC")

    q2 = QuoteFactory.clone(q1)

    q2.name = "XYZ"

    assert q1.name == "ABC"
    assert q2.name == "XYZ"


def test_factory_validation():

    try:
        QuoteFactory.create(name="")
        assert False
    except ValueError:
        assert True