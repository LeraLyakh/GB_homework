#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 5
proceed = float(input('Выручка: '))
cost = float(input('Издержка: '))
result = proceed - cost
if result < 0:
    print (f'Убыток: {-1*result}')
elif result > 0:
    print (f'Прибыль: {result}')
    print (f'Рентабельность прибыли: {result/proceed}')
    staff = int(input('Количество сотрудников фирмы: '))
    print(f'Прибыль на одного сотрудника составляет: {result/staff}')
else:
    print ('Точка безубыточности')

