import os
import sys
from logging import handlers

sys.path.append(os.path.join(os.getcwd(), '../..'))

from logs.logger import Logger
from init.constants import SERVER_LOG_DIR, SERVER_LOG_FILE


class ServerLogger(Logger):
    def __init__(self, name, log_dir, log_file):
        super().__init__(name, log_dir, log_file)

    def _add_file_handler(self):
        self.log_file = handlers.TimedRotatingFileHandler(self.path, encoding='utf8', interval=1, when='D')
        self.log_file.setFormatter(self.formatter)


logger = ServerLogger('server_dist', SERVER_LOG_DIR, SERVER_LOG_FILE).create()

if __name__ == '__main__':
    logger = ServerLogger('server_dist', SERVER_LOG_DIR, SERVER_LOG_FILE).create()
    logger.critical('Test critical event')
    logger.error('Test error ivent')
    logger.debug('Test debug ivent')
    logger.info('Test info ivent')
