from basic.general_game_logic.base_objects.GameMovingObject import GameMovingObject
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRect import CollisionRect
from basic.general_game_logic.dynamic.combat_system.DamageExecutor import DamageExecutor
from basic.general_game_logic.dynamic.combat_system.Health import Health
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer


class GameCombatObject(GameMovingObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.damage_executor = DamageExecutor()
        self.health_keeper = Health()

    def set_health_parameters(self, health: float, max_health: float, shield: float = 0):
        self.health_keeper.set_parameters(health, max_health, shield)

    def set_damage_parameters(self, damage_area: CollisionRect, damage: float):
        self.damage_executor.set_parameters(damage_area, damage)

    def set_targets_to_attack(self, objs):
        self.damage_executor.add_targets_to_attack(objs)

    def attack(self):
        self.damage_executor.attack(*self.get_coordinates())

    def take_hit(self, damage):
        self.health_keeper.take_damage(damage)

    def update(self):
        pass

    def draw_damage_area_collision(self, game_visualizer: GameVisualizer):
        x, y = self.damage_executor.damage_area.get_absolute_coordinates(*self.get_coordinates())[0]
        size = self.damage_executor.damage_area.get_rect_size()
        game_visualizer.draw_rect(x, y, *size, color="red")
