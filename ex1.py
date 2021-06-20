with open("text_for_ex1.txt", "w") as f:
    while True:
        t = input()
        if t == '':
            break
        f.write(f'{t} \n')