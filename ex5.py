with open("text_for_ex5.txt", "w+") as f:
    numbers = input('Введите числа через пробел: ').split()
    for num in numbers:
        if num.isdigit() == True:
            f.write(f'{num} ')
    f.seek(0)
    print(f'Сумме чисел: {sum([float(num) for num in f.readline().split()] )}')
