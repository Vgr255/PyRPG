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
            return int(attacker.cur_hp * (self.strength / 32))

    class MaxHPFormula:
        def __init__(self, strength):
            self.strength = strength

        def damage(self, attacker, target):
            return int(attacker.max_hp * (self.strength / 32))

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

class AttackAttributes:
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
        self.affect_mp = False
        self.drain_hp = False
        self.drain_mp = False
        self.ignore_def = False
        self.only_dead = False
        self.reflectable = False
        self.no_retarget = False
        self.allow_crit = True
        self.additional_effect = None
        self.status_effect = ()
        self.status_chance = 0
        self.strength = 0
        self.mp_cost = 0

        self.__dict__.update(kwargs)
