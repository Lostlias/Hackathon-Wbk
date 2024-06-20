import asyncio
import json
import os
import sys
import aiomqtt
import datetime
import utils.light_control as lc
import utils.utils as u
from StationHandler import StationHandler

PRODUCT_ARRIVED_STATUS_MESSAGE = os.getenv('PRODUCT_ARRIVED_STATUS_MESSAGE')
PRODUCT_IN_PROGRESS_STATUS_MESSAGE = os.getenv('PRODUCT_IN_PROGRESS_STATUS_MESSAGE')
PRODUCT_FINISHED_STATUS_MESSAGE = os.getenv('PRODUCT_FINISHED_STATUS_MESSAGE')
PRODUCT_IDLE_STATUS_MESSAGE = os.getenv('PRODUCT_IDLE_STATUS_MESSAGE')
TOPIC_NAME = "ProductStatus"
STATION_NAME = os.getenv('STATION_NAME')
STATION_IP = os.getenv('STATION_IP')
BROKER_IP = os.getenv('BROKER_IP')
LEFT_LIGHT = os.getenv('LEFT_LIGHT_PORT')
RIGHT_LIGHT = os.getenv('RIGHT_LIGHT_PORT')

stationHander = StationHandler()

async def handleArrived(): # Ruft 
    await sendStatusMessage(PRODUCT_ARRIVED_STATUS_MESSAGE, None)

    #stationHander.addExpected(1) # TODO: remove dummy value

    # Change light to yellow
    # token = u.get_token(STATION_IP)
    # lc.ampel_orange(STATION_IP, LEFT_LIGHT, token)


async def handleInProgress(nfc_id):
    await sendStatusMessage(PRODUCT_IN_PROGRESS_STATUS_MESSAGE, nfc_id)

    # RFID Chip lesen



    # Change light to green
    token = u.get_token(STATION_IP)
    lc.ampel_grün(STATION_IP, LEFT_LIGHT, token)
    lc.ampel_grün(STATION_IP, RIGHT_LIGHT, token)


async def handleFinished():
    await sendStatusMessage(PRODUCT_FINISHED_STATUS_MESSAGE)

    # Change light to blue
    token = u.get_token(STATION_IP)
    lc.ampel_blau(STATION_IP, RIGHT_LIGHT, token)


async def handleIdleAgain():
    # Turn off lights
    token = u.get_token(STATION_IP)
    lc.ampel_aus(STATION_IP, LEFT_LIGHT, token)
    lc.ampel_aus(STATION_IP, RIGHT_LIGHT, token)


async def sendStatusMessage(status, productID):
    payload = {
        "stationId": STATION_NAME,
        "status": status,
        "productID": productID
    }

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.publish("station/{topic}".format(topic=TOPIC_NAME), payload=json.dumps(payload))



