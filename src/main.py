import events.eventHandler as e
import asyncio
import sys
import subprocess
import utils.message_listener as ml

async def main():
    data_queue = asyncio.Queue

    task1 = asyncio.create_task(e.handleArrived())
    task2 = asyncio.create_task(ml.reading_nfc(data_queue))
    task3 = asyncio.create_task(ml.expecting_item_listener(data_queue))

    await task1
    await task2
    await task3


if __name__ == "__main__":
    asyncio.run(main())