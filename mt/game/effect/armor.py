from .effect import Effect, EffectType, register_effect, update_state_mult_mod


@register_effect('armor')
class Armor(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_PHYSICAL_DMG)
        self.value = value

    def on_get_monster_physical_damage(self, damage, states={}) -> float:
        armor = states.get('armor', 0)
        armor += self.value
        states['armor'] = armor
        return super().on_get_monster_physical_damage(damage, states=states)
