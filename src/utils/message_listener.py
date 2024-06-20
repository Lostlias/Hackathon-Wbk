import asyncio
import aiomqtt
import os
import json

PRODUCT_ARRIVED_STATUS_MESSAGE = os.getenv('PRODUCT_ARRIVED_STATUS_MESSAGE')
PRODUCT_IN_PROGRESS_STATUS_MESSAGE = os.getenv('PRODUCT_IN_PROGRESS_STATUS_MESSAGE')
PRODUCT_FINISHED_STATUS_MESSAGE = os.getenv('PRODUCT_FINISHED_STATUS_MESSAGE')
PRODUCT_IDLE_STATUS_MESSAGE = os.getenv('PRODUCT_IDLE_STATUS_MESSAGE')
BROKER_IP = os.getenv('BROKER_IP')
TOPIC = os.getenv('STATUS_TOPIC_NAME')

async def expecting_item_listener(expecting_items_queue):
    # Listening for messages of finished products from station befor
    async with aiomqtt.Client(BROKER_IP) as client:
        await client.subscribe(TOPIC)
        async for message in client.messages:
            m = json.loads(message)

            if m.get('status') == 'finished':
                expecting_items_queue.put(m.get('productID'))


async def reading_nfc():
    # Listening fro messages from the NFC Reader
    async with aiomqtt.Client(BROKER_IP) as Client:
        pass
