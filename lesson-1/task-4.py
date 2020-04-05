"""
    блок-схема: https://drive.google.com/file/d/1fum955_eKLcDlSPouna657uZxIfMnv14/view?usp=sharing

    4. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

    Работает только с английскими маленькими буквами.
    'a' - латинская имеет 97 ascii код + номер буквы - 1 index
"""

print('Введите номер буквы в алфавите.')
sym = int(input('---> '))

sym = ord('a') + sym - 1
print(f'Это --> {chr(sym)}')
