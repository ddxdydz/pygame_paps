from basic.game_logic.GameCollidingObject import GameCollidingObject


class DamageArea(GameCollidingObject):
    def __init__(self, coordinates: tuple, size=(0, 0), rect=(0, 0, 1, 1), damage=20, impuls=0.5):
        super().__init__(coordinates, size)
        self.set_collision_rect(*rect)
        self.damage = damage
        self.impuls = impuls
