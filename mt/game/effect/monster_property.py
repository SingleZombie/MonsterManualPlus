from copy import copy
from typing import Dict, List

from .effect import (Effect, EffectType, VaringEffect, register_effect,
                     require_extra_input, update_state_mult,
                     update_state_mult_mod)


@register_effect('monster_pro')
class MonsterProperty(Effect):

    def __init__(self,
                 life_mult_mod=0,
                 attack_mod=0,
                 defence_mod=0,
                 speed_mod=0,
                 attack_mult=1,
                 defence_mult=1,
                 speed_mult=1):
        type_list = []
        if life_mult_mod != 0:
            type_list.append(EffectType.MONSTER_LIFE)
        if attack_mod != 0 or attack_mult != 1:
            type_list.append(EffectType.MONSTER_ATTACK)
        if defence_mod != 0 or defence_mult != 1:
            type_list.append(EffectType.MONSTER_DEFENCE)
        if speed_mod != 0 or speed_mult != 1:
            type_list.append(EffectType.MONSTER_SPEED)
        super().__init__(type_list)
        self.life_mult_mod = life_mult_mod
        self.attack_mod = attack_mod
        self.defence_mod = defence_mod
        self.speed_mod = speed_mod
        self.attack_mult = attack_mult
        self.defence_mult = defence_mult
        self.speed_mult = speed_mult

    def mult(self, value):
        self.life_mult_mod *= value
        self.attack_mod *= value
        self.defence_mod *= value
        self.speed_mod *= value

    def on_get_monster_life(self, life, states={}) -> int:
        update_state_mult_mod(states, self.life_mult_mod / 100)
        return super().on_get_monster_life(life, states=states)

    def on_get_monster_attack(self, attack, states={}) -> int:
        attack += self.attack_mod
        update_state_mult(states, self.attack_mult / 100)
        return super().on_get_monster_attack(attack, states=states)

    def on_get_monster_defence(self, defence, states={}) -> int:
        defence += self.defence_mod
        update_state_mult(states, self.defence_mult / 100)
        return super().on_get_monster_defence(defence, states=states)

    def on_get_monster_speed(self, speed, states={}) -> int:
        speed += self.speed_mod
        update_state_mult(states, self.speed_mult)
        return super().on_get_monster_speed(speed, states=states)


@register_effect('monster_group_pro')
class MonsterGroupProperty(VaringEffect):

    def __init__(self,
                 race,
                 life_mult_mod=0,
                 attack_mod=0,
                 defence_mod=0,
                 speed_mod=0,
                 attack_mult=1,
                 defence_mult=1,
                 speed_mult=1):
        super().__init__()
        self.life_mult_mod = life_mult_mod
        self.attack_mod = attack_mod
        self.defence_mod = defence_mod
        self.speed_mod = speed_mod
        self.attack_mult = attack_mult
        self.defence_mult = defence_mult
        self.speed_mult = speed_mult

        self.race = race
        require_extra_input(f'{race.name}')

    def to_static_effects(self, extra_inputs: Dict) -> List[Effect]:
        count = extra_inputs[f'{self.race.name}']
        if count > 0:
            effect = MonsterProperty(self.life_mult_mod, self.attack_mod,
                                     self.defence_mod, self.speed_mod,
                                     self.attack_mult, self.defence_mult,
                                     self.speed_mult)
            effect.mult(count)
            return [effect]
        else:
            return []

    def to_test_static_effects(self) -> Dict[str, List[Effect]]:
        res = {}
        for cnt in range(10):
            new_effect = copy(self.effect)
            new_effect.mult(cnt)
            res[f'({cnt}):'] = [new_effect]
