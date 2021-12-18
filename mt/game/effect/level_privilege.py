from mt.game import Monster, Player

from .effect import DynamicEffect, EffectType, register_effect


@register_effect('level_pr')
class LevelPrevilege(DynamicEffect):

    def __init__(self, value: int):
        super().__init__()
        self.value = value

    def get_extra_param(self, player: Player, monster: Monster):
        self.mult = ((100 - self.value) / 100)**max(
            0, monster.level - player.level)
        self.type = [EffectType.PLAYER_ATTACK, EffectType.PLAYER_DEFENCE]

    def on_get_player_attack(self, attack, states={}) -> int:
        mult = states.get('mult', 1)
        mult *= self.mult
        states['mult'] = mult
        return super().on_get_player_attack(attack, states=states)

    def on_get_player_defence(self, attack, states={}) -> int:
        mult = states.get('mult', 1)
        mult *= self.mult
        states['mult'] = mult
        return super().on_get_player_defence(attack, states=states)
