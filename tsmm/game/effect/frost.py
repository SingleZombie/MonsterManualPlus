from .effect import Effect, EffectType, register_effect


@register_effect('spd_down')
class DecreaseSpeed(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.PLAYER_SPEED)
        self.value = value

    def on_get_player_speed(self, speed, states={}):
        return super().on_get_player_speed(speed - self.value, states)


@register_effect('frost')
class Frost(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.FROM_FIRST_TURN)
        self.effects = [DecreaseSpeed(value)]
