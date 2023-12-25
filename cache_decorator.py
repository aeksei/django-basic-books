import time
from collections import OrderedDict


def my_cache(max_len=10):
    def decorator(fn):
        print("Выполняется один раз в момент декорирования")
        dict_cache = OrderedDict()

        def wrapper(*args):
            if args not in dict_cache:
                result = fn(*args)
                if len(dict_cache) == max_len:
                    dict_cache.popitem(last=False)
                dict_cache[args] = result

            return dict_cache[args]
        return wrapper
    return decorator


@my_cache(10)  # decorator -> decorator(slow_func)
def slow_func():
    time.sleep(5)
    return 10


@my_cache
def some_func():
    return 100


if __name__ == '__main__':
    slow_func()
    slow_func()

    some_func()