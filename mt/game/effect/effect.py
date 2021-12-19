import enum
from abc import ABCMeta, abstractmethod
from typing import Dict, List, Sequence, Union

from mt.game import Character


class EffectType(enum.Enum):
    DYNAMIC = enum.auto()
    VARING = enum.auto()
    PLAYER_ATTACK = enum.auto()
    PLAYER_DEFENCE = enum.auto()
    PLAYER_SPELL_DEFENCE = enum.auto()
    PLAYER_SPEED = enum.auto()
    PLAYER_DAMAGE = enum.auto()
    PLAYER_REGENERATE = enum.auto()
    MONSTER_LIFE = enum.auto()
    MONSTER_ATTACK = enum.auto()
    MONSTER_DEFENCE = enum.auto()
    MONSTER_SPEED = enum.auto()
    MONSTER_PHYSICAL_DMG = enum.auto()
    MONSTER_DMG = enum.auto()
    SPECIAL_TURN = enum.auto()
    FROM_FIRST_TURN = enum.auto()


def update_state_mult(state: Dict[str, float], multiplier: float):
    v = state.get('mult', 1)
    v *= multiplier
    state['mult'] = v


def update_state_mult_mod(state: Dict[str, float], multiplier: float):
    v = state.get('mult_mod', 0)
    v += multiplier
    state['mult_mod'] = v


class Effect():

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
        mult = states.get('mult', 1)
        mult_mod = states.get('mult_mod', 0)
        mult += mult_mod
        return value * mult

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
            states.pop('evasion')
        return self.mod_value(states, damage)

    def on_get_player_regenerate(self, regenerate, states: dict = {}) -> float:
        return self.mod_value(states, regenerate)

    def on_get_monster_life(self, life, states={}) -> int:
        return self.mod_value(states, life)

    def on_get_monster_attack(self, attack, states={}) -> int:
        return self.mod_value(states, attack)

    def on_get_monster_defence(self, defence, states={}) -> int:
        return self.mod_value(states, defence)

    def on_get_monster_speed(self, speed, states={}) -> int:
        return self.mod_value(states, speed)

    def on_get_monster_physical_damage(self,
                                       physical_damage,
                                       states={}) -> float:
        return self.mod_value(states, physical_damage)

    def on_get_monster_damage(self, damage, states={}) -> float:
        return self.mod_value(states, damage)


class DynamicEffect(Effect, metaclass=ABCMeta):

    def __init__(self):
        super().__init__(EffectType.DYNAMIC)

    @abstractmethod
    def to_static_effects(self, player: Character,
                          monster: Character) -> List[Effect]:
        pass


class DynamicEffectWithTest(DynamicEffect):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def to_test_static_effects(self) -> Dict[str, List[Effect]]:
        pass


class VaringEffect(Effect, metaclass=ABCMeta):

    def __init__(self):
        super().__init__(EffectType.VARING)

    @abstractmethod
    def to_static_effects(self, extra_inputs: Dict) -> List[Effect]:
        pass

    @abstractmethod
    def to_test_static_effects(self) -> Dict[str, List[Effect]]:
        pass


class RaceEffect(DynamicEffect):

    def __init__(self, effects: List[Effect], race):
        super().__init__()
        self.effects = effects
        self.race = race

    def to_static_effects(self, player: Character,
                          monster: Character) -> List[Effect]:
        if monster.race == self.race:
            return self.effects
        else:
            return []


def dispatch_effects(effects: Sequence[Effect],
                     output=None) -> Dict[EffectType, List[Effect]]:
    if output is None:
        res = dict()
    else:
        res = output

    for effect in effects:
        if not isinstance(effect.type, list):
            effect_type_list = [effect.type]
        else:
            effect_type_list = effect.type

        for type in effect_type_list:
            if type not in res:
                res[type] = []
            res[type].append(effect)

    return res


effect_list = {}


def register_effect(name: str):

    def decorator(effect_cls: type):
        effect_list[name] = effect_cls
        return effect_cls

    return decorator


def build_effect(name, *args, **kwargs):
    return effect_list[name](*args, **kwargs)


extra_inputs = set()


def require_extra_input(name: str):
    extra_inputs.add(name)
