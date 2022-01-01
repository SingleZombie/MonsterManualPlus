from ..effect import Effect, EffectType, register_effect


@register_effect('sim_magical')
class Magical(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_DAMAGE)
        self.value = value

    def on_get_monster_damage(self, damage, states={}):
        return super().on_get_monster_damage(damage + self.value, states)
