import math
from copy import deepcopy
from typing import Dict, List, Tuple

import mt.game.utils.math_util as math_util
from mt.game.effect.effect import VaringEffect

from ..effect import DynamicEffect, Effect, EffectType, dispatch_effects
from ..monster.monster import Monster
from ..player import Player
from .dule import Dule


class SimpleDule(Dule):

    def __init__(self, monster: Monster, player: Player):
        super().__init__(monster, player)

    def get_player_damage(self):
        player_attack = self.get_player_attack()
        monster_defence = self.get_monster_defence()

        damage = max(player_attack - monster_defence, 0)

        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_DAMAGE, []):
            damage = effect.on_get_player_damage(damage, state)

        damage = max(damage, 0)

        return Effect.postprocess_value(state, damage)

    def get_monster_damage(self):
        monster_attack = self.get_monster_attack()
        player_defence = self.get_player_defence()

        damage = max(monster_attack - player_defence, 0)

        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_DAMAGE, []):
            damage = effect.on_get_monster_damage(damage, state)

        damage = max(damage, 0)

        return Effect.postprocess_value(state, damage)

    def cal_res(self, player_atk_mod=0, player_def_mod=0) -> Tuple[int, int]:
        self.player._attack += player_atk_mod
        self.player._defence += player_def_mod

        self.effect_dict = dispatch_effects(self.monster.effects)

        crt_dmg = 0
        crt_turn = 0
        monster_life = self.get_monster_life()
        if self.get_player_damage() <= 0:
            return None, 0
        turn = math.ceil(monster_life / self.get_player_damage()) - 1

        monster_dmg = self.get_monster_damage()
        crt_dmg = monster_dmg * turn
        if EffectType.FIRST_STRIKE in self.effect_dict:
            crt_dmg += monster_dmg
        crt_turn = turn + 1

        crt_dmg = max(crt_dmg - self.player.energy_shield, 0)

        self.player._attack -= player_atk_mod
        self.player._defence -= player_def_mod
        return int(crt_dmg), crt_turn

    def cal_all_res(self) -> List[Tuple[int, int, int]]:
        monster_life = self.get_monster_life()
        dmg = self.get_player_damage()
        res = []
        if dmg <= 0:
            res.append((0, None, 0))
            player_attack = self.get_player_attack()
            monster_defence = self.get_monster_defence()
            dmg = player_attack - monster_defence
            turn = None
        else:
            res.append((0, *self.cal_res()))
            turn = math.ceil(monster_life / dmg)

        for _ in range(5):
            if dmg <= 0 and turn is None:
                turn = monster_life
            else:
                turn -= 1
            if turn > 0:
                dst_dmg = math.ceil(monster_life / turn)
                dmg_diff = dst_dmg - dmg
                if dmg_diff <= res[-1][0]:
                    dmg_diff += 1
                res_dmg, res_turn = self.cal_res(dmg_diff)
                turn = res_turn
                if res_dmg > 0 or res[-1][1] is None or res[-1][1] != 0:
                    res.append((dmg_diff, res_dmg, res_turn))
            else:
                break

        return res
