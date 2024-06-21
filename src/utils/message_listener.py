import asyncio
import aiomqtt
import os
import json
import time
from utils.utils import get_token, readRFID
from events.eventHandler import eventHandler

PRODUCT_ARRIVED_STATUS_MESSAGE = os.getenv('PRODUCT_ARRIVED_STATUS_MESSAGE')
PRODUCT_IN_PROGRESS_STATUS_MESSAGE = os.getenv('PRODUCT_IN_PROGRESS_STATUS_MESSAGE')
PRODUCT_FINISHED_STATUS_MESSAGE = os.getenv('PRODUCT_FINISHED_STATUS_MESSAGE')
PRODUCT_IDLE_STATUS_MESSAGE = os.getenv('PRODUCT_IDLE_STATUS_MESSAGE')
STATION_IP = os.getenv('STATION_IP')
STATION_NAME = os.getenv('STATION_NAME')
BROKER_IP = os.getenv('BROKER_IP')
RFID_READER_PORT = os.getenv('RFID_READER_PORT')
TOPIC = os.getenv('STATUS_TOPIC_NAME')
RFID_TOPIC_NAME = os.getenv('RFID_TOPIC_NAME')


async def expecting_item_listener(expecting_items_queue, TOPIC):
    # Listening for messages of finished products from station befor
    url = "station/" + TOPIC

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.subscribe(url)
        async for message in client.messages:
            m = json.loads(message.payload)

            print("PRODUCT UPDATE RECEIVED: '{m}'")

            if m.get('status') == 'finished':
                expecting_items_queue.put(m.get('productID'))


async def listen_to_ai(eventHandler):
    url = "station/" + STATION_NAME + "/" + TOPIC

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.subscribe(url)
        async for message in client.messages:
            m = json.loads(message.payload)

            print("STATION AI UPDATE RECEIVED: '{m}'")

            if m.get('status') == 'arrived':
                await eventHandler.handleArrived()
            if m.get('status') == 'gone':
                await eventHandler.handleLeftStation()


async def reading_nfc(eHandler: eventHandler):
    # Listening for messages of RFID readers
    url = "station/" + STATION_NAME + "/io_link/ports/" + RFID_READER_PORT + "/data_translation/" + RFID_TOPIC_NAME

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.subscribe(url)
        async for message in client.messages:
            m = json.loads(message.payload)

            print("RFID READER UPDATE RECEIVED: '{m}'")

            if m.get('dataTranslation').get('event') == 'IN':
                value = m.get('dataTranslation').get('partID')
                await eHandler.handleInProgress(value)
            if m.get('dataTranslation').get('event') == 'OUT':
                value = m.get('dataTranslation').get('partID')
                await eHandler.handleFinished(value)
            
