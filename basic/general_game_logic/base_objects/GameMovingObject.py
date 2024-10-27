from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.dynamic.movement_system.MovementController import MovementController


class GameMovingObject(GameCollidingObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.hard_objects = []
        self.no_collision_mode = False

    def add_hard_object(self, obj: GameCollidingObject):
        self.hard_objects.append(obj)

    def add_hard_objects(self, objs: [GameCollidingObject, ...]):
        self.hard_objects.extend(objs)

    def reset_hard_objects(self):
        self.hard_objects.clear()

    def is_no_collision_mode(self):
        return self.no_collision_mode

    def set_collision_mode(self, no_collision_mode: bool):
        self.no_collision_mode = no_collision_mode

    def move(self, dx, dy):
        if self.is_no_collision_mode():
            MovementController.process_free_move(self, (dx, dy))
        else:
            MovementController.process_safe_move(self, (dx, dy), self.hard_objects.copy())
