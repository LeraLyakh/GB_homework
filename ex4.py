def my_func (x, y):
    result = x**y
    return result
def my_func_2 (x, y):
    result = 1
    if y > 0:
        for i in range(y):
            result = result * x
    elif y < 0:
        x = 1/x
        for i in range(y*(-1)):
            result = result * x
    return result


x = float(input('x = '))
y = int(input('y = '))
print(f'**: {my_func (x, y)}')
print(f'Цикл: {my_func_2 (x, y)}')