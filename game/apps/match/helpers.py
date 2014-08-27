import math
import random

PLAYER_DAMAGE_BASE = 2
PLAYER_DAMAGE_TUNING = 1.1

PLAYER_HEALTH_BASE = 12
PLAYER_HEALTH_TUNING = 1.3

BOSS_DAMAGE_BASE = 1
BOSS_DAMAGE_TUNING = 1.1

PLAYER_BASE_HP = 20
PLAYER_HP_TUNING = 1.6

BOSS_HEALTH_BASE = 30
BOSS_HP_TUNING = 2

PERSENTAGE_XP_GIVEN = 20
XP_BASE_REWARD = 100


def calculate_player_damage(character, spell):
    player_level = character.character.level_data()['current_level']
    min_damage = math.floor(PLAYER_DAMAGE_BASE + spell.damage + math.pow(player_level, PLAYER_DAMAGE_TUNING))
    max_damage = math.floor(PLAYER_DAMAGE_BASE + spell.damage + player_level + math.pow(player_level, PLAYER_DAMAGE_TUNING))

    return random.randint(min_damage, max_damage)


def calculate_boss_damage(boss_spell, match):
    boss_level = match.enemy.level
    min_damage = math.floor(boss_spell.damage + math.pow(boss_level, BOSS_DAMAGE_TUNING))
    max_damage = math.floor(boss_spell.damage + boss_level + math.pow(boss_level, BOSS_DAMAGE_TUNING))

    return random.randint(min_damage, max_damage)


def calculate_player_health(character):
    player_level = character.level_data()['current_level']
    character_hp = math.ceil(PLAYER_BASE_HP + math.pow(player_level, PLAYER_HP_TUNING))

    return character_hp


def calculate_boss_health(boss):
    boss_hp = math.ceil(BOSS_HEALTH_BASE + math.pow(boss.level, BOSS_HP_TUNING))

    return boss_hp


def calculate_xp(match):
    level_diffrence = 1 + (match.enemy.level - match.character.level_data()['current_level']) * 0.2
    xp_reward = level_diffrence * XP_BASE_REWARD
    if xp_reward <= 0:
        xp_reward = XP_BASE_REWARD / 10
    return xp_reward

