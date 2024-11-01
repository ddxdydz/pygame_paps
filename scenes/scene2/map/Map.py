from basic.general_game_logic.collision_system.lines_collision.CollisionLines import CollisionLines
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from scenes.scene2.general.scene_settings import OBJECTS_VISUALISATION, LINE_BORDERS, MAP_SIZE_IN_PX
from basic.tools.loading.load_borders import load_line_border


class Map:
    def __init__(self):
        self.size = self.height, self.width = OBJECTS_VISUALISATION["map_background"]["size"]
        self.collision_scheme = [[1] * self.width for _ in range(self.height)]
        # self.walls = load_rect_border(self.size)
        self.border = CollisionLines(load_line_border(LINE_BORDERS, self.size, MAP_SIZE_IN_PX))

    def draw(self, game_visualizer: GameVisualizer):
        game_visualizer.refresh_screen(refresh_color="#5E7B80")
        game_visualizer.draw_image_by_cameras_area("map_background", "base", (0, self.height - 1))
        # img = game_visualizer.get_image("map_background", "base")
        # game_visualizer.get_screen().blit(img, (100, 100), (800, 800, 4000, 400))

    def draw_collisions(self, game_visualizer: GameVisualizer):
        # for wall in self.walls:
        #     wall.draw_collision(game_visualizer)
        self.border.draw(game_visualizer)
