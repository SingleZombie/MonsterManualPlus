import enum
from abc import ABCMeta, abstractmethod
from typing import Dict, List, Sequence, Union

from mt.game import Character


class EffectType(enum.Enum):
    DYNAMIC = enum.auto()
    PLAYER_ATTACK = enum.auto()
    PLAYER_DEFENCE = enum.auto()
    PLAYER_SPELL_DEFENCE = enum.auto()
    PLAYER_SPEED = enum.auto()
    PLAYER_DAMAGE = enum.auto()
    MONSTER_ATTACK = enum.auto()
    MONSTER_DEFENCE = enum.auto()
    MONSTER_SPEED = enum.auto()
    MONSTER_DMG = enum.auto()
    SPECIAL_TURN = enum.auto()
    FROM_FIRST_TURN = enum.auto()


class Effect(metaclass=ABCMeta):

    def __init__(self, type: Union[EffectType, List[EffectType]]):
        self.type = type

    @staticmethod
    def mod_value(states: dict, value):
        if states.get('zero', False):
            return 0
        else:
            return value

    @staticmethod
    def postprocess_value(states: dict, value):
        if states.get('mult', False):
            mult = states['mult']
            return value * mult
        return value

    def on_get_player_attack(self, attack, states={}) -> int:
        return self.mod_value(states, attack)

    def on_get_player_defence(self, defence, states={}) -> int:
        return self.mod_value(states, defence)

    def on_get_player_spell_defence(self, spell_defence, states={}) -> int:
        return self.mod_value(states, spell_defence)

    def on_get_player_speed(self, speed, states={}) -> int:
        return self.mod_value(states, speed)

    def on_get_player_damage(self, damage, states: dict = {}) -> float:
        if states.get('evasion', None):
            evasion = states['evasion']
            damage = damage * evasion / 100.0
            states.popitem('evasion')
        return self.mod_value(states, damage)

    def on_get_monster_attack(self, attack, states={}) -> int:
        return self.mod_value(states, attack)

    def on_get_monster_defence(self, defence, states={}) -> int:
        return self.mod_value(states, defence)

    def on_get_monster_speed(self, speed, states={}) -> int:
        return self.mod_value(states, speed)

    def on_get_monster_damage(self, damage, states={}) -> float:
        return self.mod_value(states, damage)


class DynamicEffect(Effect):

    def __init__(self):
        super().__init__(EffectType.DYNAMIC)

    @abstractmethod
    def get_extra_param(self, player: Character, monster: Character):
        pass


def dispatch_effects(
        effects: Sequence[Effect]) -> Dict[EffectType, List[Effect]]:
    res = dict()

    for effect in effects:
        if not isinstance(effect.type, list):
            effect_type_list = [effect.type]
        else:
            effect_type_list = effect

        for type in effect_type_list:
            if type not in res:
                res[effect.type] = []
            res[effect.type].append(effect)

    return res


effect_list = {}


def register_effect(name: str):

    def decorator(effect_cls: type):
        effect_list[name] = effect_cls
        return effect_cls

    return decorator


def build_effect(name, *args, **kwargs):
    return effect_list[name](*args, **kwargs)
