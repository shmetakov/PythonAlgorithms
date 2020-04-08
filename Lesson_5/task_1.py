# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыльрациональных
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль
# выше среднего и ниже среднего.

from collections import defaultdict

# Получаем данные от пользователя
spam = defaultdict(list)

N = int(input('Введите количество предприятий (целое > 0): '))

for i in range(N):
    name = input('Введите наименование предприятия: ')
    profit = 0.0

    for j in range(1, 5):
        profit = float(input(f'Введите прибыль за {j} квартал: '))
        spam[name].append(profit)

print(spam)

# Считаем среднюю прибыль
average = 0.0
result_dict = defaultdict(float)

for k, v in spam.items():
    result_dict[k] = sum(v) / len(v)
    average += result_dict[k]

average = average / N
print(result_dict)
print(average)

# Формируем списки и выводим печать
list_min = []
list_max = []

for k, v in result_dict.items():
    if v < average:
        list_min.append(k)
    else:
        list_max.append(k)

print("Прибыль ниже среднего: ")
for name in list_min:
    print(name)

print("Прибыль выше среднего: ")
for name in list_max:
    print(name)


