"""
    1. Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = 0
max_ = 1

# берем первый элемент
for i in range(SIZE - 1):
    hit = 1
    # берем элементы после первого
    for j in range(i + 1, SIZE):
        # сравниваем первый со вторым и тд... и если есть совпадения уввеличиваем счетчик hit
        if array[i] == array[j]:
            hit += 1
    # если в hit > max то есть повторения. Сохраняем счетчик в max_ и сохраняем текущий элемент массива
    if hit > max_:
        max_ = hit
        num = array[i]

print(f'число {num} встречается {max_} раза...' if max_ > 1 else 'массив уникален')
