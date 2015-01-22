# decorators

def generate(to_affect):
    def setting(toset):
        def fn(func):
            setattr(func, to_affect, toset)
            return func
        return fn
    return setting

element = generate("element")
attack_type = generate("attack_type")
strength = generate("strength")
attack_category = generate("attack_category")
mp_cost = generate("mp_cost")
hit_rate = generate("hit_rate")
