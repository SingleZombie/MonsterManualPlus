from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('knight_bracer')
class KnightBracer(Equipment):

    def __init__(self):
        super().__init__([
            build_effect('player_pro', speed_mod=15),
            build_effect('life_reg', 1)
        ])
