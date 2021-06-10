#!/usr/bin/env python
# coding: utf-8

# In[ ]:


change_list = []
i = 0
while True:
    new_data = input('Введите данные (для выхода из программы введите 0): ')
    if new_data == '0':
        break
    else:
        change_list.append(new_data)
        if i % 2 != 0 and i != 0:
            new_data = change_list[i-1]
            change_list[i-1] = change_list[i]
            change_list[i] = new_data
        i += 1
print(change_list)

