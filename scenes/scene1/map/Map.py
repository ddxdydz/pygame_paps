from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.Scene import Scene
from scenes.scene1.game_objects.Wall import Wall
from scenes.scene1.map.layers_generator.get_scheme_coordinates import get_scheme_coordinates
from scenes.scene1.map.layers_generator.maze.MazeLayersGenerator import MazeLayersGenerator
from scenes.scene1.map.loading_objects.loading_objects import get_objects


class Map:
    def __init__(self, parent_scene: Scene):
        self.parent_scene = parent_scene

        maze_layers_generator = MazeLayersGenerator(width=15, height=15)
        maze_layers_generator.set_floor_codes(["floor_wooden1", "floor_wooden2", "floor_wooden3"])
        maze_layers_generator.set_wall_codes(["wall_stone1", "wall_stone2", "wall_stone3"])
        maze_layers_generator.set_objects_codes(
            ["hero", "chess", "money", "money", "money", "key", "vase", "vase", "sceleton"])
        map_layers = maze_layers_generator.get_layers()

        self.layer0 = map_layers[0]
        self.layer2 = map_layers[2]
        self.collision_scheme = map_layers["collision_map_scheme"]
        self.height, self.width = len(self.collision_scheme), len(self.collision_scheme[0])

        self.walls = self.load_walls()
        self.wall_scheme = self.load_wall_scheme()

        objects_map = get_objects(self.layer2, self.parent_scene)
        self.player = objects_map["heroes"][0]
        self.enemy = objects_map["enemies"][0]
        self.others = objects_map["others"]

    def load_walls(self):
        walls = []
        for row in range(self.height):
            for col in range(self.width):
                is_wall = self.collision_scheme[row][col]
                if is_wall:
                    walls.append(Wall((col, row)))
        return walls

    def load_wall_scheme(self):
        wall_scheme = []
        for row in range(self.height):
            wall_scheme.append([])
            for col in range(self.width):
                is_wall = self.collision_scheme[row][col]
                wall_scheme[row].append(Wall((col, row)) if is_wall else None)
        return wall_scheme

    def get_near_walls(self, coordinates: tuple[int, int], delta_side=2):
        result = []
        y, x = get_scheme_coordinates(coordinates)
        for col in range(y - delta_side, y + delta_side + 1):
            for row in range(x - delta_side, x + delta_side + 1):
                if -1 < row < self.height and -1 < col < self.width:
                    obj = self.wall_scheme[col][row]
                    if isinstance(obj, Wall):
                        result.append(obj)
        return result

    def check_collision(self, obj: GameCollidingObject):
        near_walls = self.get_near_walls(obj.get_centre_coordinates())
        for wall in near_walls:
            if obj.check_collision(wall):
                return True
        return False

    def clear_deleted_objects(self):
        for game_object_index in range(len(self.others) - 1, -1, -1):
            game_object = self.others[game_object_index]
            if game_object.is_deleted():
                self.others.pop(game_object_index)

    def update(self):
        self.clear_deleted_objects()

    def draw(self, game_visualizer: GameVisualizer):
        for row in range(self.height):
            for col in range(self.width):
                game_visualizer.draw_image(self.layer0[row][col], "base", (col, row))

    def draw_collisions(self, game_visualizer: GameVisualizer):
        for cells_row in self.wall_scheme:
            for cell in cells_row:
                if isinstance(cell, Wall):
                    cell.draw_collision(game_visualizer)

    def draw_near_collisions(self, game_visualizer: GameVisualizer, coordinates):
        for wall in self.get_near_walls(coordinates):
            wall.draw_collision(game_visualizer)
