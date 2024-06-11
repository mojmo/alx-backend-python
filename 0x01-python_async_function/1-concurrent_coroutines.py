#!/usr/bin/env python3

"""
This script defines an asynchronous coroutine named wait_n that spawns
multiple wait_random coroutines concurrently and returns the delays in
ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This asynchronous coroutine spawns n instances of the wait_random
    coroutine concurrently. Each wait_random coroutine waits for a random
    delay between 0 and the specified max_delay (inclusive) in seconds.

    This coroutine then collects the delays from all spawned wait_random
    coroutines and ensures they are returned in ascending order without
    using the sort() function (which might not be efficient for concurrent
    data).

    Args:
        n (int): The number of wait_random coroutines to spawn concurrently.
        max_delay (int, optional): The maximum delay for each wait_random
            coroutine in seconds. Defaults to 10.

    Returns:
        List[float]: A list of delays (in ascending order) experienced by
            each spawned wait_random coroutine.
    """

    tasks = []
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        delay = await task
        delays.append(delay)

    # Ensure ascending order without sort using insertion sort
    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and delays[j] > key:
            delays[j + 1] = delays[j]
            j -= 1
            delays[j + 1] = key
    return delays
