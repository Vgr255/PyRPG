from enum import Enum

class Fixed(Enum):
    DamageMultiplier = 32

Constants = Enum("Constant", "Recovery, Miss")
Elements = Enum("Element", "Fire, Ice, Thunder, Wind, Earth, Poison, Water, Restorative, Gravity, Holy")
StatusEffects = Enum("Status Effect", "Death, Sleep, Virus, Confuse, Silence, Haste, Slow, Stop, Petrify, " +
                     "Regen, Protect, Shell, Reflect, Dual, Shield, Berserk, Paralysis, Darkness, Shock, Lock")
StatusEffectModifiers = Enum("Status Effect Modifier", "Add, Remove, Toggle")
AttackTypes = Enum("Type", "Physical, Magical, Special")
CharacterJobs = Enum("Character Job", "WhiteMage, BlackMage, RedMage, BlueMage, TimeMage, Knight, Fighter, " +
                     "Paladin, Monk, Archer, Gunner, Dragoon, Ninja, Assassin, Gladiator, Sniper, Thief, " +
                     "Summoner, Alchemist, Sage, Mime, Freelancer")
AttackCategories = Enum("Attack Category", "WhiteMagic, BlackMagic, RedMagic, BlueMagic, TimeMagic, " +
                        "GreenMagic, PurpleMagic, ArcaneMagic")
