Balanced Price Range (BPR) Documentation
OGS Smart Money AI

Module: ogs.smart_money.bpr

Version: 1.0.0

Overview

The Balanced Price Range (BPR) module identifies areas where a Bullish Fair Value Gap (FVG) and a Bearish Fair Value Gap (FVG) overlap.

These overlapping inefficiencies represent balanced zones where institutional buying and selling pressure have interacted. Such zones frequently act as:

Price magnets
Reaction zones
Continuation zones
Reversal zones
Institutional decision areas

The BPR module automatically detects these overlapping regions and stores them as immutable domain objects.

Architecture
ogs/
└── smart_money/
    └── bpr/
        ├── __init__.py
        ├── analyzer.py
        ├── collection.py
        ├── domain.py
        ├── enums.py
        ├── factory.py
        ├── statistics.py
        ├── validator.py
        └── README.md

The module follows the standard OGS Smart Money architecture.

Dependencies

The module depends on

FairValueGap
FairValueGapSeries
FairValueGapDirection
BaseAnalyzer
BaseCollection
BaseValidator

No external libraries are required.

Domain Model
BalancedPriceRange

Represents a single balanced price range.

Attributes
Attribute	Type	Description
bullish_gap	FairValueGap	Bullish FVG
bearish_gap	FairValueGap	Bearish FVG
direction	BalancedPriceRangeDirection	Dominant side
top	float	Upper boundary
bottom	float	Lower boundary
midpoint	float	Middle price
size	float	Range size
Direction
BalancedPriceRangeDirection

Supports

BULLISH
BEARISH
NEUTRAL
Collection
BalancedPriceRangeSeries

Stores multiple BPRs.

Supports

append()

first

last

latest(count)

iteration

len()

Example

series.append(bpr)

series.last

series.latest(5)
Factory
BalancedPriceRangeFactory

Creates validated domain objects.

Example

bpr = BalancedPriceRangeFactory.create(
    bullish_gap=bull_gap,
    bearish_gap=bear_gap,
    direction=BalancedPriceRangeDirection.BULLISH,
    top=1945,
    bottom=1939,
    midpoint=1942,
    size=6,
)
Validator
BalancedPriceRangeValidator

Checks

BPR exists
Bullish gap exists
Bearish gap exists
Direction exists
Top > Bottom
Size > 0

Returns

True

or

False
Statistics
BalancedPriceRangeStatistics

Provides

count

bullish_count

bearish_count

neutral_count

average_size

largest

smallest
Analyzer
BalancedPriceRangeAnalyzer

Input

FairValueGapSeries

Output

BalancedPriceRangeSeries
Detection Algorithm

Separate all FVGs

Bullish FVGs

Bearish FVGs

Compare every Bullish FVG against every Bearish FVG.

For each pair

overlap_top

= min(
    bullish.top,
    bearish.top,
)

overlap_bottom

= max(
    bullish.bottom,
    bearish.bottom,
)

If

overlap_top <= overlap_bottom

No BPR exists.

Otherwise

size

= overlap_top - overlap_bottom
midpoint

=

(overlap_top + overlap_bottom)/2

Determine direction

Bullish

if

bull.size >= bear.size

otherwise

Bearish

Create

BalancedPriceRange

Append into

BalancedPriceRangeSeries
Time Complexity

Let

B

=

number of Bullish FVGs

N

=

number of Bearish FVGs

Complexity

O(B × N)

Memory

O(K)

K = detected BPRs
Testing

The module is fully tested.

Test Summary
Test File	Result
Package	✅
Domain	✅
Collection	✅
Validator	✅
Factory	✅
Statistics	✅
Analyzer	✅

Total

34 Tests Passed
Integration Example
from ogs.smart_money.fair_value_gap import (
    FairValueGapAnalyzer,
)

from ogs.smart_money.bpr import (
    BalancedPriceRangeAnalyzer,
)

fvg_series = FairValueGapAnalyzer().analyze(candles)

bpr_series = BalancedPriceRangeAnalyzer().analyze(
    fvg_series
)

print(len(bpr_series))
Applications

Balanced Price Range detection is useful for:

Institutional trading
Smart Money Concepts (SMC)
ICT methodologies
Liquidity mapping
Order Block confirmation
Premium–Discount analysis
Market Structure Shift (MSS)
Change of Character (CHoCH)
Entry refinement
Multi-timeframe confluence
Future Enhancements

Planned improvements include:

Minimum overlap size filtering
Percentage overlap thresholds
Time-based overlap validation
Multi-timeframe BPR detection
Nested BPR identification
BPR visualization on charts
Volume and order-flow weighting
Liquidity-aware BPR ranking
Machine learning–based BPR quality scoring
Module Status
Item	Status
Architecture	✅ Complete
Implementation	✅ Complete
Validation	✅ Complete
Unit Testing	✅ 34/34 Passed
Documentation	✅ Complete
Production Ready	✅ Yes

Balanced Price Range (BPR) is now a complete, documented, and production-ready module within the OGS Smart Money AI framework.