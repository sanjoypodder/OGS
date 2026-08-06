"""
OGS Smart Money AI

Asset Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Asset
from .enums import AssetType


class AssetFactory:
    """
    Factory for Asset objects.
    """

    @staticmethod
    def create(
        asset_id: str,
        symbol: str,
        name: str,
        **kwargs,
    ) -> Asset:

        return Asset(
            asset_id=asset_id,
            symbol=symbol,
            name=name,
            **kwargs,
        )

    @staticmethod
    def equity(
        asset_id: str,
        symbol: str,
        name: str,
        **kwargs,
    ) -> Asset:

        return Asset(
            asset_id=asset_id,
            symbol=symbol,
            name=name,
            asset_type=AssetType.EQUITY,
            **kwargs,
        )

    @staticmethod
    def crypto(
        asset_id: str,
        symbol: str,
        name: str,
        **kwargs,
    ) -> Asset:

        return Asset(
            asset_id=asset_id,
            symbol=symbol,
            name=name,
            asset_type=AssetType.CRYPTO,
            **kwargs,
        )

    @staticmethod
    def forex(
        asset_id: str,
        symbol: str,
        name: str,
        **kwargs,
    ) -> Asset:

        return Asset(
            asset_id=asset_id,
            symbol=symbol,
            name=name,
            asset_type=AssetType.FOREX,
            **kwargs,
        )

    @staticmethod
    def commodity(
        asset_id: str,
        symbol: str,
        name: str,
        **kwargs,
    ) -> Asset:

        return Asset(
            asset_id=asset_id,
            symbol=symbol,
            name=name,
            asset_type=AssetType.COMMODITY,
            **kwargs,
        )

    @staticmethod
    def clone(
        asset: Asset,
    ) -> Asset:

        return deepcopy(asset)