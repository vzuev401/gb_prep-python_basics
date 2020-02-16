# homework. lesson: 08, task: 05

"""
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании.

Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например, словарь.
"""


class WarehouseItemError(Exception):
    ...


class DuplicatedItemError(WarehouseItemError):
    ...


class MissedItemError(WarehouseItemError):
    ...


class IncorrectItemType(WarehouseItemError):
    ...


class Warehouse:
    __instances = []

    def __init__(self, address: str):
        self.address = address
        self.items = []

        Warehouse.__instances.append(self)

    def __new__(cls, address: str):
        for instance in Warehouse.__instances:
            if address == instance.address:
                return instance

        return object.__new__(cls)

    def store(self, item: 'OfficeEquipment'):
        if not isinstance(item, OfficeEquipment):
            raise IncorrectItemType

        if item in self.items:
            raise DuplicatedItemError

        self.items.append(item)

    def transfer(self, item: 'OfficeEquipment', to: str):
        if item in self.items:
            self.items.remove(item)
            print(f'"{item}" successfully transferred to {to}')
            return

        raise MissedItemError

    def search(self, item_type: type = None, /, search_word: str = None):
        items = self.items.copy()

        if item_type is not None:
            items = [item for item in items if isinstance(item, item_type)]

        if search_word is not None:
            items = [item for item in items if search_word in item.name]

        return items


class OfficeEquipment:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'OE: {self.name}'


class Printer(OfficeEquipment):
    def __init__(self, name: str, printer_value: str):
        self.printer_value = printer_value
        super().__init__(name)

    def __str__(self):
        return f'PRINTER: {self.name}'


class Scanner(OfficeEquipment):
    def __init__(self, name: str, scanner_value: str):
        self.scanner_value = scanner_value
        super().__init__(name)

    def __str__(self):
        return f'SCANNER: {self.name}'


class Xerox(OfficeEquipment):
    def __init__(self, name: str, xerox_value: str):
        self.xerox_value = xerox_value
        super().__init__(name)

    def __str__(self):
        return f'XEROX: {self.name}'


warehouse = Warehouse('some addr')
duplicated_warehouse = Warehouse('some addr')

duplicated_warehouse.store(Printer('printer 1', 'P!'))
warehouse.store(Printer('printer 1', 'P@'))
duplicated_warehouse.store(Printer('printer 2', 'P@'))
warehouse.store(Printer('printer 3', 'P#'))
duplicated_warehouse.store(Printer('printer 3', 'P#'))
duplicated_warehouse.store(Printer('printer 3', 'P$'))
warehouse.store(Printer('printer 4', 'P$'))


# Trying to add an item already stored
#
# // Start
special_scanner = Scanner('WTScanner 8000', 'S!')

duplicated_warehouse.store(special_scanner)

try:
    warehouse.store(special_scanner)
except DuplicatedItemError:
    print('DUPLICATION!!~', special_scanner)
    print()
# \\ End

warehouse.store(Scanner('scanner 2', 'S@'))

warehouse.store(Xerox('xerox 1', 'X!'))
duplicated_warehouse.store(Xerox('xerox 1', 'X@'))
duplicated_warehouse.store(Xerox('xerox 2', 'X@'))
duplicated_warehouse.store(Xerox('xerox 3', 'X#'))
warehouse.store(Xerox('xerox 3', 'X#'))

print('Items with "2":')
print(warehouse.search(search_word=' 2'))
print()

for item in warehouse.search(search_word=' 2'):
    warehouse.transfer(item, 'somewhere')

print()
print('Items with "2"')
print(duplicated_warehouse.search(search_word=' 2'))
print()

# Trying to move a missing item
#
# // Start
another_special_scanner = Scanner('WTScanner 3000', 'S!')

try:
    warehouse.transfer(another_special_scanner, 'somewhere')
except MissedItemError:
    print('MISSED!!~', another_special_scanner)
    print()
# \\ End
