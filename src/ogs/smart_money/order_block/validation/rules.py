"""
===========================================================

OGS Smart Money AI

Order Block Validation Rules

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OrderBlockRules:
    """
    Institutional Order Block rules.
    """

    minimum_displacement: float = 1.0

    require_liquidity_sweep: bool = True

    require_fresh_block: bool = True

    require_mss: bool = True