"""
===========================================================

OGS Smart Money AI

Order Block Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import OrderBlock


class OrderBlockValidator(
    BaseValidator[OrderBlock]
):
    """
    Validates a confirmed Order Block.
    """

    def validate(
        self,
        order_block: OrderBlock,
    ):

        if order_block is None:
            raise ValueError(
                "Order Block cannot be None."
            )

        if order_block.origin_candle is None:
            raise ValueError(
                "Origin candle cannot be None."
            )

        if order_block.mss is None:
            raise ValueError(
                "MSS cannot be None."
            )

        if order_block.liquidity_sweep is None:
            raise ValueError(
                "Liquidity Sweep cannot be None."
            )