def my_func(sort_list):
   # sort_list = [a, b, c]
    sort_list.remove(min(sort_list))
    result = 0
    for i in range(len(sort_list)):
        result += sort_list[i]
    return result

sort_list = []
for i in range(3):
    sort_list.append(float(input('Введите значение: ')))

print(f'Результат: {my_func(sort_list)}')