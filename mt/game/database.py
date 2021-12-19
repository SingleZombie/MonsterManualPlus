from typing import Dict

from .effect import build_effect
from .monster import Monster, MonsterRace

monster_dict: Dict[str, Monster] = dict(
    slime=Monster(
        life=32,
        attack=3,
        defence=0,
        speed=80,
        gold=1,
        experience=1,
        effects=[]),
    will_o_the_wisp=Monster(25, 6, 0, 70, [build_effect('frost', 40)], 1, 2),
    ooze=Monster(80, 2, 0, 50, [build_effect('toxin', 1)], 0, 0),
    slime_warrior=Monster(42, 5, 1, 90, [], 1, 2),
    red_slime=Monster(58, 7, 1, 80, [], 1, 3),
    red_slime_warrior=Monster(80, 11, 3, 90, [], 2, 4),
    # dead=Monster(
    #     life=45,
    #     attack=15,
    #     defence=0,
    #     speed=100,
    #     gold=1,
    #     experience=3,
    #     level=1,
    #     effects=[build_effect('monster_group_pro', MonsterRace.SKELETON)]),
    ice_ooze=Monster(
        life=300,
        attack=2,
        defence=0,
        speed=30,
        gold=2,
        experience=4,
        level=2,
        effects=[build_effect('frost', 60),
                 build_effect('toxin', 2)]),
    rogue_mage=Monster(
        life=96,
        attack=12,
        defence=4,
        speed=100,
        gold=3,
        experience=6,
        level=2,
        effects=[build_effect('spl', 3, 30)]),
    slime_man=Monster(
        life=122,
        attack=11,
        defence=2,
        speed=185,
        gold=3,
        experience=6,
        level=2,
        effects=[build_effect('evasion', 50)]),
    slime_noble=Monster(
        life=101,
        attack=13,
        defence=3,
        speed=75,
        gold=3,
        experience=5,
        level=3,
        effects=[build_effect('level_pr', 25)]),
)

# big_bat=Monster(268, 45, 27, 150, [], 9, 24))

# display_monster = [
#     'slime', 'will_o_the_wisp', 'ooze', 'slime_warrior', 'red_slime',
#     'red_slime_warrior', 'ice_ooze', 'rogue_mage', 'slime_man', 'slime_noble'
# ]

display_monster = ['ice_ooze']
