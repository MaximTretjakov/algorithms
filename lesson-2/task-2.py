"""
    Ссылка на блок-схемы: https://drive.google.com/file/d/1GTGo-20iB7krcEjQWnVV_7rLL1q6p8RB/view?usp=sharing

    2. Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

data = int(input('Введите натуральное, целое число'))
even = odd = 0
while data > 0:
    if data % 2 == 0:
        even += 1
    else:
        odd += 1
    data = data // 10   # отбрасываем единицу чтобы определить следующую цифру на четность\нечетность

print(f'чет --> {even}, нечет --> {odd}')
