import os
import subprocess
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))

from init.enums import Color, UserChoice

MAX_CLIENTS = 5
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(THIS_DIR)


def run_server(processes):
    processes.append(subprocess.Popen('python server.py', shell=True))


def run_clients(processes):
    for i in range(MAX_CLIENTS):
        processes.append(subprocess.Popen('python client.py', shell=True))


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
