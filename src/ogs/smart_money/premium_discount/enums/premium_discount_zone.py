"""
OGS FinOS

Premium / Discount Zone Enumeration

Defines the location of price within a dealing range.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from enum import Enum


class PremiumDiscountZone(str, Enum):
    """
    Represents the current price location inside a dealing range.

    Premium:
        Price is above equilibrium.

    Equilibrium:
        Price is near the midpoint (50%).

    Discount:
        Price is below equilibrium.
    """

    PREMIUM = "Premium"

    EQUILIBRIUM = "Equilibrium"

    DISCOUNT = "Discount"