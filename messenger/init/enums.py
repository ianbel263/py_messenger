from enum import Enum


class Color(Enum):
    ERROR = '\033[1;31m'
    DEFAULT = '\033[0;0m'


class UserChoice(Enum):
    RUN = 'r'
    CLOSE = 'x'
    EXIT = 'q'
