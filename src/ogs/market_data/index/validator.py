"""
===========================================================

OGS Smart Money AI

Index Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Index
from .enums import (
    IndexStatus,
    IndexType,
)


class IndexValidator(
    BaseValidator[Index],
):
    """
    Index Validator.
    """

    def validate(
        self,
        value: Index,
    ) -> None:

        if not value.index_code.strip():
            raise ValueError(
                "Invalid index code."
            )

        if not value.index_name.strip():
            raise ValueError(
                "Invalid index name."
            )

        if not value.exchange.strip():
            raise ValueError(
                "Invalid exchange."
            )

        if not isinstance(
            value.index_type,
            IndexType,
        ):
            raise ValueError(
                "Invalid index type."
            )

        if not isinstance(
            value.status,
            IndexStatus,
        ):
            raise ValueError(
                "Invalid index status."
            )

        if value.base_value < 0:
            raise ValueError(
                "Invalid base value."
            )

        if value.current_value < 0:
            raise ValueError(
                "Invalid current value."
            )

        if value.constituent_count < 0:
            raise ValueError(
                "Invalid constituent count."
            )