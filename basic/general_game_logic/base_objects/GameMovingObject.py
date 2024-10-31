from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.collision_system.lines_collision.CollisionLines import CollisionLines
from basic.general_game_logic.dynamic.movement_system.MovementController import MovementController


class GameMovingObject(GameCollidingObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.hard_objects = []
        self.moving_borders = CollisionLines(list())
        self.no_collision_mode = False

    def add_hard_object(self, obj: GameCollidingObject):
        self.hard_objects.append(obj)

    def add_hard_objects(self, objs: [GameCollidingObject, ...]):
        self.hard_objects.extend(objs)

    def reset_hard_objects(self):
        self.hard_objects.clear()

    def get_hard_objects(self):
        return self.hard_objects.copy()

    def set_moving_borders(self, moving_borders: CollisionLines):
        self.moving_borders = moving_borders

    def get_moving_borders(self):
        return self.moving_borders

    def is_no_collision_mode(self):
        return self.no_collision_mode

    def set_collision_mode(self, no_collision_mode: bool):
        self.no_collision_mode = no_collision_mode

    def move(self, dx, dy):
        if self.is_no_collision_mode():
            MovementController.process_free_move(self, (dx, dy))
        else:
            MovementController.process_safe_move(
                self, (dx, dy), self.get_hard_objects(), self.get_moving_borders()
            )
