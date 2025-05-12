#!/usr/bin/env python3
"""
This module contains a function that safely retrieves a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a mapping.

    Args:
        dct (Mapping): The dictionary-like mapping to retrieve the value from.
        key (Any): The key to search for.
        default (Union[T, None], optional): A default value if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
