from .effect import Effect, EffectType, register_effect


@register_effect('evasion')
class Evasion(Effect):
    def __init__(self, value: int):
        super().__init__(EffectType.PLAYER_DAMAGE)
        self.value = value

    def on_get_player_damage(self, damage, states: dict = {}) -> float:
        states['evasion'] = self.value
        return super().on_get_player_damage(damage, states=states)
