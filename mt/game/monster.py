import enum

from .character import Character


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
