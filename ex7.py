def fact(n):
    for el in range(1, n+1):
        yield el
n = int(input('Введите число: '))+1
for i in range (1, n):
    factorial = 1
    for el in fact(i):
        factorial *= el
    print(f'{i}! = {factorial}')
