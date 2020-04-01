#  Во втором массиве сохранить индексы четных элементов первого массива.
#  Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#  второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
#  т. к. именно в этих позициях первого массива стоят четные числа.

from random import randint

first_array = [randint(-10, 10) for _ in range(20)]
second_array = []

for i, item in enumerate(first_array):
    if not item % 2:
        second_array.append(i)

print(first_array)
print(second_array)
