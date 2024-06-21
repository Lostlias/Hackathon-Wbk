import events.eventHandler as e
import asyncio
import utils.message_listener as ml

async def main():
    # Create data Queue
    #expecting_items_queue = asyncio.Queue()

    # Create needed tasks
    #asyncio.create_task(ml.expecting_item_listener(data_queue=expecting_items_queue))
    asyncio.create_task(ml.reading_nfc())

    await e.handleArrived()

if __name__ == "__main__":
    asyncio.run(main())