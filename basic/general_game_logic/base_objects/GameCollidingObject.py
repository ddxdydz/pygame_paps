from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRectChecker import CollisionRectChecker
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRect import CollisionRect
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer


class GameCollidingObject(GameObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.collision_rect = CollisionRect(0, 0, self.width, self.height)  # default

    def create_collision_rect(self, x, y, width, height):
        self.collision_rect = CollisionRect(x, y, width, height)

    def set_collision_rect(self, rect: CollisionRect):
        self.collision_rect = rect

    def get_collision_rect(self) -> CollisionRect:
        return self.collision_rect

    def get_collision_rect_coordinates(self):
        return self.collision_rect.get_absolute_coordinates(*self.get_coordinates())

    def check_collision(self, obj):
        if isinstance(obj, GameCollidingObject):
            return CollisionRectChecker.check_collision(
                self.get_collision_rect_coordinates(),
                obj.get_collision_rect_coordinates()
            )

    def get_collided_objects(self, objects):
        result = []
        for obj in objects:
            if self.get_distance_between_centres(obj) < self.get_no_contact_distance(obj):
                if self.check_collision(obj):
                    result.append(obj)
        return result

    def draw_collision(self, game_visualizer: GameVisualizer):
        left_upper_x, left_upper_y = self.get_collision_rect_coordinates()[0]
        size = self.get_collision_rect().get_rect_size()
        game_visualizer.draw_rect(left_upper_x, left_upper_y, *size)
