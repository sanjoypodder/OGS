"""
Tests for EngineRegistry.

Generated for {{PROJECT_NAME}}.
Module: {{MODULE_NAME}}
"""

from typing import Any

import pytest

from ogs.engine.base.base_engine import BaseEngine
from ogs.engine.base.engine_context import EngineContext
from ogs.engine.base.engine_registry import EngineRegistry
from ogs.engine.base.engine_result import EngineResult
from ogs.engine.base.exceptions import (
    DuplicateEngineError,
    EngineNotFoundError,
    EngineRegistrationError,
)


class StubEngine(BaseEngine[str]):
    """Simple engine used by registry tests."""

    def __init__(self, name: str = "test_engine") -> None:
        super().__init__(name)

    def _execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[str]:
        return EngineResult.ok(
            data=self.name
        )


def test_registry_starts_empty() -> None:
    """New registries should contain no engines."""

    registry = EngineRegistry()

    assert len(registry) == 0
    assert registry.names() == ()


def test_register_engine() -> None:
    """Engine instances should be registerable."""

    registry = EngineRegistry()
    engine = StubEngine()

    registry.register(engine)

    assert len(registry) == 1
    assert registry.contains("test_engine")
    assert registry.get("test_engine") is engine


def test_register_rejects_invalid_object() -> None:
    """Only BaseEngine instances may be registered."""

    registry = EngineRegistry()

    with pytest.raises(
        EngineRegistrationError,
        match="Only BaseEngine instances can be registered",
    ):
        registry.register(  # type: ignore[arg-type]
            object()
        )


def test_duplicate_registration_is_rejected() -> None:
    """Duplicate engine names should be rejected."""

    registry = EngineRegistry()

    registry.register(
        StubEngine("liquidity")
    )

    with pytest.raises(
        DuplicateEngineError,
        match="already registered",
    ):
        registry.register(
            StubEngine("liquidity")
        )


def test_registration_can_replace_existing_engine() -> None:
    """Replacement should be possible when explicitly requested."""

    registry = EngineRegistry()

    first = StubEngine("liquidity")
    second = StubEngine("liquidity")

    registry.register(first)

    registry.register(
        second,
        replace=True,
    )

    assert len(registry) == 1
    assert registry.get("liquidity") is second


def test_get_unknown_engine_raises() -> None:
    """Unknown engine lookups should fail clearly."""

    registry = EngineRegistry()

    with pytest.raises(
        EngineNotFoundError,
        match="is not registered",
    ):
        registry.get("missing")


def test_unregister_engine() -> None:
    """Registered engines should be removable."""

    registry = EngineRegistry()
    engine = StubEngine("risk")

    registry.register(engine)

    removed = registry.unregister("risk")

    assert removed is engine
    assert len(registry) == 0
    assert registry.contains("risk") is False


def test_unregister_unknown_engine_raises() -> None:
    """Removing an unknown engine should fail."""

    registry = EngineRegistry()

    with pytest.raises(
        EngineNotFoundError,
        match="is not registered",
    ):
        registry.unregister("missing")


def test_contains_normalizes_name() -> None:
    """Lookup names should be normalized."""

    registry = EngineRegistry()

    registry.register(
        StubEngine("market_structure")
    )

    assert registry.contains(
        "  market_structure  "
    )


def test_contains_operator() -> None:
    """Registry should support the in operator."""

    registry = EngineRegistry()

    registry.register(
        StubEngine("strategy")
    )

    assert "strategy" in registry
    assert "risk" not in registry
    assert 123 not in registry


def test_names_returns_registered_names() -> None:
    """names() should expose registered engine names."""

    registry = EngineRegistry()

    registry.register(
        StubEngine("liquidity")
    )

    registry.register(
        StubEngine("risk")
    )

    assert registry.names() == (
        "liquidity",
        "risk",
    )


def test_engines_returns_read_only_mapping() -> None:
    """Registry mapping should not be externally mutable."""

    registry = EngineRegistry()

    engine = StubEngine("execution")

    registry.register(engine)

    engines = registry.engines()

    assert engines["execution"] is engine

    with pytest.raises(TypeError):
        engines["new"] = StubEngine("new")  # type: ignore[index]


def test_registry_iteration() -> None:
    """Registry should iterate over engine instances."""

    registry = EngineRegistry()

    first = StubEngine("first")
    second = StubEngine("second")

    registry.register(first)
    registry.register(second)

    assert list(registry) == [
        first,
        second,
    ]


def test_clear_removes_all_engines() -> None:
    """clear() should empty the registry."""

    registry = EngineRegistry()

    registry.register(
        StubEngine("liquidity")
    )

    registry.register(
        StubEngine("risk")
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.names() == ()


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "   ",
    ],
)
def test_lookup_rejects_empty_name(
    name: str,
) -> None:
    """Empty lookup names should be rejected."""

    registry = EngineRegistry()

    with pytest.raises(
        EngineRegistrationError,
        match="Engine name cannot be empty or whitespace",
    ):
        registry.get(name)


def test_lookup_rejects_non_string_name() -> None:
    """Lookup names must be strings."""

    registry = EngineRegistry()

    with pytest.raises(
        EngineRegistrationError,
        match="Engine name must be a string",
    ):
        registry.get(123)  # type: ignore[arg-type]

