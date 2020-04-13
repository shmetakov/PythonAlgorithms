# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.

# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки)
# вставить в виде комментариев в файл с кодом. Не забудьте указать версию
# и разрядность вашей ОС и интерпретатора Python;

# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof
# после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.

import sys


def show_size(x, level=0):
    result_size = sys.getsizeof(x)
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for k, v in x.items():
                result_size += show_size(k, level + 1)
                result_size += show_size(v, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                result_size += show_size(xx, level + 1)

    return result_size


def task_1():
    """
    Задача 1 первого урока

    Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
    """

    bit_and = 5 & 6
    bit_or = 5 | 6
    bit_xor = 5 ^ 6
    left_shift = 5 << 2
    right_shift = 5 >> 2

    print(f"Результат побитового AND : {bit_and}")
    print(f"Результат побитового OR  : {bit_or}")
    print(f"Результат побитового XOR : {bit_xor}")
    print()
    print(f"Результат побитового сдвига влево  : {left_shift}")
    print(f"Результат побитового сдвига вправо : {right_shift}")

    return locals()


def task_2():
    """
    Задача 4 третьего урока

    Определить, какое число в массиве встречается чаще всего.
    """

    from random import randint

    size_array = 20

    array = [randint(1, 5) for _ in range(size_array)]

    print(array)

    max_count = 1
    num = array[0]

    for i in range(size_array - 1):
        count = 1
        for j in range(i + 1, size_array):
            if array[i] == array[j]:
                count += 1
        if count > max_count:
            max_count = count
            num = array[i]

    if max_count > 1:
        print(max_count, 'раз(а) встречается число', num)
    else:
        print('Все элементы уникальны')

    return locals()


def task_3():
    """
    Задача 3 третьего урока (первый вариант)

    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    """

    from random import randint

    array = [randint(-10, 10) for _ in range(20)]

    max_i = 0
    min_i = 0
    max_item = array[0]
    min_item = array[0]

    print(array)

    for i, item in enumerate(array):
        if max_item < item:
            max_item = item
            max_i = i

        if min_item > item:
            min_item = item
            min_i = i

    array[max_i] = min_item
    array[min_i] = max_item

    print(array)

    return locals()


# Оптимизируем задачу task_3()


def task_3_2():
    """
    Задача 3 третьего урока (второй вариант)

    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    """

    from random import randint

    array = [randint(-10, 10) for _ in range(20)]

    print(array)

    max_item = max(array)
    min_item = min(array)

    max_i = array.index(max_item)
    min_i = array.index(min_item)

    array[max_i], array[min_i] = min_item, max_item

    print(array)

    return locals()


def task_3_3():
    """
    Задача 3 третьего урока (второй вариант)

    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    """

    from random import randint

    array = [randint(-10, 10) for _ in range(20)]

    print(array)

    if array.index(max(array)) > array.index(min(array)):
        array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    else:
        array[array.index(min(array))], array[array.index(max(array))] = max(array), min(array)

    print(array)

    return locals()


print(f'sys.platform = {sys.platform}, sys.version = {sys.version}')

# sys.platform = linux, sys.version = 3.9.0a1 (default, Dec 23 2019, 20:58:58)
# Kernel: 4.15.0-72-generic x86_64 bits

result_task_1 = task_1()
result_task_2 = task_2()
result_task_3 = task_3()
result_task_3_2 = task_3_2()
result_task_3_3 = task_3_3()

print(f'Функция {task_1.__name__}:')

size_of_all_var_1 = 0

for var in result_task_1.keys():
    size_of_all_var_1 += show_size(result_task_1[var], 1)

print('\t', f'Список всех переменных: {result_task_1}')
print('\t', f'Общий размер всех переменных: {size_of_all_var_1} байт')

# Функция task_1:
# 	 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'int'>, size= 28, object= 7
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 20
# 	 type= <class 'int'>, size= 28, object= 1
# 	 Список всех переменных: {'bit_and': 4, 'bit_or': 7, 'bit_xor': 3, 'left_shift': 20, 'right_shift': 1}
# 	 Общий размер всех переменных: 140 байт

print(f'Функция {task_2.__name__}:')

size_of_all_var_2 = 0

for var in result_task_2.keys():
    size_of_all_var_2 += show_size(result_task_2[var], 1)

print('\t', f'Список всех переменных: {result_task_2}')
print('\t', f'Общий размер всех переменных: {size_of_all_var_2} байт')

# Функция task_2:
# 	 type= <class 'int'>, size= 28, object= 20
# 	 type= <class 'list'>, size= 256, object= [1, 5, 2, 3, 1, 3, 3, 1, 2, 3, 1, 5, 2, 4, 2, 4, 1, 1, 3, 3]
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 5
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 5
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 4
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 4
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 6
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 18
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 19
# 	 type= <class 'method'>, size= 64, object= <bound method Random.randint of <random.Random object at 0x556edc6068c0>>
# 	 Список всех переменных: {'size_array': 20, 'array': [1, 5, 2, 3, 1, 3, 3, 1, 2, 3, 1, 5, 2, 4, 2, 4, 1, 1, 3, 3], 'max_count': 6, 'num': 1, 'i': 18, 'count': 2, 'j': 19, 'randint': <bound method Random.randint of <random.Random object at 0x556edc6068c0>>}
# 	 Общий размер всех переменных: 1048 байт
#
# Process finished with exit code 0

print(f'Функция {task_3.__name__}:')

size_of_all_var_3 = 0

for var in result_task_3.keys():
    size_of_all_var_3 += show_size(result_task_3[var], 1)

print('\t', f'Список всех переменных: {result_task_3}')
print('\t', f'Общий размер всех переменных: {size_of_all_var_3} байт')

# Функция task_3:
# 	 type= <class 'list'>, size= 256, object= [2, 3, 6, -10, -2, 9, 7, 9, 1, 0, -7, -1, 10, -3, -2, 3, 7, -6, 7, 4]
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 6
# 		 type= <class 'int'>, size= 28, object= -10
# 		 type= <class 'int'>, size= 28, object= -2
# 		 type= <class 'int'>, size= 28, object= 9
# 		 type= <class 'int'>, size= 28, object= 7
# 		 type= <class 'int'>, size= 28, object= 9
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 24, object= 0
# 		 type= <class 'int'>, size= 28, object= -7
# 		 type= <class 'int'>, size= 28, object= -1
# 		 type= <class 'int'>, size= 28, object= 10
# 		 type= <class 'int'>, size= 28, object= -3
# 		 type= <class 'int'>, size= 28, object= -2
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 7
# 		 type= <class 'int'>, size= 28, object= -6
# 		 type= <class 'int'>, size= 28, object= 7
# 		 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 12
# 	 type= <class 'int'>, size= 28, object= 10
# 	 type= <class 'int'>, size= 28, object= -10
# 	 type= <class 'int'>, size= 28, object= 19
# 	 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'method'>, size= 64, object= <bound method Random.randint of <random.Random object at 0x562767624680>>
# 	 Список всех переменных: {'array': [2, 3, 6, -10, -2, 9, 7, 9, 1, 0, -7, -1, 10, -3, -2, 3, 7, -6, 7, 4], 'max_i': 3, 'min_i': 12, 'max_item': 10, 'min_item': -10, 'i': 19, 'item': 4, 'randint': <bound method Random.randint of <random.Random object at 0x562767624680>>}
# 	 Общий размер всех переменных: 1044 байт


print(f'Функция {task_3_2.__name__}:')

size_of_all_var_3_2 = 0

for var in result_task_3_2.keys():
    size_of_all_var_3_2 += show_size(result_task_3_2[var], 1)

print('\t', f'Список всех переменных: {result_task_3_2}')
print('\t', f'Общий размер всех переменных: {size_of_all_var_3_2} байт')

# Функция task_3_2:
# 	 type= <class 'list'>, size= 256, object= [6, 10, -5, -6, 4, -7, 3, -8, -3, -8, -1, -7, -9, -10, -3, 6, 5, 5, 6, -5]
# 		 type= <class 'int'>, size= 28, object= 6
# 		 type= <class 'int'>, size= 28, object= 10
# 		 type= <class 'int'>, size= 28, object= -5
# 		 type= <class 'int'>, size= 28, object= -6
# 		 type= <class 'int'>, size= 28, object= 4
# 		 type= <class 'int'>, size= 28, object= -7
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= -8
# 		 type= <class 'int'>, size= 28, object= -3
# 		 type= <class 'int'>, size= 28, object= -8
# 		 type= <class 'int'>, size= 28, object= -1
# 		 type= <class 'int'>, size= 28, object= -7
# 		 type= <class 'int'>, size= 28, object= -9
# 		 type= <class 'int'>, size= 28, object= -10
# 		 type= <class 'int'>, size= 28, object= -3
# 		 type= <class 'int'>, size= 28, object= 6
# 		 type= <class 'int'>, size= 28, object= 5
# 		 type= <class 'int'>, size= 28, object= 5
# 		 type= <class 'int'>, size= 28, object= 6
# 		 type= <class 'int'>, size= 28, object= -5
# 	 type= <class 'int'>, size= 28, object= 10
# 	 type= <class 'int'>, size= 28, object= -10
# 	 type= <class 'int'>, size= 28, object= 13
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'method'>, size= 64, object= <bound method Random.randint of <random.Random object at 0x56483be95430>>
# 	 Список всех переменных: {'array': [6, 10, -5, -6, 4, -7, 3, -8, -3, -8, -1, -7, -9, -10, -3, 6, 5, 5, 6, -5], 'max_item': 10, 'min_item': -10, 'max_i': 13, 'min_i': 1, 'randint': <bound method Random.randint of <random.Random object at 0x56483be95430>>}
# 	 Общий размер всех переменных: 992 байт
#
# Process finished with exit code 0

print(f'Функция {task_3_3.__name__}:')

size_of_all_var_3_3 = 0

for var in result_task_3_3.keys():
    size_of_all_var_3_3 += show_size(result_task_3_3[var], 1)

print('\t', f'Список всех переменных: {result_task_3_3}')
print('\t', f'Общий размер всех переменных: {size_of_all_var_3_3} байт')

# Функция task_3_3:
# 	 type= <class 'list'>, size= 256, object= [-5, 3, 1, 0, -2, 2, -3, 9, -1, 6, 0, -2, -9, 3, 2, 5, -9, 9, -7, -8]
# 		 type= <class 'int'>, size= 28, object= -5
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 24, object= 0
# 		 type= <class 'int'>, size= 28, object= -2
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= -3
# 		 type= <class 'int'>, size= 28, object= 9
# 		 type= <class 'int'>, size= 28, object= -1
# 		 type= <class 'int'>, size= 28, object= 6
# 		 type= <class 'int'>, size= 24, object= 0
# 		 type= <class 'int'>, size= 28, object= -2
# 		 type= <class 'int'>, size= 28, object= -9
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 5
# 		 type= <class 'int'>, size= 28, object= -9
# 		 type= <class 'int'>, size= 28, object= 9
# 		 type= <class 'int'>, size= 28, object= -7
# 		 type= <class 'int'>, size= 28, object= -8
# 	 type= <class 'method'>, size= 64, object= <bound method Random.randint of <random.Random object at 0x55c7748ac620>>
# 	 Список всех переменных: {'array': [-5, 3, 1, 0, -2, 2, -3, 9, -1, 6, 0, -2, -9, 3, 2, 5, -9, 9, -7, -8], 'randint': <bound method Random.randint of <random.Random object at 0x55c7748ac620>>}
# 	 Общий размер всех переменных: 872 байт
#
# Process finished with exit code 0

# Вывод:
# По итогам анализа можно сказать, что лучшим вариантом оказался task_3_3().
# В данном варианте все нужные значения вычисляются “на лету” без использования
# дополнительных переменных. Код получился более сложный, чем в предыдущих вариантах,
# но при этом память используется только на хранение массива и на объект Random
