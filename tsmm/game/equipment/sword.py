from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('sword')
class Sword(Equipment):

    def __init__(self):
        super().__init__([build_effect('player_pro', attack_mod=2)])
