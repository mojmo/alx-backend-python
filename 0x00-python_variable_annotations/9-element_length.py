#!/usr/bin/env python3

"""
This script defines a function named element_length that calculates the
length of each sequence within an iterable and returns a list of tuples.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function iterates through an iterable containing sequences of any
    type and calculates the length of each sequence.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence from the input and its length.
    """

    return [(i, len(i)) for i in lst]
