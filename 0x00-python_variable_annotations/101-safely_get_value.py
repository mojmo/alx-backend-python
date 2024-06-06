#!/usr/bin/env python3

"""_summary_
This script defines a function named safely_get_value that attempts to
retrieve a value from a dictionary with a default value.

**Type Annotations:**

- `dct`: A dictionary-like object (`Mapping`) where keys can be of any type
        (`Any`) and values can be of any type (`T`).
- `key`: The key to be searched for in the dictionary (`Any`).
- `default`: An optional default value to return if the key is not found
        (`Union[T, None]`). The type of the default value should be compatible
        with the value type stored in the dictionary (`T`).
- `return`: The value associated with the key if found, otherwise the provided
        default value (`Union[None, T]`).
"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    This function retrieves a value from a dictionary-like object,
    handling the case of a missing key.

    Args:
        dct (Mapping): The input dictionary-like object.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return if
        the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found, otherwise
        the provided default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
