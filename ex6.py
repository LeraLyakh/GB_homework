from itertools import count, cycle


n = int(input('Введите начальное число: '))
m = int(input('Введите конечное число: '))
print()
print('COUNT')
for el in count(n):
    if el > m:
        break
    else:
        print(el)
print ()
print('CYCLE')
my_list = ['утро', 'день', 'вечер', 'ночь']
i = 0
for el in cycle(my_list):
    if i > m:
        break
    if i % len(my_list) == 0:
        print()
    print(el)
    i += 1
