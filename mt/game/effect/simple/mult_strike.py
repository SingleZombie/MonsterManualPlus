from ..effect import Effect, EffectType, register_effect, update_state_mult


@register_effect('mult_strike')
class MultipleStrike(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_DAMAGE)
        self.value = value

    def on_get_monster_damage(self, damage, states={}):
        update_state_mult(states, self.value)
        return super().on_get_monster_damage(damage, states)
