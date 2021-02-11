"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import defaultdict
from collections import deque


class MyHex(object):

    def __init__(self, hex_num):
        self.hex_num = hex_num

    def __add__(self, other):
        return str(hex(int(self.hex_num, 16) + int(other.hex_num, 16)))[2::].upper()

    def __mul__(self, other):
        return str(hex(int(self.hex_num, 16) * int(other.hex_num, 16)))[2::].upper()


# -----------------------------------------------------------------------


def sum_hex(a, b):
    # числа будем записывать в defaultdict потому что можно отсутствующие разряды заменить нулем
    numa = defaultdict(lambda: "0")
    numb = defaultdict(lambda: "0")
    result = deque()
    if len(a) >= len(b):
        length = len(a)
    else:
        length = len(b)

    # записываем числа в defaultdict одновременно переворачивая, ключом будет номер разряда
    for i in range(len(a) - 1, -1, -1):
        numa[len(a) - 1 - i] = a[i]

    for i in range(len(b) - 1, -1, -1):
        numb[len(b) - 1 - i] = b[i]

    # defaultdict(<function <lambda> at 0x017762B0>, {0: '2', 1: 'A'})
    # defaultdict(<function <lambda> at 0x017D2FA0>, {0: 'F', 1: '4', 2: 'C'})

    rest = 0  # для переноса в следующий разряд
    for i in range(length):
        # print(i)
        res_num = int(numa[i], 16) + int(numb[i], 16)
        # print(res_num)

        # print(f'{i} - {(res_num + rest) % 16}')
        result.append(str(hex((res_num + rest) % 16))[2::].upper())

        if res_num > 15:
            rest = 1
        else:
            rest = 0
        # print(rest)

    if rest > 0:
        result.append("1")

    final_result = ""
    while result:
        final_result += result.pop()

    return final_result


def mult_hex(a, b):
    numa = defaultdict(lambda: "0")
    numb = defaultdict(lambda: "0")
    result = deque()
    results = []
    if len(a) >= len(b):
        length = len(a)
    else:
        length = len(b)

    for i in range(len(a) - 1, -1, -1):
        numa[len(a) - 1 - i] = a[i]

    for i in range(len(b) - 1, -1, -1):
        numb[len(b) - 1 - i] = b[i]

    for j in range(length):
        rest = 0  # для переноса в следующий разряд
        result.clear()
        for i in range(length):
            res_num = int(numa[j], 16) * int(numb[i], 16)
            result.append(str(hex((res_num + rest) % 16))[2::].upper())
            if res_num > 15:
                rest = (res_num + rest) // 16
            else:
                rest = 0

        if rest > 0:
            result.append(str(hex(rest))[2::].upper())

        for _ in range(j):
            result.appendleft(0)  # каждый последующий результат сдвигаем на один разряд
        # print(result)

        final_result = ""
        while result:
            final_result += str(result.pop())

        results.append(final_result)
        # print(results)

    summ1 = ""
    for i in results:
        summ1 = sum_hex(i, summ1)
    return summ1


aaa = input('Введите шестнадцатиричное число a: ').upper()
bbb = input('Введите шестнадцатиричное число b: ').upper()

# a="A2F"
# b="C4F"
print("collections сумма " + sum_hex(aaa, bbb))
print("collections произведение " + mult_hex(aaa, bbb))

print("ООП сумма " + str(MyHex(aaa) + MyHex(bbb)))
print("ООП произведение " + str(MyHex(aaa) * MyHex(bbb)))

# print(123 % 16)
"""
Введите шестнадцатиричное число a: 36cd
Введите шестнадцатиричное число b: 7d4b
collections сумма B418
collections произведение 1AD2270F
ООП сумма B418
ООП произведение 1AD2270F
"""