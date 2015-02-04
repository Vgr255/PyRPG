from formulas import *
from definitions import *

# Black Magic

Fire = AttackGenerator(element=Elements.Fire, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Fira = AttackGenerator(element=Elements.Fire, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Firaga = AttackGenerator(element=Elements.Fire, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

Blizzard = AttackGenerator(element=Elements.Ice, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Blizzara = AttackGenerator(element=Elements.Ice, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Blizzaga = AttackGenerator(element=Elements.Ice, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

Thunder = AttackGenerator(element=Elements.Thunder, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Thundara = AttackGenerator(element=Elements.Thunder, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Thundaga = AttackGenerator(element=Elements.Thunder, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

Aero = AttackGenerator(element=Elements.Wind, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=11, mp_cost=4, hit_rate=100)
Aera = AttackGenerator(element=Elements.Wind, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=22, hit_rate=100)
Aeroga = AttackGenerator(element=Elements.Wind, type=AttackTypes.Magical, attack_category=AttackCategories.BlackMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=70, mp_cost=52, hit_rate=100)

# Red Magic

Shake = AttackGenerator(element=Elements.Earth, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=14, mp_cost=6, hit_rate=100)
Quake = AttackGenerator(element=Elements.Earth, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=27, mp_cost=28, hit_rate=100)
Seism = AttackGenerator(element=Elements.Earth, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=74, mp_cost=68, hit_Rate=100)

Water = AttackGenerator(element=Elements.Water, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2,reflectable=True,  strength=14, mp_cost=6, hit_rate=100)
Wave = AttackGenerator(element=Elements.Water, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=27, mp_cost=28, hit_rate=100)
Flood = AttackGenerator(element=Elements.Water, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=74, mp_cost=68, hit_rate=100)

Bio = AttackGenerator(element=Elements.Poison, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=10, mp_cost=8, status_effects=(StatusEffects.Virus,), status_chance=32, hit_rate=100)
Disease = AttackGenerator(element=Elements.Poison, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=36, status_effects=(StatusEffects.Virus,), status_chance=49, hit_rate=100)
Virus = AttackGenerator(element=Elements.Poison, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=68, mp_cost=80, status_effects=(StatusEffects.Virus,), status_chance=98, hit_rate=100)

Dia = AttackGenerator(element=Elements.Holy, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=10, mp_cost=8, hit_rate=100)
Pure = AttackGenerator(element=Elements.Holy, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=24, mp_cost=36, hit_rate=100)
White = AttackGenerator(element=Elements.Holy, type=AttackTypes.Magical, attack_category=AttackCategories.RedMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=68, mp_cost=80, hit_rate=100)

# White Magic

Cure = AttackGenerator(element=Elements.Restorative, type=AttackTypes.Magical, attack_category=AttackCategories.WhiteMagic, attack_formula=StrengthAttackLevel3, reflectable=True, strength=5, mp_cost=5, hit_rate=120)
Cura = AttackGenerator(element=Elements.Restorative, type=AttackTypes.Magical, attack_category=AttackCategories.WhiteMagic, attack_formula=StrengthAttackLevel3, reflectable=True, strength=34, mp_cost=24, hit_rate=120)
Curaga = AttackGenerator(element=Elements.Restorative, type=AttackTypes.Magical, attack_category=AttackCategories.WhiteMagic, attack_formula=StrengthAttackLevel3, reflectable=True, strength=130, mp_cost=64, hit_rate=120)

# Blue Magic

Gravity = AttackGenerator(element=Elements.Gravity, type=AttackTypes.Magical, attack_category=AttackCategories.BlueMagic, attack_formula=CurrentHPFormula, reflectable=True, strength=8, mp_cost=14, hit_rate=75)
Gravira = AttackGenerator(element=Elements.Gravity, type=AttackTypes.Magical, attack_category=AttackCategories.BlueMagic, attack_formula=CurrentHPFormula, reflectable=True, strength=16, mp_cost=33, hit_rate=75)
Graviga = AttackGenerator(element=Elements.Gravity, type=AttackTypes.Magical, attack_category=AttackCategories.BlueMagic, attack_formula=CurrentHPFormula, reflectable=True, strength=24, mp_cost=48, hit_rate=75)

# Purple Magic

Hell = AttackGenerator(element=Elements.Fire, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(StatusEffects.Burn,), status_chance=125, hit_rate=100)
Freeze = AttackGenerator(element=Elements.Ice, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(StatusEffects.Paralysis,), status_chance=125, hit_rate=100)
Electrocute = AttackGenerator(element=Elements.Thunder, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(StatusEffects.Shock,), status_chance=125, hit_rate=100)
Tornado = AttackGenerator(element=Elements.Wind, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=116, mp_cost=96, status_effects=(StatusEffects.Confuse,), status_chance=125, hit_rate=100)

Stone = AttackGenerator(element=Elements.Earth, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=120, mp_cost=108, status_effects=(StatusEffects.Petrify,), status_chance=125, hit_rate=100)
Tsunami = AttackGenerator(element=Elements.Water, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=120, mp_cost=108, status_effects=(StatusEffects.Lock,), status_chance=125, hit_rate=100)
Pandemic = AttackGenerator(element=Elements.Poison, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=112, mp_cost=128, status_effects=(StatusEffects.Virus,), status_chance=125, hit_rate=100)
Holy = AttackGenerator(element=Elements.Holy, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel2, reflectable=True, strength=112, mp_cost=128, status_effects=(StatusEffects.Silence,), status_chance=125, hit_rate=100)

Curaja = AttackGenerator(element=Elements.Restorative, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=StrengthAttackLevel3, reflectable=True, strength=182, mp_cost=84, additional_effect=AdditionalEffects.HealAllStatus, hit_rate=100)

Gravija = AttackGenerator(element=Elements.Gravity, type=AttackTypes.Magical, attack_category=AttackCategories.PurpleMagic, attack_formula=CurrentHPFormula, reflectable=True, strength=30, mp_cost=62, status_effects=(StatusEffects.Darkness,), status_chance=125, hit_rate=75)
