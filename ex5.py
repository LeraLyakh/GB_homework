def sum_list(list_of_num, sum):
    exit = False
    try:
        for i in list_of_num:
            if i.replace('.','').isdigit():
                i = float(i)
                sum += i
            elif i.upper() == 'Q':
                exit = True
            else:
                print('Некорректный ввод')
    except ValueError:
        print ('Некорректный ввод')
    return sum, exit

sum = 0
while True:
    data_list = input('Введите числа через пробел. Для выхода введите Q: ').split()
    sum, exit = sum_list(data_list, sum)
    print(f'Результат: {sum}')
    if exit == True:
        break
