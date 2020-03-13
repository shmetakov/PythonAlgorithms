# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Число a: "))
b = int(input("Число b: "))
c = int(input("Число c: "))

if b < a < c or c < a < b:
    print(f"Среднее {a}")
elif a < b < c or c < b < a:
    print(f"Среднее {b}")
else:
    print(f"Среднее {c}")
