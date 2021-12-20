from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('buckler')
class Buckler(Equipment):

    def __init__(self):
        super().__init__([
            build_effect('player_pro', defence_mod=2),
            build_effect('armor', 2)
        ])
