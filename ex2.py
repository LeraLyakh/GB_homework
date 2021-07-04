class Division_by_zero(Exception):
    def __init__(self) :
         super().__init__('Деление на ноль')

def div(value1, value2):
    if value2 == 0:
        raise Division_by_zero()
    return value1 / value2

while True:
    print ('Введите данные, да выхода из программы нажмите Enter')
    a = input('Введите знаменатель: ')
    if a == '':
        break
    b = input('Введите числитель: ')
    try:
        print(f'Результат: {div(float(a), float(b))}')
    except Division_by_zero as e:
        print(e)
