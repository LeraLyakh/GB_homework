#!/usr/bin/env python
# coding: utf-8

# In[36]:


class Matrix:

    def __init__(self, li_of_li):
        self.li_of_li = li_of_li
    
    def __str__(self):
        s = '\n'.join(map(str, self.li_of_li))
        return s
    
    def __add__(self, other):
        mc = []
        for i in range(len(self.li_of_li)):
            mc.append([])
            for j in range(len(self.li_of_li[0])):
              #  mc[i].append([])
                mc[i].append(self.li_of_li[i][j] + other.li_of_li[i][j])
        s = '\n'.join(map(str, mc))
        return s

a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

b = [[9, 8, 7], 
     [6, 5, 4], 
     [3, 2, 1]]

ma = Matrix(a)
mb = Matrix(b)

print(f'\n\nМатрица а: \n\n{ma}')
print('')
print(f'\n\nМатрица b: \n\n{mb}')
print('')
print(f'\n\n   a + b: \n\n{ma + mb}')


# In[ ]:




