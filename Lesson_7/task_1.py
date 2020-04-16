# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#    Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


def smart_bubble_sort(mas, reverse=False):
    """
    Сортировка пузырьком (улучшенный)
    Если перестановок не было за проход по массиву (is_swap = False),
    то массив отсортирован. Нет смысла выполнять сортировку дальше.
    """

    n = 1
    while n < len(mas):
        is_swap = False
        if not reverse:
            for i in range(len(mas) - n):
                if mas[i] > mas[i + 1]:
                    mas[i], mas[i + 1] = mas[i + 1], mas[i]
                    is_swap = True
        else:
            for i in range(len(mas) - 1, n - 1, -1):
                if mas[i] > mas[i - 1]:
                    mas[i], mas[i - 1] = mas[i - 1], mas[i]
                    is_swap = True

        if not is_swap:
            break

        n += 1


size = 20
array = [random.randrange(-100, 99) for _ in range(size)]

print(f'Исходный массив: {array}')
smart_bubble_sort(array, reverse=True)
print(f'Отсортированный массив: {array}')
