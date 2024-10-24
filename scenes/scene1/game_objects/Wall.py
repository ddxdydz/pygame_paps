from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject


class Wall(GameCollidingObject):
    def __init__(self, coordinates, size=(1, 1)):
        super().__init__(coordinates)
        self.create_collision_rect(0, 0, *size)

