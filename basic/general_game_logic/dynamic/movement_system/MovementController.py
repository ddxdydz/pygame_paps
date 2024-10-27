from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_settings import MIN_PROCESSING_MOVE_DELTA


class MovementController:
    @staticmethod
    def is_confirm_movement(
            mover: GameCollidingObject, vector,
            hard_objects: list[GameCollidingObject, ...]):
        puppet = GameCollidingObject(mover.get_coordinates())
        puppet.set_collision_rect(mover.get_collision_rect())
        puppet.add_to_coordinates(*vector)
        for obj in hard_objects:
            if puppet.check_collision(obj):
                return False
        return True

    @staticmethod
    def decrease_delta(delta) -> float:
        abs_decrease = abs(delta) - MIN_PROCESSING_MOVE_DELTA
        if abs_decrease < 0:
            abs_decrease = 0
        sign = -1 if delta < 0 else 1
        return sign * abs_decrease

    @staticmethod
    def get_possible_movement(
            mover: GameCollidingObject, vector,
            hard_objects):
        dx, dy = vector
        while dx != 0:
            if MovementController.is_confirm_movement(mover, (dx, 0), hard_objects):
                break
            dx = MovementController.decrease_delta(dx)
        while dy != 0:
            if MovementController.is_confirm_movement(mover, (dx, dy), hard_objects):
                break
            dy = MovementController.decrease_delta(dy)
        return dx, dy

    @staticmethod
    def process_safe_move(
            mover: GameCollidingObject, vector,
            hard_objects):
        possible_vector = MovementController.get_possible_movement(mover, vector, hard_objects)
        mover.add_to_coordinates(*possible_vector)

    @staticmethod
    def process_free_move(mover: GameCollidingObject, vector):
        mover.add_to_coordinates(*vector)
