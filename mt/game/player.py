from typing import List
from .character import Character
from .weapon import weapon
from .effect import Effect


class Player(Character):

    def __init__(self, life, attack, defence, speed, effects, equipment_list,
                 level, life_max):
        super().__init__(life, attack, defence, speed, effects, level)
        self.equipment_list = equipment_list
        self.life_max = life_max

    def get_equipment_comb(self) -> List[List[Effect]]:
        return [[]]
