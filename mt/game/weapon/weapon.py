from ..effect import Effect
from typing import List


class Weapon():
    def __init__(self, effects: List[Effect]):
        self.effects = effects


weapon_list = {}


def register_weapon(name: str):
    def decorator(weapon_cls: type):
        weapon_list[name] = weapon_cls
        return weapon_cls

    return decorator


def build_weapon(name, *args, **kwargs):
    return weapon_list[name](*args, **kwargs)
