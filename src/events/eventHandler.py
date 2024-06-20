import asyncio
import json
import os
import sys
import aiomqtt

PRODUCT_ARRIVED_STATUS_MESSAGE = "arrived"
PRODUCT_IN_PROGRESS_STATUS_MESSAGE = "in_progress"
PRODUCT_FINISHED_STATUS_MESSAGE = "finished"
PRODUCT_IDLE_STATUS_MESSAGE = "idle"

TOPIC_NAME = "ProductStatus"
STATION_NAME = os.getenv('STATION_NAME')
BROKER_IP = os.getenv('BROKER_IP')

async def handleArrived():
    await sendMessage(PRODUCT_ARRIVED_STATUS_MESSAGE)


async def handleInProgress():
    await sendMessage(PRODUCT_IN_PROGRESS_STATUS_MESSAGE)


async def handleFinished():
    await sendMessage(PRODUCT_FINISHED_STATUS_MESSAGE)


async def handleIdleAgain():
    pass


async def sendMessage(status):
    payload = {
        "stationId": STATION_NAME,
        "status": status
    }

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.publish("station/{topic}".format(topic=TOPIC_NAME), payload=str(payload))



