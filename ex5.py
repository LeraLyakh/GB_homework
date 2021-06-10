#!/usr/bin/env python
# coding: utf-8

# In[ ]:


my_list = [7, 5, 3, 3, 2]

while True:
    num = input('Введите данные (для выхода из программы введите Q): ').upper()
    if num == 'Q':
        break
    elif num.isdigit()== True:
        num = int(num)
        for i in range(len(my_list)):
            if my_list[i] <= num:
                my_list.insert(i, num)
                break
            else:
                if i == len(my_list)-1:
                    my_list.append(num)
    else:
        print('Некорректное значение. Значение должно быть числом')
            
print(my_list)

