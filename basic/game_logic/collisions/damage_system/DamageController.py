from basic.game_logic.GameDynamicObject import GameDynamicObject
from basic.game_logic.collisions.damage_system.DamageArea import DamageArea
from basic.game_logic.collisions.rectangle_collision.Collision import Collision


class DamageController:
    @staticmethod
    def process_damage(damage_area: DamageArea, target_obj: GameDynamicObject):
        if Collision.check_collision(
                damage_area.get_collision_rect_coordinates(),
                target_obj.get_collision_rect_coordinates()):
            da_x, da_y = damage_area.get_centre_coordinates()
            obj_x, obj_y = target_obj.get_centre_coordinates()
            distance = damage_area.get_distance_between_centres(target_obj)
            vector = (obj_x - da_x) / distance, (obj_y - da_y) / distance
            damage_impuls = vector[0] * damage_area.impuls, vector[1] * damage_area.impuls
            return True, damage_impuls
        return False, (0, 0)
