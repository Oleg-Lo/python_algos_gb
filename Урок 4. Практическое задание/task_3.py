"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from cProfile import run
from sys import setrecursionlimit
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    str00 = ""
    for i in range(1000):
        str00 += str(i)
    str10 = int(str00)
    revers(str10)
    revers_2(str10)
    revers_3(str10)


setrecursionlimit(10000)

run('main()')

str0 = ""
for i in range(1000):
    str0 += str(i)
str1 = int(str0)

print("reverse    " + str(timeit("revers(str1)", "from __main__ import revers, str1", number=1)))
print("reverse_2  " + str(timeit("revers_2(str1)", "from __main__ import revers_2, str1", number=1)))
print("reverse_3  " + str(timeit("revers_3(str1)", "from __main__ import revers_3, str1", number=1)))

'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.046    0.046 <string>:1(<module>)
   2890/1    0.026    0.000    0.026    0.026 task_3.py:18(revers)
        1    0.019    0.019    0.019    0.019 task_3.py:28(revers_2)
        1    0.001    0.001    0.001    0.001 task_3.py:36(revers_3)
        1    0.001    0.001    0.046    0.046 task_3.py:42(main)
        1    0.000    0.000    0.046    0.046 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


reverse    0.022000099999999995
reverse_2  0.019390699999999997
reverse_3  0.0005914000000000197
'''
# самая медленна это первая реализация через рекурсию, а самая быстрая последняя которая
# переводит число в строку и использует строку как масссив символов, выводя определенный срез массива
