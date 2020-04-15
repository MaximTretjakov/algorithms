"""
    2. Написать два алгоритма нахождения i-го по счёту простого числа.
    Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
    Проанализировать скорость и сложность алгоритмов.

    Первый — с помощью алгоритма «Решето Эратосфена».
    Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
    Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
    Второй — без использования «Решета Эратосфена».
"""

import timeit


def sieve(n):
    if n == 1:
        n = 2
    elif n == 0:
        return -1
    # формирую решето как n * n этого хватит и не будет оверхеда.
    _sieve = [i for i in range(n * n)]
    _sieve[1] = 0
    _res = []
    for i in range(2, n * n):
        if _sieve[i] != 0:
            j = i * 2
            # не нулевые элементы складываем в результирующий список
            _res.append(_sieve[i])
            while j < n * n:
                _sieve[j] = 0
                j += i
        if len(_res) == n:
            break
    # корректирууем индекс
    return _res[n - 1]


print(timeit.timeit('sieve(300)', number=100, globals=globals()))     # 1.9212271879987384
print(timeit.timeit('sieve(600)', number=100, globals=globals()))     # 8.45483898600105
print(timeit.timeit('sieve(900)', number=100, globals=globals()))     # 21.133728531000088
print(timeit.timeit('sieve(1200)', number=100, globals=globals()))    # 42.38479882700085
print(timeit.timeit('sieve(1500)', number=100, globals=globals()))    # 68.80187030600064
print('\n')


def _prime(n):
    x = 2
    # классический способ проверки числа на простоту взятие отстатка от деления
    while x * x <= n and n % x != 0: x += 1
    # используем эту хитрожопую конструцию чтобы возвратить True\False
    return x * x > n


def prime(n):
    if n == 1:
        n = 2
    elif n == 0:
        return -1
    _res = []
    for i in range(2, n * n):
        # если True то складываем числа в список.
        if _prime(i):
            _res.append(i)
        if len(_res) == n:
            break
    return _res[n - 1]


print(timeit.timeit('prime(3000)', number=100, globals=globals()))     # 3.817974043000504
print(timeit.timeit('prime(6000)', number=100, globals=globals()))     # 10.857019451999804
print(timeit.timeit('prime(9000)', number=100, globals=globals()))     # 19.710060119001355
print(timeit.timeit('prime(12000)', number=100, globals=globals()))    # 30.996826088998205
print(timeit.timeit('prime(15000)', number=100, globals=globals()))    # 44.457021832000464
print('\n')


# Вывод:
# выражение генератор [i for i in range(n * n)] видимо О(n).
# ниже идут 2 цткла О(n^2) и в итоге О(n^2) + О(n).
# Видимо так, но я не уверен что правильно записал.
#
# Во второй функции по сути 2 цикла О(n^2). Первый основной, второй в _prime()
#
