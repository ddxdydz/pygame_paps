import pygame

from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.collision_system.lines_collision.CollisionLine import CollisionLine
from basic.general_game_logic.collision_system.lines_collision.CollisionLineChecker import CollisionLineChecker
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.game_visualization.support_visualization_components.converting.DrawConverting import \
    DrawConverting


class CollisionLines:
    def __init__(self, lines: list[CollisionLine]):
        self.lines = lines

    def check_collision(self, obj: GameCollidingObject) -> bool:
        rect = obj.get_collision_rect_coordinates()
        for line in self.lines:
            if CollisionLineChecker.check_collision_with_rect(line, rect):
                return True
        return False

    def draw(self, game_visualizer: GameVisualizer, color="blue"):
        for line in self.lines:
            point1 = DrawConverting.main_to_draw_coordinates(
                line.point1, game_visualizer.camera.get_coordinates(), game_visualizer.get_current_tick_size())
            point2 = DrawConverting.main_to_draw_coordinates(
                line.point2, game_visualizer.camera.get_coordinates(), game_visualizer.get_current_tick_size())
            pygame.draw.line(game_visualizer.get_screen(), color, point1, point2,
                             width=int(0.04 * game_visualizer.get_current_tick_size()) + 1)
