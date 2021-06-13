
first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список: {first_list}')

new_list = [first_list[i] for i in range(0, len(first_list)) if (first_list[i] not in first_list[i+1:]) and (first_list[i] not in first_list[:i])]
print(f'Результат: {new_list}')