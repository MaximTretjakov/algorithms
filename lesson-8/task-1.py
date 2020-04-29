"""
    1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
    Требуется вернуть количество различных подстрок в этой строке.

    Примечание: в сумму не включаем пустую строку и строку целиком.
    Пример работы функции:

    func("papa")
    6
    func("sova")
    9
"""

import hashlib


def hash_sub_str(string):
    # пустая или строка полностью
    if len(string) == 0 or len(string) == 1:
        return len(string)

    hash_ = []
    offset = 1

    while offset < len(string):
        for i in range(0, len(string)):
            spam = hashlib.sha1(string[i:i + offset].encode('utf-8')).hexdigest()
            hash_.append(spam)
        offset += 1

    res = set(hash_)
    return len(res)


if __name__ == '__main__':
    str_ = input('Введите строку: ')
    count_ = hash_sub_str(str_)
    print(f'строка : {str_}\nподстрок : {count_}')
