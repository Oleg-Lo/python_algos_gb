"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr += [i]
    return new_arr


if __name__ == "__main__":
    num1 = [0, 1, 2, 2, 4, 2, 6, 7, 8, 9]
    print(timeit("func_1(num1)", "from __main__ import func_1, num1", number=10000000))
    print(timeit("func_2(num1)", "from __main__ import func_2, num1", number=10000000))
    print(timeit("func_3(num1)", "from __main__ import func_3, num1", number=10000000))

    # 16.508307700000003
    # 15.957045
    # 16.917081800000005

# вторая функция более быстрая чем первая а третья менее быстрая
# в первой итератор с функцией append
# во второй списковое включение
# в третей самый медленный итератор с конкатенацией