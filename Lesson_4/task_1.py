# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

import cProfile
import functools


def test_sum(funk):
    """Функция тестирования работы алгоритма"""
    lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625, 0.66796875]
    for i, item in enumerate(lst, 1):
        assert item == funk(i)
        print(f'Test {i} OK')


def sum_loop(n):
    """"Реализация  циклического алгоритма"""
    item = 1
    result = 0

    for i in range(n):
        result += item
        item /= -2

    return result


def _sum(n, item=1):
    """Реализация рекурсивного алгоритма (не оптимизированный)"""
    if not n:
        return 0
    return item + _sum(n - 1, item / -2)


@functools.lru_cache()
def _sum_(n, item=1):
    """Реализация рекурсивного алгоритма (оптимизированный)"""
    if not n:
        return 0
    return item + _sum(n - 1, item / -2)


# *******************************************************************************
# test_sum(sum_loop)
# *******************************************************************************

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1.sum_loop(10)"
# 1000 loops, best of 5: 685 nsec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1.sum_loop(20)"
# 1000 loops, best of 5: 1.11 usec per loop

# python3.9 -m timeit -n 1000 -s "import task_1" "task_1.sum_loop(100)"
# 1000 loops, best of 5: 4.48 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1.sum_loop(200)"
# 1000 loops, best of 5: 8.71 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1.sum_loop(500)"
# 1000 loops, best of 5: 23.7 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1.sum_loop(1000)"
# 1000 loops, best of 5: 49.2 usec per loop

# cProfile.run('sum_loop(1000)')

# 1    0.000    0.000    0.000    0.000 task_1.py:14(sum_loop) 10
# 1    0.000    0.000    0.000    0.000 task_1.py:14(sum_loop) 1000

# *******************************************************************************
# test_sum(_sum)
# *******************************************************************************

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum(10)"
# 1000 loops, best of 5: 1.14 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum(20)"
# 1000 loops, best of 5: 2.18 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum(100)"
# 1000 loops, best of 5: 10.3 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum(200)"
# 1000 loops, best of 5: 21.1 usec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum(500)"
# 1000 loops, best of 5: 61.3 usec per loop

# cProfile.run('_sum(500)')

# 11/1     0.000    0.000    0.000    0.000 task_1.py:26(_sum) 10
# 21/1     0.000    0.000    0.000    0.000 task_1.py:26(_sum) 20
# 101/1    0.000    0.000    0.000    0.000 task_1.py:26(_sum) 100
# 201/1    0.000    0.000    0.000    0.000 task_1.py:26(_sum) 200
# 501/1    0.000    0.000    0.000    0.000 task_1.py:26(_sum) 500

# *******************************************************************************
# test_sum(_sum_)
# *******************************************************************************

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum_(10)"
# 1000 loops, best of 5: 72.7 nsec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum_(20)"
# 1000 loops, best of 5: 64.9 nsec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum_(100)"
# 1000 loops, best of 5: 65.4 nsec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum_(200)"
# 1000 loops, best of 5: 65.3 nsec per loop

# $ python3.9 -m timeit -n 1000 -s "import task_1" "task_1._sum_(500)"
# 1000 loops, best of 5: 99.2 nsec per loop

# cProfile.run('_sum(500)')

# 11/1     0.000    0.000    0.000    0.000 task_1.py:26(_sum) 10
# 21/1     0.000    0.000    0.000    0.000 task_1.py:26(_sum) 20
# 101/1    0.000    0.000    0.000    0.000 task_1.py:26(_sum) 100
# 201/1    0.000    0.000    0.000    0.000 task_1.py:26(_sum) 200
# 501/1    0.000    0.000    0.000    0.000 task_1.py:26(_sum) 500

# *******************************************************************************
# Вывод
# *******************************************************************************

# Лучший результат по скорости показал оптимизированный рекурсивный алгоритм _sum_(n).
# Для небольших последовательностей использование данного алгоритма будет лучшим выбором.
# Но у данного алгоритма есть ограничение по стеку вызова функций.
# У циклического алгоритма _sum(n) данное ограничение отсутствует.
# Предпочтение в выборе алгоритма зависит от области решаемой задачи.
