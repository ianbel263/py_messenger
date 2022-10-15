"""Программа-клиент"""

import json
import os
import socket
import sys
import time

sys.path.append(os.path.join(os.getcwd(), '..'))

from init.constants import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from init.utils import get_message, send_message
from logs.conf.client_log_config import logger


def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """Загружаем параметы коммандной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        logger.error('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    logger.info(f'Запущен клиент с параметрами: адрес сервера - {server_address}; порт - {server_port}')
    # Инициализация сокета и обмен
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        transport.connect((server_address, server_port))
    except ConnectionRefusedError:
        logger.critical('Приложение сервера не запущено')
        exit(1)
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    logger.info(f'На сервер направлено сообщение: {message_to_server}')
    try:
        answer = process_ans(get_message(transport))
        logger.info(f'Получено сообщение от сервера {answer}')
    except (ValueError, json.JSONDecodeError):
        logger.critical('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
