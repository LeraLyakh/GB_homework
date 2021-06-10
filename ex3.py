#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ('Решение через список')
num_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
while True:
    num = int(input('Номер месяца: '))
    if num > 12:
        print('Номер месяца не должен превышать 12')
    else:
        for row in range(len(num_list)):
            if num in num_list[row]:
                print(f'Время года: {seasons[row]}')
        break
print()
print ('Решение через словарь')       
seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
while True:
    num = int(input('Номер месяца: '))
    if num > 12:
        print('Номер месяца не должен превышать 12')
    else:
        for keys in seasons:
                if num in seasons.get(keys):
                    print (f'Время года: {keys}')
        break

