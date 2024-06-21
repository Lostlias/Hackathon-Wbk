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

class eventHandler:

    def __init__(self):
        self.PRODUCT_ARRIVED_STATUS_MESSAGE = os.getenv('PRODUCT_ARRIVED_STATUS_MESSAGE')
        self.PRODUCT_IN_PROGRESS_STATUS_MESSAGE = os.getenv('PRODUCT_IN_PROGRESS_STATUS_MESSAGE')
        self.PRODUCT_FINISHED_STATUS_MESSAGE = os.getenv('PRODUCT_FINISHED_STATUS_MESSAGE')
        self.PRODUCT_IDLE_STATUS_MESSAGE = os.getenv('PRODUCT_IDLE_STATUS_MESSAGE')
        self.PRODUCT_LEFT_STATION_STATUS_MESSAGE = os.getenv('PRODUCT_LEFT_STATION_STATUS_MESSAGE')
        self.TOPIC_NAME = "ProductStatus"
        self.STATION_NAME = os.getenv('STATION_NAME')
        self.STATION_IP = os.getenv('STATION_IP')
        self.BROKER_IP = os.getenv('BROKER_IP')
        self.LEFT_LIGHT = os.getenv('LEFT_LIGHT_PORT')
        self.RIGHT_LIGHT = os.getenv('RIGHT_LIGHT_PORT')
        self.stationHander = StationHandler()

    async def handleArrived(self): # Ruft 
        # TODO: implement prediction system that knows which products left the previous station
        predicted_product_id = None    

        await self.sendStatusMessage(self.PRODUCT_ARRIVED_STATUS_MESSAGE, predicted_product_id)

        self.stationHander.addExpected(predicted_product_id)

        # Change light to yellow
        token = u.get_token(self.STATION_IP)
        lc.ampel_orange(self.STATION_IP, self.LEFT_LIGHT, token)


    async def handleInProgress(self, product_id):
        await self.sendStatusMessage(self.PRODUCT_IN_PROGRESS_STATUS_MESSAGE, product_id)

        self.stationHander.confirm(product_id)

        # Change light to green
        token = u.get_token(self.STATION_IP)
        lc.ampel_grün(self.STATION_IP, self.LEFT_LIGHT, token)

        # If no items are finished show only green
        if self.stationHander.rightQueueLen() == 0:
            lc.ampel_grün(self.STATION_IP, self.RIGHT_LIGHT, token)


    async def handleFinished(self, product_id):
        await self.sendStatusMessage(self.PRODUCT_FINISHED_STATUS_MESSAGE, product_id)

        self.stationHander.finish(product_id)

        # Change light to blue
        token = u.get_token(self.STATION_IP)
        lc.ampel_blau(self.STATION_IP, self.RIGHT_LIGHT, token)


    async def handleLeftStation(self):
        predicted_product_id = None

        await self.sendStatusMessage(self.PRODUCT_LEFT_STATION_STATUS_MESSAGE, predicted_product_id)

        self.stationHander.send(predicted_product_id)

        # Change light
        token = u.get_token(self.STATION_IP)
        lc.ampel_aus(self.STATION_IP, self.RIGHT_LIGHT, token)

        # Last item has left the station
        if self.stationHander.isIdle():
            handleIdleAgain()


    async def handleIdleAgain(self):
        # Turn off lights
        token = u.get_token(self.STATION_IP)
        lc.ampel_aus(self.STATION_IP, self.LEFT_LIGHT, token)
        lc.ampel_aus(self.STATION_IP, self.RIGHT_LIGHT, token)


    async def sendStatusMessage(self, status, productID):
        payload = {
            "stationId": self.STATION_NAME,
            "status": status,
            "productID": productID,
            "timestamp": datetime.datetime.now().strftime('%Y %m %d %H %M %S %f')
        }

        async with aiomqtt.Client(self.BROKER_IP) as client:
            await client.publish("station/{topic}".format(topic=self.TOPIC_NAME), payload=json.dumps(payload))



