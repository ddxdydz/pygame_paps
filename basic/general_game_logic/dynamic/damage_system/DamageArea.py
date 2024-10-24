from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject


class DamageArea(GameCollidingObject):
    def __init__(self, coordinates: tuple, size=(0, 0), rect=(0, 0, 1, 1)):
        super().__init__(coordinates, size)
        self.create_collision_rect(*rect)
