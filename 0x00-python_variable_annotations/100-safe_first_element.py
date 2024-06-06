#!/usr/bin/env python3

"""
This script defines a function named safe_first_element that attempts
to retrieve the first element from a sequence.

**Duck Typing:** While type annotations are used, this function relies
on duck typing to ensure the input sequence can be indexed using square
brackets `[]`. This doesn't guarantee the type of the element at index 0.
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function attempts to retrieve the first element from a sequence,
    handling the case of an empty sequence.

    Args:
        lst (Sequence[Any]): The input sequence, assumed to be indexable
        using square brackets `[]`.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        otherwise None.
    """

    if lst:
        return lst[0]
    else:
        return None
