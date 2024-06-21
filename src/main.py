import asyncio
import sys
import subprocess
import utils.message_listener as ml
from events.eventHandler import eventHandler
# import ai.model as ai

async def main():
    eHandler = eventHandler()

    #task1 = asyncio.create_task(e.handleArrived())
    print("Starting NFC Reader Listener")
    task2 = asyncio.create_task(ml.reading_nfc(eHandler))
    # task3 = asyncio.create_task(ml.expecting_item_listener(data_queue))
    # task4 = asyncio.create_task(ai.startAI())
    print("Starting AI Listener")
    task5 = asyncio.create_task(ml.listen_to_ai(eHandler))

    #await task1
    await task2
    # await task3
    # await task4
    await task5


if __name__ == "__main__":
    asyncio.run(main())