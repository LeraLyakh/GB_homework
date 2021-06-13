from sys import argv
print (f'Выработка в часах: {float(argv[1])} ч')
print (f'Ставка: {float(argv[2])} денег в час')
print (f'Премия: {float(argv[3])} денег')
print(float(argv[1]) * float(argv[2]) + float(argv[3]))
