from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('t_o_s')
class TearOfSouls(Equipment):

    def __init__(self):
        super().__init__([build_effect('spl_atk', value=-30)])
