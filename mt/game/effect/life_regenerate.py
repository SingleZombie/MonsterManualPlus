from .effect import Effect, EffectType, register_effect


@register_effect('life_reg')
class LifeRegenerate(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.PLAYER_REGENERATE)
        self.value = value

    def on_get_player_regenerate(self, regenerate, states={}) -> float:
        regenerate += self.value
        return super().on_get_player_regenerate(regenerate, states=states)
