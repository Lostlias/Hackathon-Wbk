import events.eventHandler as e
import asyncio
import sys
import subprocess
import utils.message_listener as ml

async def startRFIDSubprocess():
    process = await asyncio.create_subprocess_exec(
        sys.executable, 'src/utils/rfid_reader.py',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    return process

async def read_from_subprocess(process, data_queue):
    while True:
        line = await process.stdout.readline()
        if line:
            notification = line.decode().strip()
            await data_queue.put(notification)
            print(f"Main process received: {notifiation}")
        else: 
            break

async def main():
    # Create data Queue
    data_queue = asyncio.Queue()

    process = await startRFIDSubprocess()

    reader_task = asyncio.create_task(read_from_subprocess(process, data_queue))
    
    handle = asyncio.create_task(e.handleArrived())

    await handle

    reader_taskn.cancel()
    try:
        await reader_task
    except asyncio.CancelledError:
        print("Reader task has been cancelled")

    process.terminate()
    await process.wait()

    # Create needed tasks
    #asyncio.create_task(ml.expecting_item_listener(data_queue=expecting_items_queue))


if __name__ == "__main__":
    asyncio.run(main())