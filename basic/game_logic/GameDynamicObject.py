from basic.game_logic.collisions.CollisionController import CollisionController
from basic.game_logic.GameCollidingObject import GameCollidingObject


class GameDynamicObject(GameCollidingObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.processing_move = [0, 0]

    def add_processing_move(self, dx, dy):
        self.processing_move[0] += dx
        self.processing_move[1] += dy

    def reset_processing_move(self):
        self.processing_move = [0, 0]

    def get_processing_move(self):
        return self.processing_move

    def do_move(self, safe=False, hard_objects=None):
        if hard_objects is None:
            hard_objects = []
        if safe:
            CollisionController.make_safe_move(self, self.processing_move, hard_objects)
        else:
            CollisionController.make_move(self, self.processing_move)
        self.reset_processing_move()
