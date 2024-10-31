from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRect import CollisionRect
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRectChecker import CollisionRectChecker
from basic.general_settings import FPS


class DamageExecutor:
    def __init__(self):
        self.targets_to_attack = []
        self.damage_area = CollisionRect(0, 0, 0, 0)  # default
        self.damage = 0

    def set_parameters(self, damage_area: CollisionRect, damage: float):
        if damage < 0:
            raise Exception("GameDynamicObject Error: set damage < 0")
        self.damage_area = damage_area
        self.damage = damage

    def add_target_to_attack(self, obj):
        self.targets_to_attack.append(obj)

    def add_targets_to_attack(self, objs):
        self.targets_to_attack.extend(objs)

    def clear_targets_to_attack(self):
        self.targets_to_attack.clear()

    def _check_damage(self, attacker_x, attacker_y, target_obj: GameCollidingObject):
        if CollisionRectChecker.check_collision(
                self.damage_area.get_absolute_coordinates(attacker_x, attacker_y),
                target_obj.get_collision_rect_coordinates()):
            return True
        return False

    def attack(self, attacker_x, attacker_y):
        for obj in self.targets_to_attack:
            if self._check_damage(attacker_x, attacker_y, obj):
                obj.take_hit(self.damage)
        return True
