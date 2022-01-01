from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('cloth')
class Cloth(Equipment):

    def __init__(self):
        super().__init__([build_effect('player_pro', defence_mod=1)])
