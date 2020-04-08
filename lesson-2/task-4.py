"""
    Ссылка на блок-схемы: https://drive.google.com/file/d/1GTGo-20iB7krcEjQWnVV_7rLL1q6p8RB/view?usp=sharing

    4. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    Вывести на экран это число и сумму его цифр.
"""


def get_sum(dec):
    s = 0
    while dec > 0:
        s += dec % 10
        dec = dec // 10
    return s


print('Введите натуральное, целое число')
max_sum = tmp = 0
while True:
    num = int(input('--> '))
    if num == 0:
        print(f'Выход из программы | число {tmp} | сумма {max_sum} |')
        break
    tmp = num
    summa = get_sum(num)
    if summa > max_sum:
        max_sum = summa
