with open("text_for_ex4_m.txt", "r", encoding="utf-8") as f, open("text_for_ex4_p.txt", "w", encoding="utf-8") as fw:
    rus_num = ('Один', 'Два', 'Три', 'Четыре')
    i = 0
    for line in f:
        fw.write(f'{rus_num[i]} {line.split()[1]} {line.split()[2]}\n')
        i += 1