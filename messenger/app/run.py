import os
import subprocess
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from init.enums import Color, UserChoice

MAX_CLIENTS = 5

THIS_DIR = os.path.dirname(__file__)
PATH_TO_SERVER = os.path.join(THIS_DIR, 'server.py')
PATH_TO_CLIENT = os.path.join(THIS_DIR, 'client.py')


def run_server(processes):
    processes.append(subprocess.Popen(f"open -n -a Terminal.app '{PATH_TO_SERVER}'", shell=True))


def run_clients(processes):
    for i in range(MAX_CLIENTS):
        processes.append(subprocess.Popen(f"open -n -a Terminal.app '{PATH_TO_CLIENT}'", shell=True))
        time.sleep(0.5)


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
                run_server(processes)
                time.sleep(1)
                run_clients(processes)
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
