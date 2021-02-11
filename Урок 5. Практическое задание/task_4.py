"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import random
from collections import OrderedDict
from timeit import timeit

dic1 = {}
for i in range(10000000):
    dic1[i] = i

od1 = OrderedDict(dic1)

# print(random.choice(list1))
# print(random.choice(deque1))

print("Dictionary")
print("add " + str(timeit("dic1[10]=10", "from __main__ import dic1", number=1000000)))
print("pop " + str(timeit("dic1.pop(9)", "from __main__ import dic1", number=1)))
print("random choice " + str(timeit("random.choice(dic1)", "from __main__ import dic1,random", number=10000)))

# -------------------------------------
print("OrderedDict")
print("add " + str(timeit("od1[10]=10", "from __main__ import od1", number=1000000)))
print("pop " + str(timeit("od1.pop(9)", "from __main__ import od1", number=1)))
print("random choice " + str(timeit("random.choice(od1)", "from __main__ import od1,random", number=10000)))

# случайный выбор работает примерно одинаково в обоих словарях
# удаление и добавление быстрее в обычном словаре чем в OrderedDict,
# что логично т.к. обычный словарь как раз и создавался для быстрого добавления, извлечения и обновления данных
# OrderedDict создавался для частыx операций переупорядочивания при этом эффективность использования памяти,
# скорость итераций и производительность операций обновления были не так важны.
