import math
from typing import Dict, List, Tuple

from .effect import DynamicEffect, Effect, EffectType, dispatch_effects
from .monster import Monster
from .player import Player


class Dule:

    def __init__(self, monster: Monster, player: Player):
        self.monster = monster
        self.player = player

    def get_player_attack(self):
        attack = self.player.attack
        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_ATTACK, []):
            attack = effect.on_get_player_attack(attack, state)
        return Effect.postprocess_value(state, attack)

    def get_monster_attack(self):
        attack = self.monster.attack
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_ATTACK, []):
            attack = effect.on_get_monster_attack(attack, state)
        return Effect.postprocess_value(state, attack)

    def get_player_defence(self):
        defence = self.player.defence
        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_DEFENCE, []):
            defence = effect.on_get_player_defence(defence, state)
        return Effect.postprocess_value(state, defence)

    def get_player_spell_defence(self):
        spell_defence = 0
        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_SPELL_DEFENCE,
                                           []):
            spell_defence = effect.on_get_player_spell_defence(
                spell_defence, state)
        return Effect.postprocess_value(state, spell_defence)

    def get_monster_defence(self):
        defence = self.monster.defence
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_DEFENCE, []):
            defence = effect.on_get_monster_defence(defence, state)
        return Effect.postprocess_value(state, defence)

    def get_player_speed(self):
        speed = self.player.speed
        state = {}
        for effect in self.effect_dict.get(EffectType.PLAYER_SPEED, []):
            speed = effect.on_get_player_defence(speed, state)
        return Effect.postprocess_value(state, speed)

    def get_monster_speed(self):
        speed = self.monster.speed
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_SPEED, []):
            speed = effect.on_get_monster_defence(speed, state)
        return Effect.postprocess_value(state, speed)

    def get_monster_physical_damage(self, physical_damage):
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_PHYSICAL_DMG,
                                           []):
            physical_damage = effect.on_get_monster_physical_damage(
                physical_damage, state)
        return Effect.postprocess_value(state, physical_damage)

    def get_player_damage(self):
        player_attack = self.get_player_attack()
        monster_defence = self.get_monster_defence()
        player_speed = self.get_player_speed()

        damage = max(player_attack - monster_defence, 0)
        multiplier = math.sqrt(player_speed / 100)
        damage = max(damage * multiplier, 0)

        for effect in self.effect_dict.get(EffectType.PLAYER_DAMAGE, []):
            damage = effect.on_get_player_damage(damage)

        return Effect.postprocess_value(damage)

    def get_monster_damage(self):
        monster_attack = self.get_monster_attack()
        player_defence = self.get_player_defence()
        monster_speed = self.get_monster_speed()

        physical_damage = max(monster_attack - player_defence, 0)
        physical_damage = self.get_monster_physical_damage(physical_damage)

        damage = physical_damage - self.get_player_spell_defence()
        multiplier = math.sqrt(monster_speed / 100)
        damage = max(damage * multiplier, 0)

        for effect in self.effect_dict.get(EffectType.MONSTER_DMG, []):
            damage = effect.on_get_monster_damage(damage)
        return Effect.postprocess_value(damage)

    def update_dynamic_effects(self, effect_dict: Dict):
        dynamic_effects: List[DynamicEffect] = \
            effect_dict.get(EffectType.DYNAMIC, [])
        for effect in dynamic_effects:
            effects = effect.to_static_effects(self.player, self.monster)
            dispatch_effects(effects, effect_dict)
        effect_dict.popitem(EffectType.DYNAMIC)

    def cal_res(self, crt_effects) -> Tuple[int, int]:
        self.effect_dict = dispatch_effects(crt_effects)
        self.update_dynamic_effects(self.effect_dict)

        from_first_turn = self.effect_dict.get(EffectType.FROM_FIRST_TURN,
                                               None)
        special_turn = self.effect_dict.get(EffectType.SPECIAL_TURN, None)

        crt_dmg = 0
        crt_turn = 0
        if from_first_turn:
            life = self.monster.life
            life -= self.get_player_damage()
            crt_turn = 1
            if life > 0:
                crt_dmg += self.get_monster_damage()
                for new_effect in from_first_turn:
                    new_dict = dispatch_effects(new_effect.effects)
                    self.update_dynamic_effects(new_dict)
                    self.effect_dict.update(new_dict)
                if self.get_player_damage() <= 0:
                    return 9999999999, 0, 0
                turn = math.ceil(life / self.get_player_damage()) - 1
                crt_dmg += self.get_monster_damage() * turn
                crt_turn += turn + 1
        elif special_turn:
            original_effect_dict = self.effect_dict.copy()
            life = self.monster.life

            # only support one special turn now
            effect = special_turn[0]
            new_dict = dispatch_effects(effect.effects)
            self.update_dynamic_effects(new_dict)
            self.effect_dict.update(new_dict)
            player_dmg = self.get_player_damage()
            turn = math.ceil(life / player_dmg) - 1
            if turn > effect.turn:
                crt_dmg += self.get_monster_damage() * effect.turn
                life -= player_dmg * effect.turn
                self.effect_dict = original_effect_dict
                turn = math.ceil(life / self.get_player_damage()) - 1
                crt_dmg += self.get_monster_damage() * turn
                crt_turn = effect.turn + turn + 1
            else:
                crt_dmg += self.get_monster_damage() * turn
                crt_turn = turn + 1

        else:
            if self.get_player_damage() <= 0:
                return 9999999999, 0, 0
            turn = math.ceil(self.monster.life / self.get_player_damage()) - 1
            crt_dmg = self.get_monster_damage() * turn
            crt_turn = turn + 1
        crt_dmg = math.floor(crt_dmg)
        return crt_dmg, crt_turn

    def cal_all_res(self, test_effect: type) -> Dict[str, Tuple[int, int]]:

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

                    crt_dmg, _ = self.cal_res(crt_effects)

                    if key not in res or res[key][0] > crt_dmg:
                        res[key] = (crt_dmg, id)

        return res

    def cal_opt_res(self,
                    player_atk_mod=0,
                    player_def_mod=0) -> Tuple[int, int, int]:
        self.player._attack += player_atk_mod
        self.player._defence += player_def_mod
        combs = self.player.get_equipment_comb()
        opt_dmg = 9999999999
        opt_turn = 0
        equip_comb_id = 0
        for id, equip_comb in enumerate(combs):
            crt_effects = equip_comb.copy()
            crt_effects.extend(self.monster.effects)

            crt_dmg, crt_turn = self.cal_res(crt_effects)

            if crt_dmg < opt_dmg:
                opt_dmg = crt_dmg
                opt_turn = crt_turn
                equip_comb_id = id
        self.player._attack -= player_atk_mod
        self.player._defence -= player_def_mod
        return opt_dmg, opt_turn, equip_comb_id
