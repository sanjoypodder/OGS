"""
===========================================================

OGS Smart Money AI

Universe Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Universe
from .enums import (
    UniverseStatus,
    UniverseType,
)


class UniverseFactory:
    """
    Universe Factory.
    """

    @staticmethod
    def create(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            **kwargs,
        )

    @staticmethod
    def exchange(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            universe_type=UniverseType.EXCHANGE,
            status=UniverseStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def index(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            universe_type=UniverseType.INDEX,
            status=UniverseStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def watchlist(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            universe_type=UniverseType.WATCHLIST,
            status=UniverseStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def screener(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            universe_type=UniverseType.SCREENER,
            status=UniverseStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def portfolio(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            universe_type=UniverseType.PORTFOLIO,
            status=UniverseStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def ai(
        universe_id: str,
        universe_name: str,
        **kwargs,
    ) -> Universe:

        return Universe(
            universe_id=universe_id,
            universe_name=universe_name,
            universe_type=UniverseType.AI,
            status=UniverseStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        universe: Universe,
    ) -> Universe:

        return deepcopy(universe)