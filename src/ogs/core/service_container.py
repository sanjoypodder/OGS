"""
===========================================================

Module:
    service_container.py

Purpose:
    Lightweight service registry for OGS.

Author:
    Om Ganapati Solution

===========================================================
"""

from __future__ import annotations

from typing import Any


class ServiceContainer:
    """
    Central registry for shared services.

    Examples
    --------
    container.register("logger", logger)

    logger = container.resolve("logger")
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """
        Register a service.

        Raises
        ------
        KeyError
            If the service name already exists.
        """

        if name in self._services:
            raise KeyError(
                f"Service '{name}' is already registered."
            )

        self._services[name] = service

    def resolve(self, name: str) -> Any:
        """
        Return a registered service.

        Raises
        ------
        KeyError
            If the service is not registered.
        """

        try:
            return self._services[name]

        except KeyError as ex:
            raise KeyError(
                f"Service '{name}' is not registered."
            ) from ex

    def has(self, name: str) -> bool:
        """
        Check whether a service exists.
        """

        return name in self._services

    def remove(self, name: str) -> None:
        """
        Remove a service.

        Raises
        ------
        KeyError
            If the service does not exist.
        """

        if name not in self._services:
            raise KeyError(
                f"Service '{name}' is not registered."
            )

        del self._services[name]

    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._services.clear()

    @property
    def count(self) -> int:
        """
        Number of registered services.
        """

        return len(self._services)