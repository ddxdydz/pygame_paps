from basic.game_logic.GameCollidingObject import GameCollidingObject


class Wall(GameCollidingObject):
    CODE = "ws1"

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.set_collision_rect(0, 0, 1, 1)

    def get_code(self):
        return Wall.CODE
