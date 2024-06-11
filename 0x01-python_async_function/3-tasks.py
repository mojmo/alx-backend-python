#!/usr/bin/env python3

"""creates and returns an asyncio.Task"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function creates and returns an asyncio.Task that will call
    the wait_random coroutine with the specified max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine
            in seconds.

    Returns:
        asyncio.Task: The created asyncio.Task object.
    """

    return asyncio.create_task(wait_random(max_delay))
