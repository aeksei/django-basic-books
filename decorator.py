import time


N = 1000


def decorator_timer(fn):
    # nonlocal область видимости, но(!) для функции wrapper
    def wrapper(*args, **kwargs):
        t0 = time.time()  # сделать что-то до вызова функции

        result = fn(*args, **kwargs)

        dt = time.time() - t0  # сделать что-то после вызова функции
        print(f"Время выполнения функции {fn}: {dt}")

        return result

    return wrapper  # возвращаю обёртку


@decorator_timer  # get_list_comprehension = decorator_timer(get_list_comprehension)
def get_list_comprehension(n: int):
    return [i for i in range(n)]


@decorator_timer
def get_for_loop(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


# def timer(fn):
#     """
#
#     :param fn: Ссылка на функцию
#     :return:
#     """
#     t0 = time.time()
#
#     fn()
#
#     dt = time.time() - t0
#     print(f"Время выполнения функции {fn}: {dt}")








if __name__ == '__main__':
    print(get_for_loop(10))
    print(get_list_comprehension(10))
