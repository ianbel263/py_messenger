import inspect
import os
import sys
from functools import wraps

sys.path.append(os.path.join(os.getcwd(), '..'))


def log(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'server.py' in sys.argv[0]:
            from logs.conf.server_log_config import logger
        else:
            from logs.conf.client_log_config import logger

        res = func(*args, **kwargs)
        logger.debug(f'Функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return res

    return wrap
