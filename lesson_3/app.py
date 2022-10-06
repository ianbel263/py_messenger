import sys

from init.enums import Color

MIN_PYTHON_VERSION = '3.10'

if __name__ == '__main__':
    try:
        assert sys.version_info >= tuple(map(int, MIN_PYTHON_VERSION.split('.')))
        from app.run import run

        run()
    except AssertionError:
        sys.exit(f'{Color.ERROR.value}Необходимо установить интерпретатор Python не ниже версии {MIN_PYTHON_VERSION}')
