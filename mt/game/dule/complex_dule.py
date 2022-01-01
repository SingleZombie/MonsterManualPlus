import math
from copy import deepcopy
from typing import Dict, List, Tuple

import mt.game.utils.math_util as math_util
from mt.game.effect.effect import VaringEffect

from ..effect import DynamicEffect, Effect, EffectType, dispatch_effects
from ..monster.monster import Monster
from ..player import Player
from .dule import Dule


def merge_dict(a: Dict, b: Dict):
    for k, v in b.items():
        if k in a:
            a[k].extend(v)
        else:
            a[k] = v


class ComplexDule(Dule):

    def __init__(self, monster: Monster, player: Player):
        super().__init__(monster, player)

    def get_player_physical_damage(self, physical_damage):
        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_PHYSICAL_DAMAGE,
                                           []):
            physical_damage = effect.on_get_player_physical_damage(
                physical_damage, state)
        armor = state.get('armor', 0)
        multiplier = 1 / (armor * 0.06 + 1)
        physical_damage *= multiplier
        return Effect.postprocess_value(state, physical_damage)

    def get_monster_physical_damage(self, physical_damage):
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_PHYSICAL_DAMAGE,
                                           []):
            physical_damage = effect.on_get_monster_physical_damage(
                physical_damage, state)
        armor = state.get('armor', 0)
        multiplier = 1 / (armor * 0.06 + 1)
        physical_damage *= multiplier
        return Effect.postprocess_value(state, physical_damage)

    def get_player_damage(self):
        player_attack = self.get_player_attack()
        monster_defence = self.get_monster_defence()
        player_speed = self.get_player_speed()
        if player_speed <= 0:
            return 0
        multiplier = math.sqrt(player_speed / 100)

        physical_damage = max(player_attack - monster_defence, 0) * multiplier
        physical_damage = self.get_player_physical_damage(physical_damage)

        # spell_damage = max(-self.get_player_spell_defence(), 0)
        # damage = physical_damage + spell_damage
        damage = physical_damage

        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_DAMAGE, []):
            damage = effect.on_get_player_damage(damage, state)

        return Effect.postprocess_value(state, damage)

    def get_player_regenerate(self):
        regenerate = 0
        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_REGENERATE, []):
            regenerate = effect.on_get_player_regenerate(regenerate, state)
        return Effect.postprocess_value(state, regenerate)

    def get_monster_damage(self):
        monster_attack = self.get_monster_attack()
        player_defence = self.get_player_defence()
        monster_speed = self.get_monster_speed()
        multiplier = math.sqrt(monster_speed / 100)

        physical_damage = max(monster_attack - player_defence, 0) * multiplier
        physical_damage = self.get_monster_physical_damage(physical_damage)

        spell_damage = max(-self.get_player_spell_defence(), 0)
        damage = physical_damage + spell_damage

        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_DAMAGE, []):
            damage = effect.on_get_monster_damage(damage, state)

        return Effect.postprocess_value(state, damage)

    def update_dynamic_effects(self, effect_dict: Dict):
        dynamic_effects: List[DynamicEffect] = \
            effect_dict.get(EffectType.DYNAMIC, [])
        for effect in dynamic_effects:
            effects = effect.to_static_effects(self.player, self.monster)
            dispatch_effects(effects, effect_dict)
        if EffectType.DYNAMIC in effect_dict:
            effect_dict.pop(EffectType.DYNAMIC)

    def update_varing_effects(self, effect_dict: Dict, extra_inputs: Dict):
        varing_effects: List[VaringEffect] = \
            effect_dict.get(EffectType.VARING, [])
        for effect in varing_effects:
            effects = effect.to_static_effects(extra_inputs)
            dispatch_effects(effects, effect_dict)
        if EffectType.VARING in effect_dict:
            effect_dict.pop(EffectType.VARING)

    def cal_res(self, crt_effects, extra_inputs) -> Tuple[int, int]:
        self.effect_dict = dispatch_effects(crt_effects)
        self.update_dynamic_effects(self.effect_dict)
        self.update_varing_effects(self.effect_dict, extra_inputs)

        from_first_turn = self.effect_dict.get(EffectType.FROM_FIRST_TURN,
                                               None)
        special_turn = self.effect_dict.get(EffectType.SPECIAL_TURN, None)

        crt_dmg = 0
        crt_turn = 0
        monster_life = self.get_monster_life()
        if from_first_turn:
            life = monster_life
            life -= self.get_player_damage()
            regenerate = self.get_player_regenerate()
            crt_dmg -= regenerate
            crt_turn = 1
            if life > 0:
                crt_dmg += self.get_monster_damage()
                for new_effect in from_first_turn:
                    new_dict = dispatch_effects(new_effect.effects)
                    self.update_dynamic_effects(new_dict)
                    merge_dict(self.effect_dict, new_dict)
                if self.get_player_damage() <= 0:
                    return None, 0
                turn = math.ceil(life / self.get_player_damage()) - 1
                regenerate = self.get_player_regenerate()
                crt_dmg += self.get_monster_damage() * turn
                crt_dmg -= self.get_player_regenerate() * (turn + 1)
                crt_turn += turn + 1
        elif special_turn:
            original_effect_dict = deepcopy(self.effect_dict)
            life = monster_life

            # only support one special turn now
            effect = special_turn[0]
            new_dict = dispatch_effects(effect.effects[0])
            self.update_dynamic_effects(new_dict)
            merge_dict(self.effect_dict, new_dict)
            player_dmg = self.get_player_damage()
            if player_dmg <= 0:
                return None, 0
            turn = math.ceil(life / player_dmg) - 1
            if turn > effect.turn:
                crt_dmg += self.get_monster_damage() * effect.turn
                crt_dmg -= self.get_player_regenerate() * (effect.turn + 1)
                life -= player_dmg * effect.turn

                self.effect_dict = original_effect_dict
                new_dict = dispatch_effects(effect.effects[1])
                self.update_dynamic_effects(new_dict)
                merge_dict(self.effect_dict, new_dict)
                turn = math.ceil(life / self.get_player_damage()) - 1
                crt_dmg += self.get_monster_damage() * turn
                crt_dmg -= self.get_player_regenerate() * turn
                crt_turn = effect.turn + turn + 1
            else:
                crt_dmg += self.get_monster_damage() * turn
                crt_dmg -= self.get_player_regenerate() * (turn + 1)
                crt_turn = turn + 1

        else:
            life = monster_life
            if self.get_player_damage() <= 0:
                return None, 0
            turn = math.ceil(life / self.get_player_damage()) - 1
            crt_dmg = self.get_monster_damage() * turn
            crt_dmg -= self.get_player_regenerate() * (turn + 1)
            crt_turn = turn + 1
        crt_dmg = math_util.floor(crt_dmg)
        return crt_dmg, crt_turn

    def cal_test_res(self, test_effect: type,
                     extra_inputs: Dict) -> Dict[str, Tuple[int, int]]:

        combs = self.player.get_equipment_comb()
        res = {}
        for id, equip_comb in enumerate(combs):
            crt_effects = equip_comb.copy()
            crt_effects.extend(self.monster.effects)
            new_list = []
            test_effect_dicts = []
            for effect in crt_effects:
                if isinstance(effect, test_effect):
                    test_effect_dicts.append(effect.to_test_static_effects())
                else:
                    new_list.append(effect)

            if len(test_effect_dicts) > 0:
                for key in test_effect_dicts[0]:
                    crt_effects = new_list.copy()
                    for effect_dict in test_effect_dicts:
                        extra_effects = effect_dict[key]
                        crt_effects.extend(extra_effects)

                    crt_dmg, _ = self.cal_res(crt_effects, extra_inputs)

                    if key not in res or res[key][0] > crt_dmg:
                        res[key] = (crt_dmg, id)

        return res

    def cal_opt_res(self,
                    player_atk_mod=0,
                    player_def_mod=0,
                    extra_inputs: Dict = {}) -> Tuple[int, int, int]:
        self.player._attack += player_atk_mod
        self.player._defence += player_def_mod
        combs = self.player.get_equipment_comb()
        opt_dmg = None
        opt_turn = 0
        equip_comb_id = 0
        for id, equip_comb in enumerate(combs):
            crt_effects = equip_comb.copy()
            crt_effects.extend(self.monster.effects)

            crt_dmg, crt_turn = self.cal_res(crt_effects, extra_inputs)

            if crt_dmg is not None and (opt_dmg is None or crt_dmg < opt_dmg):
                opt_dmg = crt_dmg
                opt_turn = crt_turn
                equip_comb_id = id
        self.player._attack -= player_atk_mod
        self.player._defence -= player_def_mod
        return opt_dmg, opt_turn, equip_comb_id
