class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашем.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')


pen = Pen('A_01')
pencil = Pencil('B_02')
handle = Handle('C_03')

pen.draw()
pencil.draw()
handle.draw()

