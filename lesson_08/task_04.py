# homework. lesson: 08, task: 04

"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).

В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self, address: str):
        self.address = address
        self.items = []


class OfficeEquipment:
    def __init__(self, name: str):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name: str, printer_value: str):
        self.printer_value = printer_value
        super().__init__(name)


class Scanner(OfficeEquipment):
    def __init__(self, name: str, scanner_value: str):
        self.scanner_value = scanner_value
        super().__init__(name)


class Xerox(OfficeEquipment):
    def __init__(self, name: str, xerox_value: str):
        self.xerox_value = xerox_value
        super().__init__(name)

