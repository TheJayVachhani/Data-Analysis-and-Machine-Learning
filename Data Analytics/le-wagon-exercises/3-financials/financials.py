# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
import math
from math import e

def forward_price(spot, interest_rate, time):
    return round(spot * (e **(interest_rate * time)), 2)

# TODO: 2nd exercise: Define the `short_pnl` function
# sum of  all (position - mtm)
# both lists the same length
def short_pnl(positions, mtm):
    total_positions = sum(int(position) for position in positions)
    total_m = sum(int(m) for m in mtm)
    result = total_positions - total_m
    return result