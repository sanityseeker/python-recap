
import asyncio

async def get_data():
    print('getting data from somewhere')
    await asyncio.sleep(1.5)
    print('got data')
    return {'data': 'hooray!'}

async def sleeper_numbers(lenght: int, duration: float):
    for i in range(lenght):
        print(i)
        await asyncio.sleep(duration)
    
async def main():
    print('running main')
    task_sleep = asyncio.create_task(sleeper_numbers(15, 0.25))
    print('slept')
    task_data = asyncio.create_task(get_data())
    data = await task_data
    await task_sleep
    print('Got data', data)
    print('Finished main')
    
asyncio.run(main())
