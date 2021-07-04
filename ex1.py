class Date:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def num_date(cls, str_date):
        result = str_date.split(' - ')
        for i in range(len(result)):
            result[i] = int(result[i])
        return f'{result[0]} {result[1]} {result[2]}'

    @staticmethod
    def check_date(str_date):
        result = str_date.split(' - ')
        for i in range(len(result)):
            result[i] = int(result[i])
        day = result[0]
        month = result[1]
        year = result[2]
        if (day > 31 or day < 1) or (month > 12 or month < 1) or (year < 0):
            result = 'Данные введены некорректно'
        else:
            result = f'Данные введены корректно: {result[0]} {result[1]} {result[2]}'
        return result

my_date = Date('04 - 07 - 2021')

print(Date.num_date('23 - 05 - 1996'))
print(my_date.num_date('04 - 07 - 2021'))
print(Date.check_date('243 - 05 - 1996'))
print(my_date.check_date('04 - 07 - 2021'))







