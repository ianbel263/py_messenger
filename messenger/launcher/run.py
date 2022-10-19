import os
import subprocess
import sys
import time
import stat
import signal
from pprint import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from init.enums import Color, UserChoice

MAX_CLIENTS = 5

THIS_DIR = os.path.dirname(__file__)
PATH_TO_SERVER = '../app/server.py'
PATH_TO_CLIENT = '../app/client.py'


def get_subprocess(file_name, args=''):
    time.sleep(1)
    script_path = os.path.join(THIS_DIR, 'start_node.command')
    file_full_path = os.path.join(THIS_DIR, file_name)

    with open(script_path, "w") as f:
        f.write(f'#!/bin/sh\npython "{file_full_path}" {args}')
    os.chmod(script_path, stat.S_IRWXU)
    return subprocess.Popen(['/usr/bin/open', '-n', '-a', 'Terminal', script_path], shell=False)


def run():
    processes = []
    while True:
        user_choice = input(f'Выберите действие:\n'
                            f'{UserChoice.RUN.value} - запустить сервер и клиенты\n'
                            f'{UserChoice.EXIT.value} - выйти\n'
                            f'{UserChoice.CLOSE.value} - закрыть все окна\n'
                            f'Ваш выбор: ')
        match user_choice:
            case UserChoice.EXIT.value:
                break
            case UserChoice.RUN.value:
                processes.append(get_subprocess(PATH_TO_SERVER))
                for i in range(MAX_CLIENTS):
                    processes.append(get_subprocess(PATH_TO_CLIENT))
            case UserChoice.CLOSE.value:
                while processes:
                    victim = processes.pop()
                    victim.kill()
                sys.exit(0)
            case _:
                print(f'{Color.ERROR.value}Вы ввели неверный ответ. Попробуйте снова.')
                sys.stdout.write(Color.DEFAULT.value)


if __name__ == '__main__':
    run()
