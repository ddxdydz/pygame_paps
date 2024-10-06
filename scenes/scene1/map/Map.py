from math import trunc

from basic.game_logic.GameCollidingObject import GameCollidingObject
from basic.game_logic.visualization.GamingDisplayManager import GamingDisplayManager
from scenes.scene1.game_objects.Wall import Wall


class Map:
    def __init__(self, scheme):
        self.scheme = scheme
        self.collision_scheme = []
        self.collision_cells_map = []

    def set_scheme(self, scheme):
        self.scheme = scheme

    @staticmethod
    def get_scheme_coordinates(centre_coordinates):
        x, y = centre_coordinates
        col, row = trunc(x), trunc(y) + 1
        return row, col

    def fill_collision_cells_map(self, collision_scheme):
        self.collision_scheme = collision_scheme
        for row in range(len(collision_scheme)):
            self.collision_cells_map.append([])
            for col in range(len(collision_scheme[row])):
                cell_code = collision_scheme[row][col]
                self.collision_cells_map[row].append(
                    Wall((col, row)) if cell_code == 1 else None
                )

    def get_near_walls(self, coordinates: tuple[int, int], delta_side=2):
        result = []
        y, x = Map.get_scheme_coordinates(coordinates)
        height, width = len(self.collision_scheme), len(self.collision_scheme[0])

        for col in range(y - delta_side, y + delta_side + 1):
            for row in range(x - delta_side, x + delta_side + 1):
                if -1 < row < height and -1 < col < width:
                    obj = self.collision_cells_map[col][row]
                    if isinstance(obj, Wall):
                        result.append(obj)

        return result

    def check_collision(self, obj: GameCollidingObject):
        near_walls = self.get_near_walls(obj.get_centre_coordinates())
        for wall in near_walls:
            if obj.check_collision(wall):
                return True
        return False

    def draw(self, display_manager: GamingDisplayManager):
        for row in range(len(self.scheme)):
            for col in range(len(self.scheme[0])):
                obj_code = self.scheme[row][col]
                img_type = "base"
                display_manager.draw(obj_code, img_type, (col, row))

    def draw_collisions(self, display_manager: GamingDisplayManager):
        for row in self.collision_cells_map:
            for col in row:
                if isinstance(col, Wall):
                    col.draw_collision(display_manager, col.get_code())

    def draw_near_collisions(self, display_manager: GamingDisplayManager, coordinates):
        for wall in self.get_near_walls(coordinates):
            wall.draw_collision(display_manager, wall.get_code())
