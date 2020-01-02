# coding: utf-8


class Item:
    def __init__(self, name, value, name_accusative=None):
        self.name = name
        self.value = value
        self.name_accusative = name_accusative or self.name


class Weapon(Item):
    def __init__(self, name, damage, value, name_accusative=None):
        super().__init__(name, value, name_accusative)
        self.damage = damage

    def __str__(self):
        return f'{self.name_accusative} (útok +{self.damage})'


class Consumable(Item):
    def __init__(self, name, healing_value, value, name_accusative=None):
        super().__init__(name, value, name_accusative)
        self.healing_value = healing_value

    def __str__(self):
        return f'{self.name_accusative} (+{self.healing_value} % zdraví)'
