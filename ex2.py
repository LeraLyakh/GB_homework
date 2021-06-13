from random import randint
first_list = []
n = int(input('Введите количество элементов списка: '))
first_list = [randint(0, 1000) for el in range(n) ]
print(f'Исходный список: {first_list}')

new_list = [first_list[i] for i in range(1, len(first_list)) if first_list[i] > first_list[i-1] ]
print(f'Результат: {new_list}')