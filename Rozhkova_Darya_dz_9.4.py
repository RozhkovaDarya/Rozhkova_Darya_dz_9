class Car:
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police

  def go(self):
    return f'{self.name} поехала'

  def stop(self):
    return f'{self.name} остановилась'

  def turn_right(self):
    return f'{self.name} повернула направо'

  def turn_left(self):
    return f'{self.name} повернула налево'

  def show_speed(self):
    return f'Текущая скорость {self.name} {self.speed} км/ч'


class TownCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
  def show_speed(self):
    print(f'Текущая скорость городского автомобиля {self.name} {self.speed} км/ч')

    if self.speed > 40:
      return f'Скорость {self.name} превышена!'

    else:
      return f'Скорость {self.name} в пределах допустимого'


class WorkCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
  def show_speed(self):
    print(f'Текущая скорость рабочего автомобиля {self.name} {self.speed} км/ч')

    if self.speed > 60:
      return f'Скорость {self.name} превышена!'

    else:
      return f'Скорость {self.name} в пределах допустимого'


class SportCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
  def show_speed(self):
    print(f'Текущая скорость рабочего автомобиля {self.name} {self.speed} км/ч')


class PoliceCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)

  def police(self):
    if self.is_police:
      return f'{self.name} это полиция'

    else:
      return f'{self.name} это не полиция'

oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(65, 'White', 'Lada', False)
audi = SportCar(100, 'Red', 'Audi', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)

print(lada.turn_left())
print(f'Когда {oka.turn_right()}, {audi.stop()}')
print(f'{lada.name} {lada.color}')
print(f'{audi.name} это полиция? {audi.is_police}')
print(f'{lada.name}  это полиция? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
