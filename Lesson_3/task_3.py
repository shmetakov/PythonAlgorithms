# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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
