#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Задание 6
a = float(input('В первый день спортсмен пробежал: '))
b = float(input('Требуется суммарно пробежать: '))
day = 1
print (f'{day}-й день: {a} км')
while a < b:
    day += 1
    a = a * 1.1
    print (f'{day}-й день: {round(a, 2)} км')
print (f'На {day}-й день спортсмен достиг результата — не менее 3 км')

