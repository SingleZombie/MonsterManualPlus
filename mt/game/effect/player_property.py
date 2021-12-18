from .effect import Effect, EffectType, register_effect, update_state_mult


@register_effect('player_pro')
class PlayerProperty(Effect):

    def __init__(self,
                 attack_mod=0,
                 defence_mod=0,
                 speed_mod=0,
                 attack_mult=1,
                 defence_mult=1,
                 speed_mult=1):
        type_list = []
        if attack_mod != 0 or attack_mult != 1:
            type_list.append(EffectType.PLAYER_ATTACK)
        if defence_mod != 0 or defence_mult != 1:
            type_list.append(EffectType.PLAYER_DEFENCE)
        if speed_mod != 0 or speed_mult != 1:
            type_list.append(EffectType.PLAYER_SPEED)
        super().__init__(type_list)
        self.attack_mod = attack_mod
        self.defence_mod = defence_mod
        self.speed_mod = speed_mod
        self.attack_mult = attack_mult
        self.defence_mult = defence_mult
        self.speed_mult = speed_mult

    def mult(self, value):
        self.attack_mod *= value
        self.defence_mod *= value
        self.speed_mod *= value

    def on_get_player_attack(self, attack, states={}) -> int:
        attack += self.attack_mod
        update_state_mult(states, self.attack_mult)
        return super().on_get_player_attack(attack, states=states)

    def on_get_player_defence(self, defence, states={}) -> int:
        defence += self.defence_mod
        update_state_mult(states, self.defence_mult)
        return super().on_get_player_defence(defence, states=states)

    def on_get_player_speed(self, speed, states={}) -> int:
        speed += self.speed_mod
        update_state_mult(states, self.speed_mult)
        return super().on_get_player_speed(speed, states=states)
