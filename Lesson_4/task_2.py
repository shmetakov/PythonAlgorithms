# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import cProfile


def test_prime(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i, item in enumerate(lst, 1):
        assert item == func(i)
        print(f'Test {i} OK')


def prime(n):
    inc = 1
    item = 2

    while True:
        for i in range(2, item + 1):
            if not item % i and i != item:
                break
            elif i == item:
                inc += 1
                if inc == n + 1:
                    return i

        item += 1


def sieve(n):
    item = n * 7 + 1
    sv = [i for i in range(item)]
    sv[1] = 0

    for i in range(2, item):
        if sv[i] != 0:
            j = i * 2

        while j < item:
            sv[j] = 0
            j += i

    sv = [i for i in sv if i]
    return sv[n - 1]


# $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.prime(10)"
# 1000 loops, best of 5: 11.3 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.prime(20)"
# 1000 loops, best of 5: 40.5 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.prime(100)"
# 1000 loops, best of 5: 1.13 msec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.prime(200)"
# 1000 loops, best of 5: 5.45 msec per loop

# ************************************************************************

# $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.sieve(10)"
# 1000 loops, best of 5: 11 usec per loop

# 13:42 $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.sieve(20)"
# 1000 loops, best of 5: 21.8 usec per loop

# 13:43 $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.sieve(100)"
# 1000 loops, best of 5: 132 usec per loop

# 13:43 $ python3.9 -m timeit -n 1000 -s "import task_2" "task_2.sieve(200)"
# 1000 loops, best of 5: 279 usec per loop


