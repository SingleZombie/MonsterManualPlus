from .character import Character


class Monster(Character):

    def __init__(self,
                 life,
                 attack,
                 defence,
                 speed,
                 effects,
                 gold,
                 experience,
                 level=1):
        super().__init__(life, attack, defence, speed, effects, level)
        self._gold = gold
        self._experience = experience
