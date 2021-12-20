from typing import Dict, List

from .monster import Monster, MonsterRace


def build_effect(name: str, *arg, **kwargs):
    return (name, arg, kwargs)


__monster_dict: Dict[str, Dict] = dict(
    slime=dict(
        life=32,
        attack=3,
        defence=0,
        speed=80,
        gold=1,
        experience=1,
        effects=[]),
    will_o_the_wisp=dict(
        life=25,
        attack=6,
        defence=0,
        speed=70,
        effects=[build_effect('frost', 40)],
        gold=1,
        experience=2),
    ooze=dict(
        life=80,
        attack=2,
        defence=0,
        speed=50,
        effects=[build_effect('toxin', 1)],
        gold=1,
        experience=2),
    slime_warrior=dict(
        life=42,
        attack=5,
        defence=1,
        speed=90,
        effects=[],
        gold=1,
        experience=2),
    red_slime=dict(
        life=58,
        attack=7,
        defence=1,
        speed=80,
        effects=[],
        gold=1,
        experience=3),
    red_slime_warrior=dict(
        life=80,
        attack=11,
        defence=3,
        speed=90,
        effects=[],
        gold=2,
        experience=4),
    dead=dict(
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
    blood_dead=dict(
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
    ice_ooze=dict(
        life=300,
        attack=2,
        defence=0,
        speed=30,
        gold=2,
        experience=4,
        level=2,
        effects=[build_effect('frost', 60),
                 build_effect('toxin', 2)]),
    rogue_mage=dict(
        life=96,
        attack=12,
        defence=4,
        speed=100,
        gold=3,
        experience=6,
        level=2,
        effects=[build_effect('spl', 3, 30)]),
    slime_man=dict(
        life=122,
        attack=11,
        defence=2,
        speed=185,
        gold=3,
        experience=6,
        level=2,
        effects=[build_effect('evasion', 50)]),
    slime_noble=dict(
        life=101,
        attack=13,
        defence=3,
        speed=75,
        gold=3,
        experience=5,
        level=3,
        effects=[build_effect('level_pr', 25)]),
    toxic_dead=dict(
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
    black_slime=dict(
        life=157,
        attack=19,
        defence=8,
        speed=80,
        gold=4,
        experience=7,
        level=3,
        effects=[]),
    swordman=dict(
        life=135,
        attack=22,
        defence=6,
        speed=240,
        gold=4,
        experience=8,
        level=3,
        effects=[]),
    bowman=dict(
        life=160,
        attack=28,
        defence=8,
        speed=120,
        gold=5,
        experience=12,
        level=4,
        effects=[]),
    bird=dict(
        life=184,
        attack=23,
        defence=5,
        speed=130,
        gold=4,
        experience=8,
        level=3,
        effects=[build_effect('evasion', 25)]),
    goblin=dict(
        life=245,
        attack=26,
        defence=12,
        speed=110,
        gold=5,
        experience=13,
        level=4,
        effects=[]),
    red_slime_noble=dict(
        life=178,
        attack=20,
        defence=11,
        speed=75,
        gold=4,
        experience=8,
        level=4,
        effects=[build_effect('level_pr', 25)]),
    bat=dict(
        life=138,
        attack=35,
        defence=8,
        speed=140,
        gold=6,
        experience=14,
        level=4,
        effects=[build_effect('evasion', 35)]),
    black_slime_warrior=dict(
        life=288,
        attack=28,
        defence=15,
        speed=90,
        gold=6,
        experience=15,
        level=4,
        effects=[]),
    demon_seed=dict(
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
    metero_rogue_mage=dict(
        life=310,
        attack=33,
        defence=14,
        speed=100,
        gold=7,
        experience=18,
        level=4,
        effects=[build_effect('spl', 7, 60)]),
    tomb_watcher=dict(
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
    fire_of_soul=dict(
        life=107,
        attack=45,
        defence=15,
        speed=82,
        gold=7,
        experience=17,
        level=4,
        effects=[build_effect('frost', 160)]),
    tomb_general=dict(
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
    tomb_swordman=dict(
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
    big_bat=dict(
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
    nightmare_soldier=dict(
        life=268,
        attack=45,
        defence=27,
        speed=150,
        gold=9,
        experience=24,
        level=5,
        effects=[]),
    nightmare_mage=dict(
        life=373,
        attack=42,
        defence=24,
        speed=100,
        gold=9,
        experience=26,
        level=5,
        effects=[build_effect('spl', 3, 120)]),
    nightmare_shieldman=dict(
        life=550,
        attack=40,
        defence=28,
        speed=90,
        gold=10,
        experience=28,
        level=5,
        effects=[build_effect('stone_skin', 25, 3)]),
)


def get_monsters(monster_name_list: List[str]) -> List[Monster]:
    from .effect import build_effect as build_effect_instance
    res = []
    for name in monster_name_list:
        a_monster_dict = __monster_dict[name]
        a_monster_dict['effects'] = [
            build_effect_instance(name, *args, **kwargs)
            for name, args, kwargs in a_monster_dict['effects']
        ]
        res.append(Monster(**a_monster_dict))
    return res
