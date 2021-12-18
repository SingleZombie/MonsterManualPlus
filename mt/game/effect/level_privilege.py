from typing import List

from .effect import DynamicEffect, Effect, register_effect
from .player_property import PlayerProperty


@register_effect('level_pr')
class LevelPrevilege(DynamicEffect):

    def __init__(self, value: int):
        super().__init__()
        self.value = value

    def to_static_effects(self, player, monster) -> List[Effect]:
        if monster.level > player.level:
            mult = ((100 - self.value) / 100) * (monster.level - player.level)
            return [PlayerProperty(attack_mult=mult, defence_mult=mult)]
        else:
            return []
