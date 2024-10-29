from random import choice, randint

from scenes.scene1.general.scene_settings import EMPTY_CODE
from scenes.scene1.map.layers_generator.maze.MazeGenerator import MazeGenerator, WALL, EMPTY


class MazeLayersGenerator:
    def __init__(self, width=15, height=15, seed=None):
        self.width, self.height = width, height
        self.maze_generator = MazeGenerator(width, height, seed)
        # Коды для размещения в лабиринте:
        self.floor_codes = ["fw1", "fw2", "fw3"]
        self.wall_codes = ["ws1", "ws2", "ws3"]
        self.objects_codes = ["hr", "ch", "mn", "mn", "mn", "ky", "vs", "vs", "sc"]

    def set_parameters(self, width, height, seed=None):
        self.width, self.height = width, height
        self.maze_generator = MazeGenerator(width, height, seed)

    def set_floor_codes(self, floor_codes):
        self.floor_codes = floor_codes

    def set_wall_codes(self, wall_codes):
        self.wall_codes = wall_codes

    def set_objects_codes(self, objects_codes):
        self.objects_codes = objects_codes

    def random_maze_replace(self, maze):
        result = []
        for row in range(len(maze)):
            result.append([])
            for col in range(len(maze[0])):
                if maze[row][col] == WALL:
                    result[row].append(choice(self.wall_codes))
                else:
                    result[row].append(choice(self.floor_codes))
        return result

    @staticmethod
    def get_free_cells(maze):
        free_cells = []
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == EMPTY:
                    free_cells.append((row, col))
        return free_cells

    def get_layers(self):
        maze = self.maze_generator.get_maze()
        layer_0 = self.random_maze_replace(maze)

        layer_2 = [[EMPTY_CODE] * self.width for _ in range(self.height)]
        free_cells = self.get_free_cells(maze)
        for obj_code in self.objects_codes:
            row, col = free_cells.pop(randint(0, len(free_cells) - 1))
            layer_2[row][col] = obj_code

        return {
            0: layer_0,
            2: layer_2,
            "collision_map_scheme": [[1 if col == WALL else 0 for col in row] for row in maze]
        }
