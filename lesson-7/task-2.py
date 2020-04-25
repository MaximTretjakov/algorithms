"""
    Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
    заданный случайными числами на промежутке [0; 50).
    Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge(left, right):
    sorted_ = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_.append(left[i])
            i += 1
        else:
            sorted_.append(right[j])
            j += 1

    sorted_ += left[i:]
    sorted_ += right[j:]
    return sorted_


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    # print(f'left {left} right {right}')
    return merge(left, right)


if __name__ == '__main__':
    SIZE = 10
    PRECISION = 2
    spam = [0] * SIZE
    array = [round(random.uniform(0, 49), PRECISION) for _ in range(SIZE)]
    print(f'Исходный массив = {array}')
    print(f'Отсортированный = {merge_sort(array)}')
