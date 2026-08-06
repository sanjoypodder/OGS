"""
===========================================================

OGS Smart Money AI

Metadata Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import (
    BaseValidator,
)

from .domain import Metadata
from .enums import (
    MetadataStatus,
    MetadataType,
    MetadataValueType,
)


class MetadataValidator(
    BaseValidator[Metadata],
):
    """
    Metadata Validator.
    """

    def validate(
        self,
        value: Metadata,
    ) -> None:

        if not value.metadata_id.strip():
            raise ValueError(
                "Invalid metadata id."
            )

        if not value.entity_type.strip():
            raise ValueError(
                "Invalid entity type."
            )

        if not value.entity_id.strip():
            raise ValueError(
                "Invalid entity id."
            )

        if not value.key.strip():
            raise ValueError(
                "Invalid metadata key."
            )

        if not isinstance(
            value.metadata_type,
            MetadataType,
        ):
            raise ValueError(
                "Invalid metadata type."
            )

        if not isinstance(
            value.value_type,
            MetadataValueType,
        ):
            raise ValueError(
                "Invalid value type."
            )

        if not isinstance(
            value.status,
            MetadataStatus,
        ):
            raise ValueError(
                "Invalid metadata status."
            )