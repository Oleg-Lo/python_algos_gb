"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import timeit
from itertools import groupby

import memory_profiler
from memory_profiler import profile


def mydecor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = timeit.default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        t2 = timeit.default_timer()
        mem_diff = m2[0] - m1[0]
        time_diff = t2 - t1
        return res, mem_diff, time_diff

    return wrapper


@mydecor
def func1(number):
    dic1 = {}
    for i in range(number):
        dic1[i] = i * i
    return dic1


@mydecor
def func2(number):
    list1 = []
    for i in range(number):
        list1.append(i * i)
    return list1


@mydecor
def func3(number):
    for i in range(number):
        yield i * i


@mydecor
def factorial(n):
    result = 1
    for i in range(0, n, 1):
        result *= i
    return result


@mydecor
def factorial1(n):
    if n == 1:
        return 1
    return n * factorial1(n - 1)


# подсчет количества подстрок в строке
@profile
def convert_str(str1):
    set1 = set()
    for i in range(len(str1)):
        for j in range(len(str1) - 1 if i == 0 else len(str1), i, -1):
            set1.add(hash(str1[i:j]))
    return len(set1)


@profile
def convert_str1(str1):
    set1 = []
    for i in range(len(str1)):
        for j in range(len(str1) - 1 if i == 0 else len(str1), i, -1):
            set1.append(hash(str1[i:j]))

    # удалим дубли из списка
    # new_set1 = [x for x, _ in groupby(set1)]
    new_set1 = []
    for i in set1:
        if i not in new_set1:
            new_set1.append(i)

    return len(new_set1)


if __name__ == "__main__":
    res, mem_diff, time_diff = factorial(100)
    # print(res)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(f"а по времени {time_diff}")

    print(convert_str("Старайтесь использовать генераторы для вычислений. Суть таких вычислений "
                      "заключается в итерации: или через явное использование «for», или неявное. "
                      "For передает это вычисление любой функции или конструкции, осуществляющей "
                      "итерацию. Генераторы не возвращают любое количество элементов сразу вместе, "
                      "как списки, они возвращают элементы один за другим."))
    print(convert_str1("Старайтесь использовать генераторы для вычислений. Суть таких вычислений "
                       "заключается в итерации: или через явное использование «for», или неявное. "
                       "For передает это вычисление любой функции или конструкции, осуществляющей "
                       "итерацию. Генераторы не возвращают любое количество элементов сразу вместе, "
                       "как списки, они возвращают элементы один за другим."))

# для func1(10000)
# Выполнение заняло 0.5390625 Mib
# а по времени 0.1012071

# для func2(10000)
# Выполнение заняло 0.140625 Mib
# а по времени 0.10302940000000005
# стало лучше по памяти потому что списки занимают места меньше чем словари

# для func3(10000)
# Выполнение заняло 0.00390625 Mib
# а по времени 0.10070980000000002
# видим существенное улучшение по памяти потому что используем ленивые вычисления
# не храним все результаты а берем только то что нужно
# ------------------------------------------------------------------


# factorial(100) c циклом
# Выполнение заняло 0.00390625 Mib
# а по времени 0.10042859999999998

# factorial1(100) c рекурсией
# Выполнение заняло 0.10546875 Mib
# а по времени 20.1679625
# рекурсивная функция занимает больше места в памяти из-за постоянного добавления новых слоев в стек
# и по времени она проигрывает так как постоянно пересчитывает саму себя
# ------------------------------------------------------------------------


# теперь возьмем 2 реализации функции подсчета количества подстрок в строке
# в первом варианте использовался set который работал быстро но отъел памяти 2.1 MiB
# во втором варианте использовалось два списка и они оба весили меньше чем один set! 1.6 Mib против 2.1 Mib
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    84     15.8 MiB     15.8 MiB           1   @profile
    85                                         def convert_str(str1):
    86     15.8 MiB      0.0 MiB           1       set1 = set()
    87     17.9 MiB      0.0 MiB         349       for i in range(len(str1)):
    88     17.9 MiB      0.0 MiB       61073           for j in range(len(str1) - 1 if i == 0 else len(str1), i, -1):
    89     17.9 MiB      2.1 MiB       60725               set1.add(hash(str1[i:j]))
    90     17.9 MiB      0.0 MiB           1       return len(set1)


59939
Filename: C:/Users/OLEGLO/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    93     15.9 MiB     15.9 MiB           1   @profile
    94                                         def convert_str1(str1):
    95     15.9 MiB      0.0 MiB           1       set1 = []
    96     17.1 MiB      0.0 MiB         349       for i in range(len(str1)):
    97     17.1 MiB      0.0 MiB       61073           for j in range(len(str1) - 1 if i == 0 else len(str1), i, -1):
    98     17.1 MiB      1.2 MiB       60725               set1.append(hash(str1[i:j]))
    99                                         
   100                                             # удалим дубли из списка
   101                                             #new_set1 = [x for x, _ in groupby(set1)]
   102     17.1 MiB      0.0 MiB           1       new_set1 = []
   103     17.5 MiB      0.0 MiB       60726       for i in set1:
   104     17.5 MiB      0.1 MiB       60725           if i not in new_set1:
   105     17.5 MiB      0.3 MiB       59939               new_set1.append(i)
   106                                         
   107     17.5 MiB      0.0 MiB           1       return len(new_set1)


59939
"""
