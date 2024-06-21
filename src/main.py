import asyncio
import sys
import subprocess
import utils.message_listener as ml
from events.eventHandler import eventHandler
import ai.model as ai

async def main():
    data_queue = asyncio.Queue

    eHandler = eventHandler()

    #task1 = asyncio.create_task(e.handleArrived())
    task2 = asyncio.create_task(ml.reading_nfc(data_queue, eHandler))
    # task3 = asyncio.create_task(ml.expecting_item_listener(data_queue))
    task4 = asyncio.create_task(ai.startAI())

    #await task1
    await task2
    # await task3
    await task4


if __name__ == "__main__":
    asyncio.run(main())