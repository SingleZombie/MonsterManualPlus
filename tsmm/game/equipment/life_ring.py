from ..effect import build_effect
from .equipment import Equipment, register_equipment


@register_equipment('life_ring')
class LifeRing(Equipment):

    def __init__(self):
        super().__init__([build_effect('life_reg', 4)])
