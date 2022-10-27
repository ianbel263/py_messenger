import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from init.constants import LOGGING_LEVEL, SERVER_LOG_DIR, SERVER_LOG_FILE


class Logger:
    def __init__(self, name, log_dir, log_file):
        self.name = name
        self.log_file = None
        # Подготовка имени файла для логирования
        root = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(root, '..', log_dir, log_file)

        # создаём формировщик логов (formatter):
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

    def _add_stream_handlers(self):
        # создаём потоки вывода логов
        self.stream = logging.StreamHandler(sys.stderr)
        self.stream.setFormatter(self.formatter)
        self.stream.setLevel(logging.INFO)

    def _add_file_handler(self):
        pass

    def create(self):
        self._add_stream_handlers()
        self._add_file_handler()
        # создаём регистратор и настраиваем его
        logger = logging.getLogger(self.name)
        logger.addHandler(self.stream)
        if self.log_file is not None:
            logger.addHandler(self.log_file)
        logger.setLevel(LOGGING_LEVEL)
        return logger


if __name__ == '__main__':
    logger = Logger('server_dist', SERVER_LOG_DIR, SERVER_LOG_FILE).create()
    logger.critical('Test critical event')
    logger.error('Test error ivent')
    logger.debug('Test debug ivent')
    logger.info('Test info ivent')
