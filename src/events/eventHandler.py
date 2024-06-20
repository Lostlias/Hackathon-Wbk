import asyncio
import json
import os
import sys
import aiomqtt

BROKER_IP = "172.22.192.101"
TOPIC_NAME = "ProductStatus"

STATION_NAME = os.getenv('STATION_NAME')

def handleArrived():
    # Send Message

    # Handle Lights
    pass

def handleIdleAgain():
    pass

async def sendMessage(status):
    payload = {
        "stationId": STATION_NAME,
        "status": status
    }

    async with aiomqtt.Client(BROKER_IP) as client:
        await client.publish("station/{topic}".format(topic=TOPIC_NAME), payload=str(payload))



