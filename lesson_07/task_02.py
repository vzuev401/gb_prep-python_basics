from abc import ABC, abstractmethod
from typing import Union


class Dress(ABC):
    def __init__(self, name: str, measure: Union[int, float]):
        self.name = name
        self.measure = measure

    @property
    @abstractmethod
    def material_consumption(self):
        ...


class Coat(Dress):
    @property
    def material_consumption(self) -> float:
        return self.measure / 6.5 + 0.5

    def __str__(self):
        return f'"{self.name}" with size {self.measure}'


class Suit(Dress):
    @property
    def material_consumption(self) -> float:
        return 2 * self.measure + 0.3

    def __str__(self):
        return f'"{self.name}" with height {self.measure}'


coat = Coat('some coat', 32)
suit = Suit('some suit', 1.8)

for dress in (coat, suit):
    print(dress)
    print('material:', dress.material_consumption)
    print()

