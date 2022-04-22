
import asyncio

async def printer(text: str):
    print(text)
    
async def sleeper(duration: int):
    await asyncio.sleep(duration)
    print(f'sleeping for {duration} seconds')

async def main():
    await sleeper(5)
    await printer('Woke up')

async def main():
    print('Running main')
    task_sleep = asyncio.create_task(sleeper(5))
    print('slept')
    task_print = asyncio.create_task(printer('woke up'))
    
    await task_sleep
    await task_print
    
    print('Finished main')


asyncio.run(main())
