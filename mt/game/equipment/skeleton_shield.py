from mt.game import MonsterRace

from ..effect import PlayerProperty, RaceEffect, build_effect
from .equipment import Equipment, register_equipment


class SkeletonResistance(RaceEffect):

    def __init__(self, value: int):
        super().__init__([PlayerProperty(defence_mod=value)],
                         MonsterRace.SKELETON)


@register_equipment('skeleton_shield')
class SkeletonShield(Equipment):

    def __init__(self):
        super().__init__([build_effect('armor', 1), SkeletonResistance(5)])
