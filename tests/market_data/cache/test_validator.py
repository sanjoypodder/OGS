"""
Tests for CacheValidator.
"""

import pytest

from ogs.market_data.cache import (
    Cache,
    CacheFactory,
    CacheType,
    CacheValidator,
)


validator = CacheValidator()


def test_valid_cache():

    cache = CacheFactory.memory(
        "Memory Cache"
    )

    validator.validate(cache)


def test_empty_name():

    with pytest.raises(ValueError):

        validator.validate(
            Cache(name="")
        )


def test_negative_capacity():

    with pytest.raises(ValueError):

        validator.validate(
            Cache(
                name="Cache",
                capacity=-1,
            )
        )


def test_used_greater_than_capacity():

    with pytest.raises(ValueError):

        validator.validate(
            Cache(
                name="Cache",
                capacity=100,
                used=150,
            )
        )


def test_invalid_cache_type():

    with pytest.raises(TypeError):

        validator.validate(
            Cache(
                name="Cache",
                cache_type="MEMORY",
            )
        )


def test_invalid_object():

    with pytest.raises(TypeError):

        validator.validate(
            "Cache"
        )