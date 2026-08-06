"""
===========================================================

OGS Smart Money AI

Metadata Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Metadata
from .enums import (
    MetadataStatus,
    MetadataType,
)


class MetadataFactory:
    """
    Metadata Factory.
    """

    @staticmethod
    def create(
        metadata_id: str,
        entity_type: str,
        entity_id: str,
        key: str,
        value,
        **kwargs,
    ) -> Metadata:

        return Metadata(
            metadata_id=metadata_id,
            entity_type=entity_type,
            entity_id=entity_id,
            key=key,
            value=value,
            **kwargs,
        )

    @staticmethod
    def system(
        metadata_id: str,
        entity_type: str,
        entity_id: str,
        key: str,
        value,
        **kwargs,
    ) -> Metadata:

        return Metadata(
            metadata_id=metadata_id,
            entity_type=entity_type,
            entity_id=entity_id,
            key=key,
            value=value,
            metadata_type=MetadataType.SYSTEM,
            status=MetadataStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def market(
        metadata_id: str,
        entity_type: str,
        entity_id: str,
        key: str,
        value,
        **kwargs,
    ) -> Metadata:

        return Metadata(
            metadata_id=metadata_id,
            entity_type=entity_type,
            entity_id=entity_id,
            key=key,
            value=value,
            metadata_type=MetadataType.MARKET,
            status=MetadataStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def smart_money(
        metadata_id: str,
        entity_type: str,
        entity_id: str,
        key: str,
        value,
        **kwargs,
    ) -> Metadata:

        return Metadata(
            metadata_id=metadata_id,
            entity_type=entity_type,
            entity_id=entity_id,
            key=key,
            value=value,
            metadata_type=MetadataType.SMART_MONEY,
            status=MetadataStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def ai(
        metadata_id: str,
        entity_type: str,
        entity_id: str,
        key: str,
        value,
        **kwargs,
    ) -> Metadata:

        return Metadata(
            metadata_id=metadata_id,
            entity_type=entity_type,
            entity_id=entity_id,
            key=key,
            value=value,
            metadata_type=MetadataType.AI,
            status=MetadataStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        metadata: Metadata,
    ) -> Metadata:

        return deepcopy(metadata)