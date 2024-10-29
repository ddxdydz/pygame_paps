from basic.general_game_logic.game_visualization.GameVisualizer import GamingDisplayManager
from scenes.scene2.general.scene_settings import OBJECTS_VISUALISATION
from scenes.scene2.map.load_borders import load_borders


class Map:
    def __init__(self):
        self.size = self.height, self.width = OBJECTS_VISUALISATION["map_background"]["size"]
        self.collision_scheme = [[1] * self.width for _ in range(self.height)]
        self.walls = load_borders(self.size)

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw_image("map_fon", "base", (-8, 28))
        display_manager.draw_image("map_background", "base", (0, 24))

    def draw_collisions(self, display_manager: GamingDisplayManager):
        for wall in self.walls:
            wall.draw_collision(display_manager)
