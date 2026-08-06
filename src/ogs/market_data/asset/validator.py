"""
OGS Smart Money AI

Asset Validator
"""

from __future__ import annotations

from datetime import datetime

from .domain import Asset
from .enums import AssetType


class AssetValidator:
    """
    Validator for Asset.
    """

    def __call__(
        self,
        asset: Asset,
    ) -> bool:

        if not isinstance(asset.asset_id, str) or not asset.asset_id.strip():
            raise ValueError("Invalid asset_id.")

        if not isinstance(asset.symbol, str) or not asset.symbol.strip():
            raise ValueError("Invalid symbol.")

        if not isinstance(asset.name, str) or not asset.name.strip():
            raise ValueError("Invalid name.")

        if not isinstance(asset.asset_type, AssetType):
            raise ValueError("Invalid asset type.")

        if not isinstance(asset.currency, str) or not asset.currency.strip():
            raise ValueError("Invalid currency.")

        if not isinstance(asset.active, bool):
            raise ValueError("Invalid active flag.")

        if not isinstance(asset.created_at, datetime):
            raise ValueError("Invalid created_at.")

        if not isinstance(asset.updated_at, datetime):
            raise ValueError("Invalid updated_at.")

        return True