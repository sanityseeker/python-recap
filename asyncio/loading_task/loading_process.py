import itertools
import time
from multiprocessing import Process, Event

FPS = 5

def print_load(msg: str, sync_thr: Event) -> None:
    for smile in itertools.cycle(['(⊙﹏⊙)', '(Ф﹏Ф)']):
        status = f'\r{smile} {msg}'
        print(status, flush=True, end='')
        if sync_thr.wait(1. / FPS):
            break

    blanks = ' ' * 50
    print(f'\r{blanks}\r', end='')

def do_smth_slow() -> int:
    time.sleep(30)
    return 1337

def supervisor() -> int:
    sync_obj = Event()
    loading_icon_displayer = Process(target=print_load, args=('loading...', sync_obj))
    loading_icon_displayer.start()
    
    slow_result = do_smth_slow()
    sync_obj.set()
    loading_icon_displayer.join()
    return slow_result

def main() -> None:
    res = supervisor()
    print(f'Result is {res}')

if __name__ == '__main__':
    main()