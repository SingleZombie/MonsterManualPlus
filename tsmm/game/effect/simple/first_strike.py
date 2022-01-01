from ..effect import Effect, EffectType, register_effect


@register_effect('first_strike')
class FirstStrike(Effect):

    def __init__(self):
        super().__init__(EffectType.FIRST_STRIKE)
