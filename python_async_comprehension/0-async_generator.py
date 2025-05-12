#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers after waiting 1 second.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:   # type: ignore
    """
    An asynchronous generator that loops 10 times, waiting 1 second
    between each iteration and yielding a random number between 0 and 10.
    Yields:
        int: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
