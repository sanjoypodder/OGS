"""
===========================================================

OGS Smart Money AI

Metadata Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    MetadataStatus,
    MetadataType,
    MetadataValueType,
)


@dataclass(slots=True)
class Metadata:
    """
    Metadata entity.
    """

    metadata_id: str = ""

    entity_type: str = ""

    entity_id: str = ""

    key: str = ""

    value: object = None

    value_type: MetadataValueType = (
        MetadataValueType.STRING
    )

    source: str = ""

    metadata_type: MetadataType = (
        MetadataType.UNKNOWN
    )

    status: MetadataStatus = (
        MetadataStatus.UNKNOWN
    )

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:

        return (
            self.active
            and self.status == MetadataStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.metadata_id.strip())
            and bool(self.entity_type.strip())
            and bool(self.entity_id.strip())
            and bool(self.key.strip())
        )

    def to_dict(self) -> dict:

        value_type = (
            self.value_type.value
            if isinstance(
                self.value_type,
                MetadataValueType,
            )
            else str(self.value_type)
        )

        metadata_type = (
            self.metadata_type.value
            if isinstance(
                self.metadata_type,
                MetadataType,
            )
            else str(self.metadata_type)
        )

        status = (
            self.status.value
            if isinstance(
                self.status,
                MetadataStatus,
            )
            else str(self.status)
        )

        return {
            "metadata_id": self.metadata_id,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "key": self.key,
            "value": self.value,
            "value_type": value_type,
            "source": self.source,
            "metadata_type": metadata_type,
            "status": status,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Metadata("
            f"id='{self.metadata_id}', "
            f"key='{self.key}')"
        )