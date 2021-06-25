#!/usr/bin/env python
# coding: utf-8

# In[29]:


from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    
    @property
    @abstractmethod
    def cloth(self):
        pass

    def __add__(self, other):
        return self.cloth + other.cloth
    

class Coat(Clothes):

    @property
    def cloth(self):
        c = self.param / 6.5 + 0.5
        return round(c, 3)

class Costume(Clothes):
    @property
    def cloth(self):
        c = 2 * self.param + 0.3
        return round(c, 3)

    
coat = Coat(42)
costume = Costume(160)

print(f' Ткань для пальто: {coat.cloth}')
print(f' Ткань для костюма: {costume.cloth}')
print(f' Ткани всего: {coat + costume}')


# In[ ]:




