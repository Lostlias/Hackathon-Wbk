import asyncio
import json
import os
import sys
import aiomqtt


async def main():

    url = "172.22.192.101"

    topic = "station/Screwer1 (Manual)/io_link/ports/2/data_translation/status_light"

    payload = {

        "stationId": "Screwer1 (Manual)",

        "portId": "2",

        "segmentId": "all",

        "dataTranslation": {"color": "red", "blink": False, "blinkMode": "0"},

        "sentAt": "2024-06-20T11:48:16.251293113Z",
    }


    ## publishing
    payload_json = json.dumps(payload)

    async with aiomqtt.Client(url) as client:

        await client.publish(topic, payload=payload_json)

    print("published1")
    
    ##publish2 example simply publish 
    async with aiomqtt.Client(url) as client:

        await client.publish("station", "hello")

    print("published2")


    ## subscribing
    async with aiomqtt.Client(url) as client:

        await client.subscribe("station/Screwer1 (Manual)/#")

        async for message in client.messages:
            dict_message = json.loads(message.payload)
            print(dict_message)




if sys.platform.lower() == "win32" or os.name.lower()== "nt":

    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy

    set_event_loop_policy(WindowsSelectorEventLoopPolicy())




asyncio.run(main())