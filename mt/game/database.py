from typing import Dict, List, Tuple

from .effect import build_effect
from .monster import Monster, MonsterRace

__monster_dict: Dict[str, Dict] = dict(
    slime=lambda: Monster(
        life=32,
        attack=3,
        defence=0,
        speed=80,
        gold=1,
        experience=1,
        effects=[]),
    will_o_the_wisp=lambda: Monster(
        life=25,
        attack=6,
        defence=0,
        speed=70,
        effects=[build_effect('frost', 40)],
        gold=1,
        experience=2),
    ooze=lambda: Monster(
        life=80,
        attack=2,
        defence=0,
        speed=50,
        effects=[build_effect('toxin', 1)],
        gold=1,
        experience=2),
    slime_warrior=lambda: Monster(
        life=42,
        attack=5,
        defence=1,
        speed=90,
        effects=[],
        gold=1,
        experience=2),
    red_slime=lambda: Monster(
        life=58,
        attack=7,
        defence=1,
        speed=80,
        effects=[],
        gold=1,
        experience=3),
    red_slime_warrior=lambda: Monster(
        life=80,
        attack=11,
        defence=3,
        speed=90,
        effects=[],
        gold=2,
        experience=4),
    dead=lambda: Monster(
        life=45,
        attack=15,
        defence=0,
        speed=100,
        gold=1,
        experience=3,
        level=1,
        effects=[
            build_effect(
                'monster_group_pro', MonsterRace.SKELETON, life_mult_mod=10)
        ],
        race=MonsterRace.SKELETON),
    blood_dead=lambda: Monster(
        life=75,
        attack=18,
        defence=1,
        speed=100,
        gold=3,
        experience=5,
        level=2,
        effects=[
            build_effect(
                'monster_group_pro', MonsterRace.SKELETON, life_mult_mod=15),
            build_effect(
                'blood_hunter',
                monster_property=build_effect('monster_pro', speed_mod=2))
        ],
        race=MonsterRace.SKELETON),
    ice_ooze=lambda: Monster(
        life=300,
        attack=2,
        defence=0,
        speed=30,
        gold=2,
        experience=4,
        level=2,
        effects=[build_effect('frost', 60),
                 build_effect('toxin', 2)]),
    rogue_mage=lambda: Monster(
        life=96,
        attack=12,
        defence=4,
        speed=100,
        gold=3,
        experience=6,
        level=2,
        effects=[build_effect('spl', 3, 30)]),
    slime_man=lambda: Monster(
        life=122,
        attack=11,
        defence=2,
        speed=185,
        gold=3,
        experience=6,
        level=2,
        effects=[build_effect('evasion', 50)]),
    slime_noble=lambda: Monster(
        life=101,
        attack=13,
        defence=3,
        speed=75,
        gold=3,
        experience=5,
        level=3,
        effects=[build_effect('level_pr', 25)]),
    toxic_dead=lambda: Monster(
        life=115,
        attack=27,
        defence=5,
        speed=100,
        gold=4,
        experience=8,
        level=3,
        effects=[
            build_effect(
                'monster_group_pro', MonsterRace.SKELETON, life_mult_mod=20),
            build_effect('toxin', 3)
        ],
        race=MonsterRace.SKELETON),
    black_slime=lambda: Monster(
        life=157,
        attack=19,
        defence=8,
        speed=80,
        gold=4,
        experience=7,
        level=3,
        effects=[]),
    swordman=lambda: Monster(
        life=135,
        attack=22,
        defence=6,
        speed=240,
        gold=4,
        experience=8,
        level=3,
        effects=[]),
    bowman=lambda: Monster(
        life=160,
        attack=28,
        defence=8,
        speed=120,
        gold=5,
        experience=12,
        level=4,
        effects=[]),
    bird=lambda: Monster(
        life=184,
        attack=23,
        defence=5,
        speed=130,
        gold=4,
        experience=8,
        level=3,
        effects=[build_effect('evasion', 25)]),
    goblin=lambda: Monster(
        life=245,
        attack=26,
        defence=12,
        speed=110,
        gold=5,
        experience=13,
        level=4,
        effects=[]),
    red_slime_noble=lambda: Monster(
        life=178,
        attack=20,
        defence=11,
        speed=75,
        gold=4,
        experience=8,
        level=4,
        effects=[build_effect('level_pr', 25)]),
    bat=lambda: Monster(
        life=138,
        attack=35,
        defence=8,
        speed=140,
        gold=6,
        experience=14,
        level=4,
        effects=[build_effect('evasion', 35)]),
    black_slime_warrior=lambda: Monster(
        life=288,
        attack=28,
        defence=15,
        speed=90,
        gold=6,
        experience=15,
        level=4,
        effects=[]),
    demon_seed=lambda: Monster(
        life=275,
        attack=29,
        defence=17,
        speed=80,
        gold=6,
        experience=16,
        level=4,
        effects=[
            build_effect(
                'blood_hunter',
                monster_property=build_effect('monster_pro', speed_mod=3))
        ]),
    metero_rogue_mage=lambda: Monster(
        life=310,
        attack=33,
        defence=14,
        speed=100,
        gold=7,
        experience=18,
        level=4,
        effects=[build_effect('spl', 7, 60)]),
    tomb_watcher=lambda: Monster(
        life=187,
        attack=40,
        defence=20,
        speed=110,
        gold=7,
        experience=19,
        level=4,
        effects=[
            build_effect(
                'monster_group_pro', MonsterRace.SKELETON, life_mult_mod=20)
        ],
        race=MonsterRace.SKELETON),
    fire_of_soul=lambda: Monster(
        life=107,
        attack=45,
        defence=15,
        speed=82,
        gold=7,
        experience=17,
        level=4,
        effects=[build_effect('frost', 160)]),
    tomb_general=lambda: Monster(
        life=270,
        attack=50,
        defence=25,
        speed=135,
        gold=9,
        experience=25,
        level=5,
        effects=[
            build_effect(
                'monster_group_pro', MonsterRace.SKELETON, life_mult_mod=100),
            build_effect('level_pr', 20)
        ],
        race=MonsterRace.SKELETON),
    tomb_swordman=lambda: Monster(
        life=210,
        attack=52,
        defence=16,
        speed=240,
        gold=8,
        experience=22,
        level=5,
        effects=[
            build_effect(
                'monster_group_pro', MonsterRace.SKELETON, life_mult_mod=10),
            build_effect('crt_stk', 20, 250)
        ],
        race=MonsterRace.SKELETON),
    big_bat=lambda: Monster(
        life=232,
        attack=40,
        defence=23,
        speed=160,
        gold=8,
        experience=20,
        level=5,
        effects=[
            build_effect('evasion', 30),
        ]),
    nightmare_soldier=lambda: Monster(
        life=268,
        attack=45,
        defence=27,
        speed=150,
        gold=9,
        experience=24,
        level=5,
        effects=[]),
    nightmare_mage=lambda: Monster(
        life=373,
        attack=42,
        defence=24,
        speed=100,
        gold=9,
        experience=26,
        level=5,
        effects=[build_effect('spl', 3, 120)]),
    nightmare_shieldman=lambda: Monster(
        life=550,
        attack=40,
        defence=28,
        speed=90,
        gold=10,
        experience=28,
        level=5,
        effects=[build_effect('stone_skin', 25, 3)]),
)

__monster_instances = []
__monster_names = []


def build_monsters(monster_name_list: List[str]) -> List[Monster]:
    global __monster_names
    __monster_names = monster_name_list

    for name in monster_name_list:
        __monster_instances.append(__monster_dict[name]())
    return __monster_instances


def get_monsters() -> Tuple[List[str], List[Monster]]:
    return __monster_names, __monster_instances
