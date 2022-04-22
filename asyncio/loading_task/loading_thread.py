import itertools
import time
from threading import Event, Thread

FPS = 5

def print_load(msg: str, sync_thr: Event) -> None:
    for smile in itertools.cycle(['(⊙﹏⊙)', '(Ф﹏Ф)']):
        status = f'\r{smile} {msg}'
        print(status, flush=True, end='')
        if sync_thr.wait(1. / FPS):
            break

    blanks = ' ' * 20
    print(f'\r{blanks}\r', end='')

def do_smth_slow() -> int:
    time.sleep(30)
    return 1337

def supervisor() -> int:
    sync_obj = Event()
    loading_icon_displayer = Thread(target=print_load, args=('loading...', sync_obj))
    loading_icon_displayer.start()

    
    slow_result = do_smth_slow()  # Вызываем slow и блокируем main thread. Второ тред будет продолжать выполняться
    sync_obj.set()  # Ставим флаг, что результат получен, тем самым передаем сигнал загрузке, чтобы она остановилась
    loading_icon_displayer.join()
    return slow_result

def main() -> None:
    res = supervisor()
    print(f'Result is {res}')

if __name__ == '__main__':
    main()