"""Программа-сервер"""

import json
import os
import socket
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))

from init.constants import *
from init.utils import get_message, send_message
from logs.conf.server_log_config import logger


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    """
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 7777 -a 127.0.0.1
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        logger.error('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        logger.error('Номер порта может быть указано только в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = DEFAULT_IP_ADDRESS

    except IndexError:
        logger.error(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    logger.info(f'Старт сервера ip {listen_address}:{listen_port}')
    # Готовим сокет
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_address, listen_port))

    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        logger.info(f'Подключен клиент {client_address}')
        try:
            message_from_client = get_message(client)
            response = process_client_message(message_from_client)
            logger.debug(f'Разбор сообщения {message_from_client} клиента {client_address}')
            send_message(client, response)
            logger.debug(f'Клиенту {client_address} отправлен ответ {response}')
            client.close()
            logger.info(f'Соединение с клиентом {client_address} закрыто')
        except (ValueError, json.JSONDecodeError):
            logger.error('Принято некорректное сообщение от клиента.')
            client.close()
            logger.info(f'Соединение с клиентом {client_address} закрыто')


if __name__ == '__main__':
    main()
