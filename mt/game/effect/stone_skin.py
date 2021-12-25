from .effect import (Effect, EffectType, register_effect, update_state_mult,
                     update_state_post_mod)


@register_effect('stone_skin')
class StoneSkin(Effect):

    def __init__(self, mult: int, mod: int):
        super().__init__(EffectType.PLAYER_PHYSICAL_DAMAGE)
        self.mult = mult
        self.mod = mod

    def on_get_player_physical_damage(self, damage, states={}) -> float:
        update_state_mult(states, 1 - self.mult / 100)
        update_state_post_mod(states, -self.mod)
        return super().on_get_monster_physical_damage(damage, states=states)
