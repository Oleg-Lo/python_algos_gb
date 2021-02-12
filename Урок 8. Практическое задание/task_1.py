"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

import heapq
from collections import defaultdict


def encodeHuffman(freq):
    heap = [[frequency, [char, '']] for char, frequency in freq.items()]
    heapq.heapify(heap)  # преобразуем наш список в кучу
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)

        for value in low[1:]:
            value[1] = '0' + value[1]

        for value in high[1:]:
            value[1] = '1' + value[1]

        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    result = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    return result


if __name__ == "__main__":
    string = input("Введите строку:")
    freq = defaultdict(int)  # словарь где символ строки это ключ а частота его появления в строке это значение

    for character in string:
        freq[character] += 1
    print(freq)

    huff = encodeHuffman(freq)
    print(huff)

    for i in huff:
        print(i[0] + " - " + i[1])

"""
Введите строку:мама мыла раму
defaultdict(<class 'int'>, {'м': 4, 'а': 4, ' ': 2, 'ы': 1, 'л': 1, 'р': 1, 'у': 1})
[['а', '10'], ['м', '11'], [' ', '010'], ['у', '000'], ['ы', '001'], ['л', '0110'], ['р', '0111']]
а - 10
м - 11
  - 010
у - 000
ы - 001
л - 0110
р - 0111
"""