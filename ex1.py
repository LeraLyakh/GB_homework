#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def division(a, b):
    if a == 0 and b == 0:
        result_1 = 'Деление на ноль'
        result_2 = 'Деление на ноль'
    elif b == 0:
        result_1 = 'Деление на ноль'
        result_2 = b/a
    elif a == 0:
        result_1 = a/b
        result_2 = 'Деление на ноль'
    else:
        result_1 = a/b
        result_2 = b/a
    return result_1, result_2
arguments = []
for i in range(2):
    arguments.append(float(input('Введите число: ')))
result = division(arguments[0], arguments[1])
print(f'{arguments[0]} / {arguments[1]} = {result[0]} \n{arguments[1]} / {arguments[0]} = {result[1]}')

