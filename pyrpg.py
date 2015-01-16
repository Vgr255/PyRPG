# Something something classes damage stuff
# This is a bad attempt at trying to make a text-based RPG game
# Loosely based off FF7's battle system and years of both handwritten notes and daydreaming
# Yes, I daydream about RPGs. Because why not.
# something something use at will give credit contribute etc etc
# -Vgr
# can also ask me on IRC to be given push access if you want

from constants import *

# This is only a draft, and can change heavily

"""
I want to have each character, magic, summon, item etc as a class instance
Already have the frame of how I'd want to use this in here, use as reference

constants stuff are 8-bits hex values because it's fun and they look like offsets
this can add many modules and stuff as this grows

this is really more of a fun kinda project than a serious one
as such commit history doesn't matter, have ten unrelated things in one commit,
merge commits, etc. I don't care; if this ever gets bigger we can clean it up

this is already kinda object-oriented even though I suck at OOP to begin with

my notes and some of my fantasy world (long story, you don't need to know) will come online at some point
my notes are mainly handwritten though, and in French, but you can get some out of it

this is also based off FF7's battle damage formulas, and other various FFs

-Vgr"""

class DamageTypes:
    def _recovery(target):
        target.cur_hp = target.max_hp
        target.cur_mp = target.max_mp
        target.status.clear()
        return RECOVERY

    def _fixed_damage(strength):
        return int(strength * FIXED_DAMAGE_MULTIPLIER)

class AttackFormula(DamageTypes):
    class NoDamage:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return 0

    class StrengthAttackLevel1:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return int((self.strength / 16) * (attacker.attack + ((attacker.level + attacker.attack) * 32) ** 2))

    class StrengthAttackLevel2:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return int((self.strength / 16) * ((attacker.level + attacker.attack) * 6))

    class StrengthAttackLevel3:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return int((self.strength * 22) + ((attacker.level + attacker.attack) * 6))

    class CurrentHPFormula:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return int(target.cur_hp * (self.strength / 32))

    class MaxHPFormula:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return int(target.max_hp * (self.strength / 32))

    class FixedDamage:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return _fixed_damage(self.strength)

    class Recovery:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return _recovery(attacker, target)

class AttackGenerator(AttackFormula):
    def __init__(self, **kwargs):
        # Target settings
        self.enable_selection = True
        self.start_on_enemies = True
        self.toggle_target_group = True
        self.start_as_multiple = True
        self.toggle_multiple = True
        self.one_row_only = False
        self.short_range = False
        self.all_rows = False
        self.random = False

        # Attack properties
        self.element = None
        self.type = PHYSICAL
        self.attack_category = None
        self.attack_formula = NoDamage
        self.affect_mp = False
        self.drain_hp = False
        self.drain_mp = False
        self.ignore_def = False
        self.only_dead = False
        self.reflectable = False
        self.no_retarget = False
        self.allow_crit = False
        self.additional_effect = None
        self.status_effects = ()
        self.status_modify = STATUS_ADD
        self.status_chance = 0 # up to 255 (base 16)
        self.strength = 0 # base 10
        self.mp_cost = 0 # base 10
        self.hit_rate = 0 # up to 255 (base 16)

        self.__dict__.update(kwargs)

        self._attack_formula = self.attack_formula(self.strength)

# Black Magic

Fire = AttackGenerator(element=FIRE, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Fira = AttackGenerator(element=FIRE, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Firaga = AttackGenerator(element=FIRE, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

Blizzard = AttackGenerator(element=ICE, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Blizzara = AttackGenerator(element=ICE, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Blizzaga = AttackGenerator(element=ICE, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

Thunder = AttackGenerator(element=THUNDER, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Thundara = AttackGenerator(element=THUNDER, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Thundaga = AttackGenerator(element=THUNDER, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

Aero = AttackGenerator(element=WIND, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Aera = AttackGenerator(element=WIND, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Aeroga = AttackGenerator(element=WIND, type=MAGICAL, attack_category=BLACK_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

# Red Magic

Shake = AttackGenerator(element=EARTH, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=14, mp_cost=6, hit_rate=100)
Quake = AttackGenerator(element=EARTH, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=27, mp_cost=28, hit_rate=100)
Seism = AttackGenerator(element=EARTH, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=74, mp_cost=68, hit_Rate=100)

Water = AttackGenerator(element=WATER, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2,reflectable=True,  strength=14, mp_cost=6, hit_rate=100)
Wave = AttackGenerator(element=WATER, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=27, mp_cost=28, hit_rate=100)
Flood = AttackGenerator(element=WATER, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=74, mp_cost=68, hit_rate=100)

Bio = AttackGenerator(element=POISON, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=10, mp_cost=8, status_effects=(VIRUS,), status_chance=32, hit_rate=100)
Disease = AttackGenerator(element=POISON, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=36, status_effects=(VIRUS,), status_chance=49, hit_rate=100)
Virus = AttackGenerator(element=POISON, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=68, mp_cost=80, status_effects=(VIRUS,), status_chance=98, hit_rate=100)

Dia = AttackGenerator(element=HOLY, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=10, mp_cost=8, hit_rate=100)
Pure = AttackGenerator(element=HOLY, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=36, hit_rate=100)
White = AttackGenerator(element=HOLY, type=MAGICAL, attack_category=RED_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=68, mp_cost=80, hit_rate=100)

# White Magic

Cure = AttackGenerator(element=RESTORATIVE, type=MAGICAL, attack_category=WHITE_MAGIC, attack_formula=StrengthAttackLevel3, reflectable=True, strength=5, mp_cost=5, hit_rate=120)
Cura = AttackGenerator(element=RESTORATIVE, type=MAGICAL, attack_category=WHITE_MAGIC, attack_formula=StrengthAttackLevel3, reflectable=True, strength=34, mp_cost=24, hit_rate=120)
Curaga = AttackGenerator(element=RESTORATIVE, type=MAGICAL, attack_category=WHITE_MAGIC, attack_formula=StrengthAttackLevel3, reflectable=True, strength=130, mp_cost=64, hit_rate=120)

# Blue Magic

Gravity = AttackGenerator(element=GRAVITY, type=MAGICAL, attack_category=BLUE_MAGIC, attack_formula=CurrentHPFormula, reflectable=True, strength=8, mp_cost=14, hit_rate=75)
Gravira = AttackGenerator(element=GRAVITY, type=MAGICAL, attack_category=BLUE_MAGIC, attack_formula=CurrentHPFormula, reflectable=True, strength=16, mp_cost=33, hit_rate=75)
Graviga = AttackGenerator(element=GRAVITY, type=MAGICAL, attack_category=BLUE_MAGIC, attack_formula=CurrentHPFormula, reflectable=True, strength=24, mp_cost=48, hit_rate=75)

# Purple Magic

Hell = AttackGenerator(element=FIRE, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(BURN,), status_chance=125, hit_rate=100)
Freeze = AttackGenerator(element=ICE, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(PARALYSIS,), status_chance=125, hit_rate=100)
Electrocute = AttackGenerator(element=THUNDER, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(SHOCK,), status_chance=125, hit_rate=100)
Tornado = AttackGenerator(element=WIND, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(CONFUSE,), status_chance=125, hit_rate=100)

Stone = AttackGenerator(element=EARTH, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=120, mp_cost=108, status_effects=(PETRIFY,), status_chance=125, hit_rate=100)
Tsunami = AttackGenerator(element=WATER, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=120, mp_cost=108, status_effects=(LOCK), status_chance=125, hit_rate=100)
Pandemic = AttackGenerator(element=POISON, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=112, mp_cost=128, status_effects=(VIRUS,), status_chance=125, hit_rate=100)
Holy = AttackGenerator(element=HOLY, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel2, reflectable=True, strength=112, mp_cost=128, status_effects=(SILENCE,), status_chance=125, hit_rate=100)

Curaja = AttackGenerator(element=RESTORATIVE, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=StrengthAttackLevel3, reflectable=True, strength=182, mp_cost=84, additional_effect=HEALALLSTATUS, hit_rate=100)

Gravija = AttackGenerator(element=GRAVITY, type=MAGICAL, attack_category=PURPLE_MAGIC, attack_formula=CurrentHPFormula, reflectable=True, strength=30, mp_cost=62, status_effects=(DARKNESS,), status_chance=125, hit_rate=75)
