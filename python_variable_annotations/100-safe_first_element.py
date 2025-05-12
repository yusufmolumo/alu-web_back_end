#!/usr/bin/env python3
"""
This module provides a utility function to safely get the first element from a sequence.
If the sequence is empty, it returns None.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None

