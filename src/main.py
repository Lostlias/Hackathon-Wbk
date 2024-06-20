import events.eventHandler as e
import asyncio

async def main():
    await e.handleArrived()

if __name__ == "__main__":
    asyncio.run(main())