#!/usr/bin/env python3

"""
Takes a string key 'k' and an integer or float value 'v' as arguments
and returns a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string key 'k' and an integer or float value 'v'
    as arguments and returns a tuple.

    Args:
        k (str): The key string.
        v (Union[int, float]): The value which can be an integer or a float.

    Returns:
        tuple[str, float]: A tuple containing the key string 'k' and the
        square of the value 'v' as a float.
    """
    return k, v**2
