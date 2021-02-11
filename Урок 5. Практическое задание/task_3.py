"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
import random
from collections import deque
from timeit import timeit

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deque1 = deque()
deque1.extend(list1)
# print(random.choice(list1))
# print(random.choice(deque1))

print("list")
print("append " + str(timeit("list1.append(4)", "from __main__ import list1", number=10000000)))
print("append " + str(timeit("list1.append(5)", "from __main__ import list1", number=10000000)))
print("pop " + str(timeit("list1.pop()", "from __main__ import list1", number=10000000)))
print("pop " + str(timeit("list1.pop()", "from __main__ import list1", number=10000000)))
print("random choice " + str(timeit("random.choice(list1)", "from __main__ import list1,random", number=10000000)))

# -------------------------------------
print("deque")
print("append " + str(timeit("deque1.append(4)", "from __main__ import deque1", number=10000000)))
print("appendleft " + str(timeit("deque1.appendleft(5)", "from __main__ import deque1", number=10000000)))
print("pop " + str(timeit("deque1.pop()", "from __main__ import deque1", number=10000000)))
print("popleft " + str(timeit("deque1.popleft()", "from __main__ import deque1", number=10000000)))
print("random choice " + str(timeit("random.choice(deque1)", "from __main__ import deque1,random", number=10000000)))

"""
list
append 0.8252886
append 0.817207
pop 0.5967297
pop 0.5590105999999997
random choice 5.6451802
deque
append 0.6096826999999987
appendleft 0.6272000000000002
pop 0.5665293000000009
popleft 0.5776900000000005
random choice 5.747086900000001
"""

# запись и извлечение быстрее в deque
