import time
from functools import cache

from decorator import decorator_timer


@cache
@decorator_timer
def slow_func():
    time.sleep(5)
    return 10


def main():
    print(slow_func())
    print(slow_func())


if __name__ == '__main__':
    main()
