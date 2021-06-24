class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        fn = f'{self.name} {self.surname}'
        return fn

    def get_total_income(self):
        ti = sum(self._income.values())
        return ti


w = Position('Иван', 'Иванов', 'менеджер', 50000, 15000)
print(w.name)
print(w.surname)
print(w.position)
print(w._income)
print()
print(w.get_full_name())
print(f'Доход: {w.get_total_income()}')