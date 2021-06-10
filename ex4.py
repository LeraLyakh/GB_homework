#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str_list = input().split()
for i in range(len(str_list)):
    print(f'{i+1}: {str_list[i][:10]}')

