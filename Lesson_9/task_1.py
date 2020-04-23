# 1. Определение количество различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция
# вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)

import hashlib


def substring_count(s: str) -> int:
    assert len(s) > 0, 'Строка не может быть пустой'

    set_hash = set()
    s_hash = hashlib.sha1(s.encode('utf-8')).hexdigest()

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            spam = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            if spam != s_hash:
                set_hash.add(spam)

    return len(set_hash)


s = input('Введите строку: ')
num = substring_count(s)

print(f'Количество подстрок {num}')
