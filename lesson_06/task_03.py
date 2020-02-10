from typing import Union
from math import pi


class Worker:
    def __init__(
        self,
        name: str,
        surname: str,
        position: str,
        wage: Union[int, float],
        bonus: Union[int, float]
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> Union[str, int]:
        return sum(self._income.values())


position = Position('Name', 'Surname', 'Position', 42, pi)

print(position.get_full_name())
print(position.get_total_income())

