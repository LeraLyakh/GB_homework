#!/usr/bin/env python
# coding: utf-8

# In[8]:



class Cells:
    
    def __init__(self, nums, cell):
        self.param = [nums, cell]
    
    def __add__(self, other):
        new_cell = [self.param[0] + other.param[0], self.param[1] + other.param[1]]
        return new_cell
    
    def __sub__(self, other):
        if self.param[0]- other.param[1] > 0:
            new_cell = [self.param[0] - other.param[0], self.param[1] - other.param[1]]
        else:
            new_cell = 'Операция невозможна'
        return new_cell
    
    def __mul__(self, other):
        new_cell = [self.param[0] * other.param[0], self.param[1] * other.param[1]]
        return new_cell
            
    def __truediv__(self, other):
        new_cell = [self.param[0] // other.param[0], self.param[1] // other.param[1]]
        return new_cell
    
    def make_order(self):
        c = '\n'.join(['*' * self.param[0] for i in range(self.param[1] // self.param[0])]) + '\n' + '*' * (self.param[1] % self.param[0])
        return  c
    
    
cell_1 = Cells(7, 10)
cell_2 = Cells(2, 3)
print (cell_1 + cell_2)
print (cell_1 - cell_2)
print (cell_1 * cell_2)
print (cell_1 / cell_2)

print(cell_1.make_order())
        


# In[ ]:




