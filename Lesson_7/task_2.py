# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge(left, right):
    """Слияние массивов"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(mas):
    """Сортировка слиянием"""
    if len(mas) < 2:
        return mas[:]

    middle = int(len(mas) / 2)
    left = merge_sort(mas[:middle])
    right = merge_sort(mas[middle:])

    return merge(left, right)


size = 20
array = [random.uniform(0, 50) for _ in range(size)]

print(f'Исходный массив: {array}')
array = merge_sort(array)
print(f'Отсортированный массив: {array}')
