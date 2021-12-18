from .effect import Effect, EffectType, register_effect, update_state_mult


@register_effect('armor')
class Armor(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_PHYSICAL_DMG)
        self.mult = 1 / (1 + 0.06 * value)

    def on_get_monster_physical_damage(self, damage, states={}) -> float:
        update_state_mult(states, self.mult)
        return super().on_get_monster_physical_damage(damage, states=states)
