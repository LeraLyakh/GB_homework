with open("text_for_ex6.txt", "r", encoding="utf-8") as f:
    lessons_keys = [line.split(':')[0] for line in f]
    f.seek(0)
    lessons_val = [line.split()[1:] for line in f]
lessons_val_f = []
j = 0
for li in lessons_val:
    i = 0
    for val in li:
        val = ''.join(letter for letter in val if letter.isdigit())
        if val != '':
            if i == 0:
                lessons_val_f.append(float(val))
            else:
                lessons_val_f [j] += float(val)
            i += 1
    j += 1

lessons_dict = {lessons_keys[i]:lessons_val_f[i] for i in range(len(lessons_keys))}
print(lessons_dict)
