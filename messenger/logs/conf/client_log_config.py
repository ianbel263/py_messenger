import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from logs.logger import Logger
from init.constants import CLIENT_LOG_DIR, CLIENT_LOG_FILE


class ClientLogger(Logger):
    def __init__(self, name, log_dir, log_file):
        super().__init__(name, log_dir, log_file)

    def _add_file_handler(self):
        self.log_file = logging.FileHandler(self.path, encoding='utf8')
        self.log_file.setFormatter(self.formatter)


logger = ClientLogger('client_dist', CLIENT_LOG_DIR, CLIENT_LOG_FILE).create()

if __name__ == '__main__':
    logger = ClientLogger('client_dist', CLIENT_LOG_DIR, CLIENT_LOG_FILE).create()
    logger.critical('Test critical event')
    logger.error('Test error ivent')
    logger.debug('Test debug ivent')
    logger.info('Test info ivent')
