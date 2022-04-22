
import asyncio

async def printer(text: str):
    print(text)
    
async def sleeper(duration: int):
    print(f'sleeping for {duration} seconds')
    await asyncio.sleep(duration)

async def main():
    await sleeper(5)
    await printer('Woke up')
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
