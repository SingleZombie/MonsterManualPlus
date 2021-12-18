from typing import List

from .character import Character
from .effect import Effect
from .equipment import Equipment


class Player(Character):

    def __init__(self, life, attack, defence, speed, effects,
                 equipment_set_list: List[List[Equipment]], level, life_max):
        super().__init__(life, attack, defence, speed, effects, level)
        self.equipment_set_list = equipment_set_list
        self.life_max = life_max

    def get_equipment_comb(self) -> List[List[Effect]]:
        res = []
        for equipment_set in self.equipment_set_list:
            effects = []
            for equipment in equipment_set:
                effects.extend(equipment.effects)
            res.append(effects)
        return res
