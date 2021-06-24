class Stationary:

    def __init__(self, title='Название'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'Пишем ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Рисуем карандашом')


class Handle(Stationary):
    def draw(self):
        print(f'Отмечаем маркером')

stat = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()

stat_list = [stat, pen, pencil, handle]

for i in stat_list:
    i.draw()
