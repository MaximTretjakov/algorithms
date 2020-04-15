"""
    1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
    Примечание. Идеальным решением будет:
    ● выбрать хорошую задачу, которую имеет смысл оценивать,
    ● написать 3 варианта кода (один у вас уже есть),
    ● проанализировать 3 варианта и выбрать оптимальный,
    ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
    ● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

import timeit
import cProfile
import random


# вариант из ДЗ.
def get_even_ind(size):
    min_item = 0
    max_item = 1000000
    array = [random.randint(min_item, max_item) for _ in range(size)]

    res = []
    for i in range(size):
        if array[i] % 2 == 0:
            res.append(i)
    return res


print(timeit.timeit('get_even_ind(300000)', number=100, globals=globals()))     # 27.362353289999874
print(timeit.timeit('get_even_ind(600000)', number=100, globals=globals()))     # 53.23987481899985
print(timeit.timeit('get_even_ind(900000)', number=100, globals=globals()))     # 80.16283023200003
print(timeit.timeit('get_even_ind(1200000)', number=100, globals=globals()))    # 106.27893516999984
print(timeit.timeit('get_even_ind(1500000)', number=100, globals=globals()))    # 133.39984958800005
print('\n')


# вариант 1. Этот варинат мне нравится больше потому что он работает побыстрее и компактнее.
def get_even_ind1(size):
    min_item = 0
    max_item = 1000000
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return [i for i in range(size) if array[i] % 2 == 0]


print(timeit.timeit('get_even_ind1(300000)', number=100, globals=globals()))    # 26.410614169999917
print(timeit.timeit('get_even_ind1(600000)', number=100, globals=globals()))    # 52.881418177999876
print(timeit.timeit('get_even_ind1(900000)', number=100, globals=globals()))    # 79.20067433900022
print(timeit.timeit('get_even_ind1(1200000)', number=100, globals=globals()))   # 105.728113699
print(timeit.timeit('get_even_ind1(1500000)', number=100, globals=globals()))   # 132.66937920700002
print('\n')


# вариант 2. Тут я намеренно сделал лишних телодвижений чтобы было похуже.
def get_even_ind2(size):
    i = min_item = 0
    max_item = 1000000
    array = [random.randint(min_item, max_item) for _ in range(size)]

    res = []
    for i in range(size):
        if array[i] % 2 == 0:
            res.append(i)
    return map(lambda x: res.append(i), [i for i in range(size) if i % 2 == 0])


print(timeit.timeit('get_even_ind2(300000)', number=100, globals=globals()))    # 28.444977222000034
print(timeit.timeit('get_even_ind2(600000)', number=100, globals=globals()))    # 56.77653339200015
print(timeit.timeit('get_even_ind2(900000)', number=100, globals=globals()))    # 85.27984558400021
print(timeit.timeit('get_even_ind2(1200000)', number=100, globals=globals()))   # 114.1955059220004
print(timeit.timeit('get_even_ind2(1500000)', number=100, globals=globals()))   # 142.52530624600013
print('\n')


def main():
    get_even_ind(100000)


cProfile.run('main()')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.142    0.142 <string>:1(<module>)
#    100000    0.044    0.000    0.092    0.000 random.py:174(randrange)
#    100000    0.020    0.000    0.113    0.000 random.py:218(randint)
#    100000    0.034    0.000    0.048    0.000 random.py:224(_randbelow)
#         1    0.010    0.010    0.141    0.141 task-1.py:17(get_even_ind)
#         1    0.017    0.017    0.130    0.130 task-1.py:20(<listcomp>)
#         1    0.001    0.001    0.142    0.142 task-1.py:74(main)
#         1    0.000    0.000    0.142    0.142 {built-in method builtins.exec}
#     50138    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#    100000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    104807    0.010    0.000    0.010    0.000 {method 'getrandbits' of '_random.Random' objects}


# Вывод:
# Из всех вариантов решения мне понравился вариант get_even_ind1.
# Он быстрее и компактнее при одинаковом количестве запусков и N.
# Имеет линейную асимптотику О(n).
