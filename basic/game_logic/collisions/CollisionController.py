from basic.game_logic.GameCollidingObject import GameCollidingObject


class CollisionController:
    @staticmethod
    def confirm_movement(
            mover: GameCollidingObject, vector,
            hard_objects: list[GameCollidingObject, ...]):
        puppet = GameCollidingObject(mover.get_coordinates())
        puppet.set_collision_rect(*mover.get_collision_rect())
        puppet.move(*vector)
        for obj in hard_objects:
            if puppet.check_collision(obj):
                return False
        return True

    @staticmethod
    def get_possible_movement(
            mover: GameCollidingObject, vector,
            hard_objects):
        result = []
        vector_by_x = (vector[0], 0)
        vector_by_y = (0, vector[1])
        if CollisionController.confirm_movement(mover, vector_by_x, hard_objects):
            result.append(vector[0])
        else:
            result.append(0)
        if CollisionController.confirm_movement(mover, vector_by_y, hard_objects):
            result.append(vector[1])
        else:
            result.append(0)
        return tuple(result)

    @staticmethod
    def make_move(mover: GameCollidingObject, vector):
        mover.move(*vector)

    @staticmethod
    def make_safe_move(
            mover: GameCollidingObject, vector,
            hard_objects):
        possible_vector = CollisionController.get_possible_movement(mover, vector, hard_objects)
        mover.move(*possible_vector)
