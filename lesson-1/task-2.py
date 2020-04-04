"""
    блок-схема: https://drive.google.com/file/d/1fum955_eKLcDlSPouna657uZxIfMnv14/view?usp=sharing

    2. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print('Введите три положительных числа.')
x = int(input('---> '))
y = int(input('---> '))
z = int(input('---> '))

if y < x < z or z < x < y:
    print(f'Средний результат: {x}')
elif x < y < z or z < y < x:
    print(f'Средний результат: {y}')
else:
    print(f'Средний результат: {z}')
