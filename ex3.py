class NotNumberError(Exception):
    def __init__(self):
        super().__init__('Значение некорректно')


my_list = []
while True:
    user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")
    if user_input.lower() == "stop":
        break
    try:
        if not user_input.isdigit():
            raise NotNumberError()
        my_list.append(int(user_input))
    except NotNumberError as e:
        print(e)

print(my_list)