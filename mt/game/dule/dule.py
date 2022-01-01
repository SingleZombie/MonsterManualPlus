from abc import ABCMeta, abstractmethod

from ..effect import Effect, EffectType
from ..monster.monster import Monster
from ..player import Player


class Dule(metaclass=ABCMeta):

    def __init__(self, monster: Monster, player: Player):
        self.monster = monster
        self.player = player
        self.effect_dict = {}

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

    def get_monster_life(self):
        life = self.monster.life
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_LIFE, []):
            life = effect.on_get_monster_life(life, state)
        return Effect.postprocess_value(state, life)

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
            speed = effect.on_get_player_speed(speed, state)
        return Effect.postprocess_value(state, speed)

    def get_monster_speed(self):
        speed = self.monster.speed
        state = {}
        for effect in self.effect_dict.get(EffectType.MONSTER_SPEED, []):
            speed = effect.on_get_monster_speed(speed, state)
        return Effect.postprocess_value(state, speed)

    @abstractmethod
    def get_player_damage(self):
        pass

    @abstractmethod
    def get_monster_damage(self):
        pass
