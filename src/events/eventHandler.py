import asyncio
import json
import os
import sys
import aiomqtt
import datetime
import utils.light_control as lc
import utils.utils as u
from StationHandler import StationHandler
import time

PRODUCT_ARRIVED_STATUS_MESSAGE = os.getenv('PRODUCT_ARRIVED_STATUS_MESSAGE')
PRODUCT_IN_PROGRESS_STATUS_MESSAGE = os.getenv('PRODUCT_IN_PROGRESS_STATUS_MESSAGE')
PRODUCT_FINISHED_STATUS_MESSAGE = os.getenv('PRODUCT_FINISHED_STATUS_MESSAGE')
PRODUCT_IDLE_STATUS_MESSAGE = os.getenv('PRODUCT_IDLE_STATUS_MESSAGE')
PRODUCT_LEFT_STATION_STATUS_MESSAGE = os.getenv('PRODUCT_LEFT_STATION_STATUS_MESSAGE')
TOPIC_NAME = "ProductStatus"
STATION_NAME = os.getenv('STATION_NAME')
STATION_IP = os.getenv('STATION_IP')
BROKER_IP = os.getenv('BROKER_IP')
LEFT_LIGHT = os.getenv('LEFT_LIGHT_PORT')
RIGHT_LIGHT = os.getenv('RIGHT_LIGHT_PORT')

stationHander = StationHandler()

async def handleArrived(): # Ruft 
    # TODO: implement prediction system that knows which products left the previous station
    predicted_product_id = None    

    await sendStatusMessage(PRODUCT_ARRIVED_STATUS_MESSAGE, predicted_product_id)

    stationHander.addExpected(predicted_product_id)

    # Change light to yellow
    token = u.get_token(STATION_IP)
    lc.ampel_orange(STATION_IP, LEFT_LIGHT, token)


async def handleInProgress(product_id):
    await sendStatusMessage(PRODUCT_IN_PROGRESS_STATUS_MESSAGE, product_id)

    stationHander.confirm(product_id)

    # Change light to green
    token = u.get_token(STATION_IP)
    lc.ampel_grün(STATION_IP, LEFT_LIGHT, token)

    # If no items are finished show only green
    if stationHander.rightQueueLen() == 0:
        lc.ampel_grün(STATION_IP, RIGHT_LIGHT, token)


async def handleFinished(product_id):
    await sendStatusMessage(PRODUCT_FINISHED_STATUS_MESSAGE, product_id)

    stationHander.finish(product_id)

    # Change light to blue
    token = u.get_token(STATION_IP)
    lc.ampel_blau(STATION_IP, RIGHT_LIGHT, token)


async def handleLeftStation():
    predicted_product_id = None

    await sendStatusMessage(PRODUCT_LEFT_STATION_STATUS_MESSAGE, predicted_product_id)

    stationHander.send(predicted_product_id)

    # Change light
    tocke = u.get_token(STATION_IP)
    lc.ampel_aus(STATION_IP, RIGHT_LIGHT, token)

    # Last item has left the station
    if stationHander.isIdle():
        handleIdleAgain()


async def handleIdleAgain():
    # Turn off lights
    token = u.get_token(STATION_IP)
    lc.ampel_aus(STATION_IP, LEFT_LIGHT, token)
    lc.ampel_aus(STATION_IP, RIGHT_LIGHT, token)


async def sendStatusMessage(status, productID):
    payload = {
        "stationId": STATION_NAME,
        "status": status,
        "productID": productID,
        "timestamp": datetime.datetime.now().strftime('%Y %m %d %H %M %S %f')
    }

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.publish("station/{topic}".format(topic=TOPIC_NAME), payload=json.dumps(payload))



