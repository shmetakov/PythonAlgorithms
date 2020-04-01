# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

array = [randint(-10, 10) for _ in range(20)]

max_i = 0
max_item = 0

for i, item in enumerate(array):
    if item < 0 and abs(item) > abs(max_item):
        max_item = item
        max_i = i

print(array)
print(f"Максимальный отрицательный элемен {max_item} на позиции {max_i}")
