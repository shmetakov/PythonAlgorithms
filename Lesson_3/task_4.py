# 4. Определить, какое число в массиве встречается чаще всего.

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

