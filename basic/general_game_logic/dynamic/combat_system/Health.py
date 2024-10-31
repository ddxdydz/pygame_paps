from math import inf


class Health:
    def __init__(self):
        self.health = inf
        self.max_health = inf
        self.shield = 0
        self.decrease_prohibition = False

    def set_parameters(self, health: float, max_health: float, shield: float = 0):
        if health < 0:
            raise Exception("GameDynamicObject Error: set health < 0")
        if max_health < 0:
            raise Exception("GameDynamicObject Error: set max_health < 0")
        if shield < 0:
            raise Exception("GameDynamicObject Error: set shield < 0")
        self.health = health
        self.max_health = max_health
        self.shield = shield

    def switch_decrease_prohibition(self):
        self.decrease_prohibition = not self.decrease_prohibition

    def decrease_health(self, value):
        if self.decrease_prohibition:
            return
        self.health -= value
        if self.health < 0:
            self.health = 0

    def increase_health(self, value):
        if value > 0:
            self.health += value

    def take_damage(self, damage):
        damage -= self.shield
        if damage < 0:
            damage = 0
        self.decrease_health(damage)

    def is_died(self):
        return self.health == 0
