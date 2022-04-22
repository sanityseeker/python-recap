import asyncio
import itertools
import time

FPS = 5

async def print_load(msg: str) -> None:
    for smile in itertools.cycle(['(⊙﹏⊙)', '(Ф﹏Ф)']):  # infinite loop
        status = f'\r{smile} {msg}'
        print(status, flush=True, end='')

        try:
            await asyncio.sleep(1 / FPS)
        except asyncio.CancelledError:
            print('Task is cancelled')
            break

    blanks = ' ' * 50
    print(f'\r{blanks}\r', end='')

async def do_smth_slow() -> int:
    await asyncio.sleep(30)
    # time.sleep(30)
    return 1337

async def supervisor() -> int:
    loading_icon_displayer = asyncio.create_task(print_load('loading...'))
    slow_result = await do_smth_slow()
    loading_icon_displayer.cancel()
    return slow_result

def main() -> None:
    res = asyncio.run(supervisor())
    print(f'Result is {res}')

if __name__ == '__main__':
    main()
