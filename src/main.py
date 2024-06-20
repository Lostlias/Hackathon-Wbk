import events.eventHandler as e
import asyncio

async def main():
    await e.sendMessage("TestStatus")

if __name__ == "__main__":
    asyncio.run(main())