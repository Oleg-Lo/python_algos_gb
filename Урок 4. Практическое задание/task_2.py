"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint

from functools import lru_cache


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@lru_cache(maxsize=1000)
def recursive_reverse2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))
# -------------------------------------------------------------------------


print('Не оптимизированная функция recursive_reverse с декоратором lru_cache')
print(
    timeit(
        "recursive_reverse2(num_100)",
        setup='from __main__ import recursive_reverse2, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse2(num_1000)",
        setup='from __main__ import recursive_reverse2, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse2(num_10000)",
        setup='from __main__ import recursive_reverse2, num_10000',
        number=10000))

# в функции recursive_reverse с каждым последующим вычислением мы
# вычисляем эту функцию для нашего числа только без одной конечной цифры, поэтому
# время выполнения возрастает с увеличением входного числа num.
# Можно не вычислять всякий раз а сохранять результат предыдущего вычисления в кеше
# и тогда функция будет отрабатывать значительно быстрее и результат уже не будет
# зависеть от величины входного параметра num
# А если применить декоратор lru_cache то будет еще быстрее

# Не оптимизированная функция recursive_reverse
# 0.0314148
# 0.0367406
# 0.0689924
# Оптимизированная функция recursive_reverse_mem
# 0.0020610000000000073
# 0.0020610000000000073
# 0.0021446999999999994
# Не оптимизированная функция recursive_reverse с декоратором lru_cache
# 0.000847500000000001
# 0.0008422999999999903
# 0.0008650000000000047
