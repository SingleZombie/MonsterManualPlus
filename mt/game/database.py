from typing import Dict

from .effect import build_effect
from .monster import Monster

monster_dict: Dict[str, Monster] = dict(
    slime=Monster(32, 3, 0, 80, [], 1, 1),
    will_o_the_wisp=Monster(25, 6, 0, 70, [build_effect('frost', 40)], 1, 2),
    ooze=Monster(80, 2, 0, 50, [], 0, 0),
    slime_warrior=Monster(42, 5, 1, 90, [], 1, 2),
    red_slime=Monster(58, 7, 1, 80, [], 1, 3),
    red_slime_warrior=Monster(80, 11, 3, 90, [], 2, 4),
    slime_man=Monster(
        122,
        11,
        2,
        185,
    ),
    big_bat=Monster(268, 45, 27, 150, [], 9, 24))
