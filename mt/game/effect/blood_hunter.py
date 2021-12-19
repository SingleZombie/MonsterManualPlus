from copy import copy
from typing import Dict, List

from .effect import DynamicEffectWithTest, Effect, register_effect
from .monster_property import MonsterProperty
from .player_property import PlayerProperty


@register_effect('blood_hunter')
class BloodHunter(DynamicEffectWithTest):

    def __init__(self,
                 monster_property: MonsterProperty = None,
                 player_property: PlayerProperty = None):
        super().__init__()
        self.effects = []
        if monster_property:
            self.effects.append(monster_property)
        if player_property:
            self.effects.append(player_property)

    def to_static_effects(self, player, monster) -> List[Effect]:
        if player.life < player.life_max:
            multiplier = (player.life_max -
                          player.life) / player.life_max * 100
            res = []
            for effect in self.effects:
                new_effect = copy(effect)
                new_effect.mult(multiplier)
                res.append(new_effect)
            return res
        else:
            return []

    def to_test_static_effects(self) -> Dict[str, List[Effect]]:
        res = {}
        for i in range(10):
            percentage = (i + 1) * 10
            new_list = [copy(x).mult(percentage) for x in self.effects]
            res[f'{percentage}%:'] = new_list
