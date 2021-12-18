from .effect import Effect, EffectType, register_effect


class SpellAttack(Effect):

    def __init__(self, value: int):
        super().__init__(
            [EffectType.PLAYER_SPELL_DEFENCE, EffectType.MONSTER_ATTACK])
        self.value = value

    def on_get_player_spell_defence(self, spell_defence, states={}) -> int:
        return super().on_get_player_spell_defence(spell_defence - self.value,
                                                   states)

    def on_get_monster_attack(self, attack, states={}) -> int:
        states['zero'] = True
        return super().on_get_monster_attack(attack, states)


@register_effect('spl')
class Spell(Effect):

    def __init__(self, turn: int, value: int):
        super().__init__(EffectType.SPECIAL_TURN)
        self.turn = turn
        self.effects = [SpellAttack(value)]
