"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import random

# сортирует левую часть и правую и объединяет
def merge(right: list, left: list, result: list):
    result.append((left if left[0] < right[0] else right).pop(0))
    return merge(right, left, result) if left and right else result + left + right

# разбивает массив пополам пока в нем не останется 1 элемент
def merge_sort(collection: list):
    if len(collection) == 1:
        return collection
    return merge(merge_sort(collection[len(collection) // 2:]),
                 merge_sort(collection[:len(collection) // 2]), [])


orig_list = [random.randint(0, 50) for _ in range(10)]

print(orig_list)
print(merge_sort(orig_list))

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(0, 50) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(0, 50) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
[7, 3, 48, 32, 42, 9, 3, 9, 12, 47]
[3, 3, 7, 9, 9, 12, 32, 42, 47, 48]
0.0157348
0.27090329999999996
4.102166400000001
"""