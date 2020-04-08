# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
list_of_numbers = [(0, '0'), (1, '1'), (2, '2'), (3, '3'),
                   (4, '4'), (5, '5'), (6, '6'), (7, '7'),
                   (8, '8'), (9, '9'), (10, 'A'), (11, 'B'),
                   (12, 'C'), (13, 'D'), (14, 'E'), (15, 'F')]


dict_of_numbers = defaultdict(str)
dict_of_values = defaultdict(int)

for k, v in list_of_numbers:
    dict_of_numbers[k] = v
    dict_of_values[v] = k


def summa(*args):
    """Функция сложения любого количества аргументов"""
    args = sorted(args, key=len, reverse=True)

    result = []
    k_sum = 0

    # Складываем в цикле
    for i in range(len(args[0])):
        spam = []
        # Если вышли за предел списка, то присваиваем 0
        try:
            for j in args:
                spam.append(dict_of_values[j[-i - 1]])
        except IndexError:
            spam.append(0)

        # Добавляем в список младший разряд
        result.append(dict_of_numbers[(sum(spam) + k_sum) % 16])
        # Старший запоминаем для следующей итерации
        k_sum = (sum(spam) + k_sum) // 16

    # Если остался, добавляем
    if k_sum:
        result.append(str(k_sum))

    # Инвертируем результат
    result = result[::-1]

    return result


def mul(x, y):
    """Функция умножения 2 чисел"""
    result = []

    # Цикл умножения
    for i in range(len(x)):
        spam = []
        k_mul = 0

        # Каждый разряд первого числа умножаем целиком на второе число
        for j in range(len(y)):
            a = dict_of_values[x[-i - 1]] * dict_of_values[y[-j - 1]]
            spam.append(list('0' * j + dict_of_numbers[(a + k_mul) % 16] + dict_of_numbers[(a + k_mul) // 16])[::-1])

        # Складываем полученые резяльтаты
        spam = summa(*spam)

        # Добавляем нужное количество нулей в зависимости от итерации
        for k in range(i):
            spam.append('0')

        # Заносим в резяльтирующий список
        result.append(spam)

    # Складываем полученые числа и возращаем результат
    return summa(*result)


first = list(input('Первое число: ').upper())
second = list(input('Второе число: ').upper())

print(first)
print(second)

print(f'Сумма: {summa(first, second)}')
print(f'Произведение: {mul(first, second)}')







