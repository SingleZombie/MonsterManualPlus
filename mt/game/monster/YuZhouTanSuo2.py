from typing import Callable, Dict

from ..effect import build_effect
from .monster import Monster, register_monster_set

__monster_dict: Dict[str, Callable] = dict(
    slime=lambda: Monster(life=20, attack=2, defence=0, gold=1, effects=[]),
    red_slime=lambda: Monster(
        life=25, attack=3, defence=0, gold=1, effects=[]),
    skeleton=lambda: Monster(life=40, attack=7, defence=2, gold=1, effects=[]),
    bat=lambda: Monster(
        life=20,
        attack=6,
        defence=0,
        gold=1,
        effects=[build_effect('first_strike')]),
    giant_slime=lambda: Monster(
        life=30, attack=12, defence=2, gold=2, effects=[]),
    mage=lambda: Monster(
        life=50,
        attack=0,
        defence=1,
        gold=2,
        effects=[build_effect('sim_magical', 10)]),
    guard_a=lambda: Monster(life=40, attack=24, defence=12, gold=2),
    swordman_a=lambda: Monster(
        life=50,
        attack=48,
        defence=8,
        gold=3,
        effects=[build_effect('mult_strike', 2)]),
    skeleton_soldier=lambda: Monster(life=70, attack=20, defence=5, gold=2),
    ghost=lambda: Monster(life=60, attack=16, defence=2, gold=2),
    white_bat=lambda: Monster(
        life=35,
        attack=65,
        defence=8,
        gold=3,
        effects=[build_effect('first_strike')]),
    black_bat=lambda: Monster(
        life=45,
        attack=64,
        defence=10,
        gold=4,
        effects=[build_effect('first_strike')]),
    slime_king=lambda: Monster(life=300, attack=120, defence=15, gold=10),
    red_bird=lambda: Monster(
        life=120,
        attack=68,
        defence=6,
        gold=5,
        effects=[build_effect('first_strike')]),
    skeleton_warrior=lambda: Monster(life=180, attack=82, defence=10, gold=5),
    blue_bird=lambda: Monster(life=210, attack=58, defence=18, gold=5),
    zombie=lambda: Monster(
        life=80,
        attack=75,
        defence=20,
        gold=5,
        effects=[build_effect('mult_strike', 2)]),
    skeleton_general=lambda: Monster(
        life=240,
        attack=105,
        defence=10,
        gold=7,
        effects=[build_effect('first_strike')]),
    swordman_b=lambda: Monster(
        life=130,
        attack=126,
        defence=18,
        gold=6,
        effects=[build_effect('mult_strike', 2)]),
    yellow_bird=lambda: Monster(
        life=200,
        attack=0,
        defence=30,
        gold=7,
        effects=[build_effect('sim_magical', 60)]),
    giant_bat=lambda: Monster(
        life=200,
        attack=188,
        defence=16,
        gold=8,
        effects=[build_effect('first_strike')]),
    rock=lambda: Monster(life=100, attack=180, defence=68, gold=7),
    intermediate_mage=lambda: Monster(
        life=400,
        attack=0,
        defence=20,
        gold=9,
        effects=[build_effect('sim_magical', 80)]),
    purple_bird=lambda: Monster(
        life=110,
        attack=144,
        defence=36,
        gold=9,
        effects=[build_effect('mult_strike', 2)]),
)

register_monster_set('YuZhouTanSuo2', __monster_dict)
