from math import inf

from basic.general_game_logic.base_objects.GameMovingObject import GameMovingObject
from basic.general_game_logic.dynamic.damage_system.DamageArea import DamageArea
from basic.general_game_logic.dynamic.damage_system.DamageController import DamageController
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer


class GameDynamicObject(GameMovingObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.damage_processing_objects = []
        self.damage_area = DamageArea(coordinates)
        self.max_health = inf
        self.current_health = inf
        self.shield = 0
        self.damage = 0

    def add_damage_processing_object(self, obj):
        self.damage_processing_objects.append(obj)

    def add_damage_processing_objects(self, objs):
        self.damage_processing_objects.extend(objs)

    def reset_damage_processing_objects(self):
        self.damage_processing_objects.clear()

    def decrease_health(self, damage):
        damage -= self.shield
        if damage < 0:
            damage = 0
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def do_damage(self):
        self.damage_area.set_coordinates(self.get_coordinates())
        for obj in self.damage_processing_objects:
            if DamageController.is_damaged(self.damage_area, obj):
                obj.process_getting_damage(self.damage)

    def process_getting_damage(self, damage):
        self.decrease_health(damage)

    def draw_damage_area_collision(self, display_manager: GameVisualizer):
        self.damage_area.set_coordinates(self.get_coordinates())
        left_upper_x, left_upper_y = self.damage_area.get_collision_rect_coordinates()[0]
        size = self.damage_area.get_collision_rect().get_rect_size()
        display_manager.draw_rect(left_upper_x, left_upper_y, *size, color="red")
