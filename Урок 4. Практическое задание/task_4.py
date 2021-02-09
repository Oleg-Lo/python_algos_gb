"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from statistics import mode
from timeit import timeit
from collections import Counter

array = [5, 3, 5, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    return max(set(array), key=array.count)


def func_4():
    return mode(array)


def func_5():
    count1 = Counter(array)
    return count1.most_common(1)[0][0]


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print("func_1  " + str(timeit("func_1()", "from __main__ import func_1", number=100000)))
print("func_2  " + str(timeit("func_2()", "from __main__ import func_2", number=100000)))
print("func_3  " + str(timeit("func_3()", "from __main__ import func_3", number=100000)))
print("func_4  " + str(timeit("func_4()", "from __main__ import func_4", number=100000)))
print("func_5  " + str(timeit("func_5()", "from __main__ import func_5", number=100000)))

'''
func_1  0.1715152
func_2  0.25252260000000004
func_3  0.13063590000000003
func_4  0.36976470000000006
func_5  0.3548838999999999
'''
# самая быстрая функция func_3 которая использует set для удаления дублей
# и потом ищет наибольшее количество вхождений
