"""
    1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
    для каждого предприятия.
    Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
    наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections
import random


Company = collections.namedtuple('Company', ['p1', 'p2', 'p3', 'p4'])
companes = {}
total_profit = ()

# заполняем
n = int(input("Количество компаний: "))
for i in range(n):
    company_name = input(str(i+1) + '-я компания: ')
    profit_p1 = int(input('Прибыль в 1-й квартал: '))
    profit_p2 = int(input('Прибыль в 2-й квартал: '))
    profit_p3 = int(input('Прибыль в 3-й квартал: '))
    profit_p4 = int(input('Прибыль в 4-й квартал: '))
    companes[company_name] = Company(
        p1=profit_p1,
        p2=profit_p2,
        p3=profit_p3,
        p4=profit_p4
    )

# сумма за год и общая по всем компаниям
for company_name, profit in companes.items():
    print(f'Компания: {company_name} прибыль за год - {sum(profit)}')
    total_profit += profit

# рассчет среднего для всех
avg_profit_total = sum(total_profit) / len(companes)
print(f'Средняя прибыль за год для всех компаний {avg_profit_total}')

# больше менбше
print('Компании, у которых прибыль выше среднего:')
for company_name, profit in companes.items():
    if sum(profit) > avg_profit_total:
        print(f'{company_name} - {sum(profit)}')

print('Компании, у которых прибыль меньшк среднего:')
for company_name, profit in companes.items():
    if sum(profit) < avg_profit_total:
        print(f'{company_name} - {sum(profit)}')
