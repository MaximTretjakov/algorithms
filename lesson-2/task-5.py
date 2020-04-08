"""
    Ссылка на блок-схемы: https://drive.google.com/file/d/1GTGo-20iB7krcEjQWnVV_7rLL1q6p8RB/view?usp=sharing

    5. В программе генерируется случайное целое число от 0 до 100.
    Пользователь должен его отгадать не более чем за 10 попыток.
    После каждой неудачной попытки должно сообщаться,
    больше или меньше введенное пользователем число, чем то, что загадано.
    Если за 10 попыток число не отгадано, вывести правильный ответ.
"""

from random import random


def guessing_game(i, n):
    max_count = 10
    if i <= max_count:
        user_num = int(input(f'{str(i)} -я попытка: '))
        if user_num > n:
            return f'\n{str(i)} -я попытка: Много {guessing_game(i+1, n)}'
        elif user_num < n:
            return f'\n{str(i)} -я попытка: Мало {guessing_game(i+1, n)}'
        else:
            return f'\nВы угадали с {i}-й попытки'
    else:
        return f'\nВы исчерпали 10 попыток. Было загадано {n}'


if __name__ == '__main__':
    rand_num = round(random() * 100)
    index = 1
    print('есть 10 попыток')
    res = guessing_game(index, rand_num)
    print(res)
