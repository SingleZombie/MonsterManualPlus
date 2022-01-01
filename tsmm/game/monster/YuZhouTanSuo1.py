from typing import Callable, Dict

from ..effect import build_effect
from .monster import Monster, register_monster_set

__monster_dict: Dict[str, Callable] = dict(
    slime=lambda: Monster(
        life=40, attack=18, defence=1, gold=1, experience=1, effects=[]),
    red_slime=lambda: Monster(
        life=50, attack=22, defence=2, gold=2, experience=1, effects=[]),
    skeleton=lambda: Monster(
        life=60, attack=26, defence=1, gold=4, experience=1, effects=[]),
    bat=lambda: Monster(
        life=35,
        attack=30,
        defence=2,
        gold=3,
        experience=1,
        effects=[build_effect('first_strike')]),
    giant_slime=lambda: Monster(
        life=70, attack=32, defence=3, gold=7, experience=2, effects=[]),
    mage=lambda: Monster(
        life=50,
        attack=0,
        defence=8,
        gold=5,
        experience=2,
        effects=[build_effect('sim_magical', 10)]),
    giant_bat=lambda: Monster(
        life=80,
        attack=40,
        defence=4,
        gold=10,
        experience=3,
        effects=[build_effect('mult_strike', 2)]),
    guard_a=lambda: Monster(
        life=30, attack=25, defence=15, gold=8, experience=3),
    skeleton_soldier=lambda: Monster(
        life=100, attack=45, defence=9, gold=12, experience=4),
    ghost=lambda: Monster(
        life=40, attack=300, defence=0, gold=12, experience=4),
    slime_king=lambda: Monster(
        life=100, attack=82, defence=8, gold=10, experience=5),
    superior_mage=lambda: Monster(
        life=240,
        attack=0,
        defence=20,
        gold=15,
        experience=5,
        effects=[build_effect('sim_magical', 20)]),
    rock=lambda: Monster(
        life=300, attack=80, defence=5, gold=22, experience=5),
    red_bat=lambda: Monster(
        life=100,
        attack=85,
        defence=10,
        gold=18,
        experience=5,
        effects=[build_effect('mult_strike', 3)]),
    knight=lambda: Monster(
        life=75,
        attack=75,
        defence=30,
        gold=17,
        experience=5,
        effects=[build_effect('mult_strike', 2)]),
    guard_b=lambda: Monster(
        life=200, attack=60, defence=40, gold=20, experience=5),
    zombie=lambda: Monster(
        life=160,
        attack=60,
        defence=12,
        gold=14,
        experience=4,
        effects=[build_effect('first_strike')]),
    skeleton_captain=lambda: Monster(
        life=490, attack=158, defence=36, gold=33, experience=8),
    knight_b=lambda: Monster(
        life=150,
        attack=120,
        defence=40,
        gold=26,
        experience=6,
        effects=[build_effect('mult_strike', 3)]),
    shadow_mage=lambda: Monster(
        life=300,
        attack=0,
        defence=50,
        gold=35,
        experience=6,
        effects=[build_effect('sim_magical', 80)]),
    shadow_knight=lambda: Monster(
        life=200,
        attack=160,
        defence=35,
        gold=30,
        experience=6,
        effects=[build_effect('mult_strike', 3)]),
    dark_captain=lambda: Monster(
        life=350,
        attack=210,
        defence=50,
        gold=50,
        experience=8,
        effects=[build_effect('first_strike')]),
    dark_soldier=lambda: Monster(
        life=310,
        attack=195,
        defence=55,
        gold=45,
        experience=8,
        effects=[build_effect('first_strike')]),
    necrolord=lambda: Monster(
        life=655, attack=265, defence=40, gold=50, experience=10),
    soullord=lambda: Monster(
        life=1000, attack=400, defence=80, gold=100, experience=10),
    guard_c=lambda: Monster(
        life=300, attack=150, defence=75, gold=40, experience=8),
)

register_monster_set('YuZhouTanSuo1', __monster_dict)
