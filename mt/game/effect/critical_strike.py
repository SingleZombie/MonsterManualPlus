from .effect import Effect, EffectType, register_effect, update_state_mult


@register_effect('m_dmg_mult')
class MonsterDamageMultiplier(Effect):

    def __init__(self, value):
        super().__init__(EffectType.MONSTER_DAMAGE)
        self.value = value

    def on_get_monster_damage(self, damage, states={}) -> int:
        update_state_mult(states, self.value)
        return super().on_get_monster_damage(damage, states)


@register_effect('crt_stk')
class CriticalStrike(Effect):

    def __init__(self, cs_chance: int, cs_mult: int):
        super().__init__(EffectType.SPECIAL_TURN)
        self.turn = 1
        self.effects = [[MonsterDamageMultiplier(cs_mult / 100)],
                        [
                            MonsterDamageMultiplier((cs_mult / 100 - 1) *
                                                    (cs_chance / 100) + 1)
                        ]]
