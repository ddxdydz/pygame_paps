from basic.general_game_logic.collisions.rectangle_collision.CollisionChecker import CollisionChecker
from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.dynamic.damage_system.DamageArea import DamageArea


class DamageController:
    @staticmethod
    def is_damaged(damage_area: DamageArea, target_obj: GameCollidingObject):
        if CollisionChecker.check_collision(
                damage_area.get_collision_rect_coordinates(),
                target_obj.get_collision_rect_coordinates()):
            return True
        return False
