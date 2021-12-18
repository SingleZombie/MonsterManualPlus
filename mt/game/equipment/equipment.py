from typing import List

from ..effect import Effect


class Equipment():

    def __init__(self, effects: List[Effect]):
        self.effects = effects


equipment_list = {}


def register_equipment(name: str):

    def decorator(equipment_cls: type):
        equipment_list[name] = equipment_cls
        return equipment_cls

    return decorator


def build_equipment(name):
    return equipment_list[name]()
