from typing import List, Tuple

from .monster.monster import Monster, get_monster_set

__monster_instances = []
__monster_names = []


def build_monsters(monster_name_list: List[str],
                   monster_set_name: str) -> List[Monster]:
    global __monster_names
    __monster_names = monster_name_list
    monster_set = get_monster_set(monster_set_name)

    for name in monster_name_list:
        __monster_instances.append(monster_set[name]())
    return __monster_instances


def get_monsters() -> Tuple[List[str], List[Monster]]:
    return __monster_names, __monster_instances
