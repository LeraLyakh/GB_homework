with open("text_for_ex2.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
m = 0
for line in content:
    split_line = line.split()
    n = 0
    for word in split_line:
        n += 1
    m += 1
    print (f'В строке {m} содержится {n} слов')
print(f'Всего {m} строки')