import asyncio
import json
import os
import sys
import aiomqtt

##portId = 2
##color = "red"

async def changeLights(portId, color):

    #url = "172.22.192.101"
    #topic = "station/Screwer1 (Manual)/io_link/ports/2/data_translation/status_light"   ##change to 'Joining 2 (Manual)'
    payload = {

        "stationId": "Screwer1 (Manual)",       ##change to 'Joining 2 (Manual)'
        "portId": portId,
        "segmentId": "all",
        "dataTranslation": {"color": color, "blink": False, "blinkMode": "0"},
        "sentAt": "2024-06-20T11:48:16.251293113Z",

    }
    
    return payload 

    ## publishing
    #payload_json = json.dumps(payload)
    #async with aiomqtt.Client(url) as client:

     #   await client.publish(topic, payload=payload_json)

    print("change lights")