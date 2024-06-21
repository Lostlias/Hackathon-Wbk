import asyncio
import aiomqtt
import os
import json
import time
from utils.utils import get_token, readRFID

PRODUCT_ARRIVED_STATUS_MESSAGE = os.getenv('PRODUCT_ARRIVED_STATUS_MESSAGE')
PRODUCT_IN_PROGRESS_STATUS_MESSAGE = os.getenv('PRODUCT_IN_PROGRESS_STATUS_MESSAGE')
PRODUCT_FINISHED_STATUS_MESSAGE = os.getenv('PRODUCT_FINISHED_STATUS_MESSAGE')
PRODUCT_IDLE_STATUS_MESSAGE = os.getenv('PRODUCT_IDLE_STATUS_MESSAGE')
STATION_IP = os.getenv('STATION_IP')
BROKER_IP = os.getenv('BROKER_IP')
RFID_READER_PORT = os.getenv('RFID_READER_PORT')
TOPIC = os.getenv('STATUS_TOPIC_NAME')
RFID_TOPIC = os.getenv('RFID_TOPIC_NAME')

async def expecting_item_listener(expecting_items_queue):
    # Listening for messages of finished products from station befor
    async with aiomqtt.Client(BROKER_IP) as client:
        await client.subscribe(TOPIC)
        async for message in client.messages:
            m = json.loads(message)

            if m.get('status') == 'finished':
                expecting_items_queue.put(m.get('productID'))


async def reading_nfc(data_queue):
    print("Starting RFID Loop")
    while True:
        data = readRFID(STATION_IP, RFID_READER_PORT)
        data_queue.put(data)

        time.sleep(0.5)

    # Listening for messages of RFID readers
    # async with aiomqtt.Client(BROKER_IP) as client:
    #    await client.subscribe(RFID_TOPIC)
    #    async for message in client.messages:
    #        m = json.loads(message)

    #        data_queue.put(m)
