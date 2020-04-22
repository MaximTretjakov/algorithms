"""
    Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
    Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
    Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

    ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
    ● написать 3 варианта кода (один у вас уже есть);
    ● проанализировать 3 варианта и выбрать оптимальный;
    ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
      Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
    ● написать общий вывод: какой из трёх вариантов лучше и почему.

    Я выбрал 2 задачу 3-его урока: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    OC Linux X64, Python 3.7.5 X64

"""

import sys
import random


def sum_memory(x):
    sum_ = sys.getsizeof(x)
    print(f'TYPE = {type(x)}  |  SIZE = {sum_}  |  OBJ = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                sum_ += sum_memory(key)
                sum_ += sum_memory(value)
        elif not isinstance(x, str):
            for item in x:
                sum_ += sys.getsizeof(item)
    return sum_


def min_max_change(array, size):
    """
    Переделал под функцию.
    Возвращает min_, max_ в общем случае, но в данном дикт атрибутов функции.
    NУдобнее измерять память.
    """

    #   если на вход придёт dict
    if isinstance(array, dict):
        array = [j for j in array.values()]

    min_ = 0
    max_ = 0
    for i in range(size):
        if array[i] < array[min_]:
            min_ = i
        elif array[i] > array[max_]:
            max_ = i

    b = array[min_]
    array[min_] = array[max_]
    array[max_] = b
    # return min_, max_
    return locals()


if __name__ == '__main__':

    SIZE = 10
    MIN_ITEM = 0
    MAX_ITEM = 10

    test_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    test_dict = {'d': 1, 'w': 2, 'e': 0}

    for k in [test_arr, test_dict]:
        dict_atr = min_max_change(k, len(k))
        variables = [value for key, value in dict_atr.items()]
        print(f'Всего занято памяти {sum_memory(variables)}')


# Вывод:
# не стал использовать tuple т.к у него нет __setitem__, а мне нужно переставлять элементы и возникала ошибка.
# в функцию подаю рандомный list и dict с числами.
# list занял всего памяти = 476
# dict занял всего памяти = 376
# я выбираю dict в замерах он меньше потребляет памяти.
