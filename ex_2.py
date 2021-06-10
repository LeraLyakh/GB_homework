#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 2
seconds = int(input('Количество секунд = '))
hours = int(seconds // 3600)
seconds = int(seconds % 3600)
minutes = int(seconds // 60)
seconds = int(seconds % 60)
print (f'{hours}:{minutes}:{seconds}')

