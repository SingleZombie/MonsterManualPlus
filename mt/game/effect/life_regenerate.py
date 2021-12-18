from .effect import Effect, EffectType, register_effect


@register_effect('life_reg')
class LifeRegenerate(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_DMG)
        self.value = value

    def on_get_monster_damage(self, damage, states={}) -> float:
        damage -= self.value
        return super().on_get_monster_damage(damage, states=states)
