from .effect import Effect, EffectType, register_effect


@register_effect('spl_atk')
class SpellAttack(Effect):

    def __init__(self, value: int):
        super().__init__(EffectType.PLAYER_SPELL_DEFENCE)
        self.value = value

    def on_get_player_spell_defence(self, spell_defence, states={}) -> int:
        return super().on_get_player_spell_defence(spell_defence - self.value,
                                                   states)


@register_effect('stop_phy_dmg')
class StopPhysicalDamage(Effect):

    def __init__(self):
        super().__init__(EffectType.MONSTER_PHYSICAL_DAMAGE)

    def on_get_monster_physical_damage(self, damage, states={}) -> int:
        states['zero'] = True
        return super().on_get_monster_physical_damage(damage, states)


@register_effect('spl')
class Spell(Effect):

    def __init__(self, turn: int, value: int):
        super().__init__(EffectType.SPECIAL_TURN)
        self.turn = turn
        self.effects = [[SpellAttack(value), StopPhysicalDamage()], []]
