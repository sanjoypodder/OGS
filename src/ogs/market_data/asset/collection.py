"""
OGS Smart Money AI

Asset Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Asset
from .enums import AssetType


class AssetCollection(BaseCollection[Asset]):
    """
    Collection of Asset objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Asset]:
        return self._items

    def add(
        self,
        asset: Asset,
    ) -> None:
        self.append(asset)

    def find(
        self,
        asset_id: str,
    ) -> Asset | None:
        return next(
            (
                asset
                for asset in self
                if asset.asset_id == asset_id
            ),
            None,
        )

    def active(self) -> list[Asset]:
        return [
            asset
            for asset in self
            if asset.active
        ]

    def inactive(self) -> list[Asset]:
        return [
            asset
            for asset in self
            if not asset.active
        ]

    def equities(self) -> list[Asset]:
        return [
            asset
            for asset in self
            if asset.asset_type == AssetType.EQUITY
        ]

    def crypto(self) -> list[Asset]:
        return [
            asset
            for asset in self
            if asset.asset_type == AssetType.CRYPTO
        ]

    def forex(self) -> list[Asset]:
        return [
            asset
            for asset in self
            if asset.asset_type == AssetType.FOREX
        ]

    def commodities(self) -> list[Asset]:
        return [
            asset
            for asset in self
            if asset.asset_type == AssetType.COMMODITY
        ]

    def to_list(self) -> list[dict]:
        return [
            asset.to_dict()
            for asset in self
        ]