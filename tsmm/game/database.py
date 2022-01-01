from typing import List, Tuple

from .monster.monster import Monster, get_monster_set

__monster_instances = []
__monster_names = []


def build_monsters(monster_set_name: str) -> List[Monster]:
    global __monster_names
    monster_set = get_monster_set(monster_set_name)
    __monster_names = list(monster_set.keys())
    for k, v in monster_set.items():
        __monster_instances.append(v())
    return __monster_instances


def get_monsters() -> Tuple[List[str], List[Monster]]:
    return __monster_names, __monster_instances
