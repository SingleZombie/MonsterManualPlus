import enum

from mt.game.effect.effect import DynamicEffectWithTest

from .character import Character
from .effect import VaringEffect


class MonsterRace(enum.Enum):
    NORMAL = enum.auto()
    SKELETON = enum.auto()


class Monster(Character):

    def __init__(self,
                 life,
                 attack,
                 defence,
                 speed,
                 effects,
                 gold,
                 experience,
                 level=1,
                 race: MonsterRace = MonsterRace.NORMAL):
        super().__init__(life, attack, defence, speed, effects, level)
        self.race = race
        self._gold = gold
        self._experience = experience

        self._test_effects = []
        for effect in self._effects:
            if isinstance(effect, (VaringEffect, DynamicEffectWithTest)):
                self._test_effects.append(effect)

    @property
    def has_test(self):
        return len(self._test_effects) > 0

    @property
    def test_effects(self):
        return self._test_effects
