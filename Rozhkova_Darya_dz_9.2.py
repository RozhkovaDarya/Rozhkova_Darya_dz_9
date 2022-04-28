class Road:
  def __init__(self, length, width):
    self._length = length
    self._width = width

class MassCount(Road):
  def __init__(self, length, width, road_thickness, mass_road_on_1cm=25):
    self.road_thickness = road_thickness
    super().__init__(length, width)
    self.mass = self._length * self._width * self.road_thickness * mass_road_on_1cm
    print(self.mass)

volume = MassCount(60, 5, 7)