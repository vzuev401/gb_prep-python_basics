from typing import Union


class Road:
    def __init__(self, length: Union[float, int], width: Union[float, int]):
        self._length = length
        self._width = width

    def mass_calc(
        self,
        mass: Union[float, int],
        thickness: Union[float, int]
    ) -> Union[int, float]:
        return self._length * self._width * mass * thickness


road = Road(5000, 20)
print('mass:', road.mass_calc(25, 5) / 1000, 't')

