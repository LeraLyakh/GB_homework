with open("text_for_ex3.txt", "r", encoding="utf-8") as f:
    salary_dict = {line.split()[0]: float (line.split()[1]) for line in f}
low_salary = ' '.join([name for name in salary_dict if salary_dict.get(name) < 20000])
average = sum(salary_dict.values())/len(salary_dict)

print(f'Сотрудники с зарплатой ниже 20 000 рублей: {low_salary}\nСредняя зарплата: {average} рублей')


