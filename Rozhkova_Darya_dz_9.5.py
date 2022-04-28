class Stationery:
  def __init__(self, title):
    self.title = title

  def draw(self):
    return f'Запуск отрисовки'


class Pen(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return f'Запуск отрисовки ручкой'


class Pencil(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return f'Запуск отрисовки карандашом'


class Handle(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return f'Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(pen.title)
print(pen.draw())
print('\n')

print(pencil.title)
print(pencil.draw())
print('\n')

print(handle.title)
print(handle.draw())