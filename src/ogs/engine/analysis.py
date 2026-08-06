"""
===========================================================

OGS Smart Money AI

Analysis Result

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ogs.smart_money.swing import SwingSeries
from ogs.smart_money.bos import BOSSeries
from ogs.smart_money.choch import CHOCHSeries
from ogs.smart_money.mss import MSSSeries

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighSeries,
)
from ogs.smart_money.liquidity.equal_lows import (
    EqualLowSeries,
)
from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquiditySeries,
)
from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquiditySeries,
)
from ogs.smart_money.liquidity.sweep import (
    LiquiditySweepSeries,
)


@dataclass(frozen=True, slots=True)
class Analysis:
    """
    Complete Smart Money analysis result.
    """

    swings: SwingSeries = field(default_factory=lambda: SwingSeries([]))

    bos: BOSSeries = field(default_factory=lambda: BOSSeries([]))

    choch: CHOCHSeries = field(default_factory=lambda: CHOCHSeries([]))

    mss: MSSSeries = field(default_factory=lambda: MSSSeries([]))

    equal_highs: EqualHighSeries = field(
        default_factory=lambda: EqualHighSeries([])
    )

    equal_lows: EqualLowSeries = field(
        default_factory=lambda: EqualLowSeries([])
    )

    buy_side: BuySideLiquiditySeries = field(
        default_factory=lambda: BuySideLiquiditySeries([])
    )

    sell_side: SellSideLiquiditySeries = field(
        default_factory=lambda: SellSideLiquiditySeries([])
    )

    sweeps: LiquiditySweepSeries = field(
        default_factory=lambda: LiquiditySweepSeries([])
    )