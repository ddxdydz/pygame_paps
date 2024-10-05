from basic.game_logic.GameObject import GameObject
from basic.game_logic.collisions.rectangle_collision.Collision import Collision
from basic.game_logic.visualization.GamingDisplayManager import GamingDisplayManager


class GameCollidingObject(GameObject):
    def __init__(self, coordinates: tuple, size=(0, 0)):
        super().__init__(coordinates, size)
        self.collision_rect = tuple()  # x, y in image left upper corner, weight, height
        self.collision_rect_points = tuple()  # points in image

    def set_collision_rect(self, x, y, weight, height):
        self.collision_rect = (x, y, weight, height)
        self.collision_rect_points = (
            (x, y),
            (x + weight, y),
            (x + weight, y - height),
            (x, y - height)
        )

    def get_collision_rect(self):
        return self.collision_rect

    def get_collision_rect_points(self):
        return self.collision_rect_points

    def get_collision_rect_coordinates(self):
        x, y = self.get_coordinates()
        rect_coordinates = []
        for rx, ry in self.get_collision_rect_points():
            rect_coordinates.append((rx + x, ry + y))
        return tuple(rect_coordinates)

    def check_collision(self, obj):
        if isinstance(obj, GameCollidingObject):
            return Collision.check_collision(
                self.get_collision_rect_coordinates(),
                obj.get_collision_rect_coordinates()
            )

    def draw_collision(self, display_manager: GamingDisplayManager, code):
        display_manager.draw_collision(
            code, self.get_collision_rect_points(),
            self.get_coordinates()
        )
