#!/usr/bin/env python3
"""Return values with the appropriate types"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
