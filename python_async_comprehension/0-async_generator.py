#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
import random


async def async_generator():
    """ The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

