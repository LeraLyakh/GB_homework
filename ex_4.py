#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 4
num = input('Введите число: ')
i = 0;
max_num = num[i]
    while i < (len(num) - 1):
        if num[i + 1] > max_num:
            max_num = num[i + 1]
        i += 1
print (f'Самая большая цифра: {max_num}')

