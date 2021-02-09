"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple2(i):
    set1 = set(range(2, 10000 + 1))
    j = 0
    while j < i:
        simple_number = min(set1)
        set1 -= set(range(simple_number, 10000 + 1, simple_number))
        j += 1
    return simple_number


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(simple2(i))

num_10 = 10
num_100 = 100
num_1000 = 1000
# ---------------------------------------------------------------
print('функция simple')
print(timeit('simple(num_10)', 'from __main__ import simple, num_10', number=10))
print(timeit('simple(num_100)', 'from __main__ import simple, num_100', number=10))
print(timeit('simple(num_1000)', 'from __main__ import simple, num_1000', number=10))

# ---------------------------------------------------------------
print('функция simple2')
print(timeit('simple2(num_10)', 'from __main__ import simple2, num_10', number=10))
print(timeit('simple2(num_100)', 'from __main__ import simple2, num_100', number=10))
print(timeit('simple2(num_1000)', 'from __main__ import simple2, num_1000', number=10))

'''
функция simple
0.00042909999999984905
0.03596829999999995
4.834563299999999
функция simple2
0.030009500000000244
0.08052980000000076
0.4217195
'''

# на малых объемах эффективнее первый алгоритм, а на больших второй

