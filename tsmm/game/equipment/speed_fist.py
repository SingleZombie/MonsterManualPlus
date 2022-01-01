from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('speed_fist')
class SpeedFist(Equipment):

    def __init__(self):
        super().__init__([build_effect('player_pro', speed_mod=50)])
