from .effect import EffectType, Effect, register_effect


class Toxin(Effect):
    def __init__(self, value: int):
        super().__init__(EffectType.MONSTER_DMG)

    def on_get_monster_damage(self, damage, states={}):
        return super().on_get_monster_damage(damage + self.value, states)
