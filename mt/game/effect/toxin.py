from .effect import Effect, EffectType, register_effect


@register_effect('toxin')
class Toxin(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_PHYSICAL_DMG)
        self.value = value

    def on_get_monster_physical_damage(self, damage, states={}):
        return super().on_get_monster_physical_damage(damage + self.value,
                                                      states)
