from formulas import AttackGenerator

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
