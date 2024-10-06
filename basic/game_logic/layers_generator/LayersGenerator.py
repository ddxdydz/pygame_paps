from random import choice, randint

from basic.game_logic.game_constants import EMPTY_CODE
from basic.game_logic.layers_generator.maze.MazeGenerator import MazeGenerator, WALL, EMPTY


class LayersGenerator:
    floor_codes = ["fw1", "fw2", "fw3"]
    wall_codes = ["ws1", "ws2", "ws3"]
    objects_on_map = ["hr", "ch", "mn", "mn", "mn", "ky", "vs", "vs", "sc"]

    def __init__(self, width=15, height=15, seed=None):
        self.width, self.height = width, height
        self.maze_generator = MazeGenerator(width, height, seed)

    def set_parameters(self, width, height, seed=None):
        self.width, self.height = width, height
        self.maze_generator = MazeGenerator(width, height, seed)

    def replace(self, maze):
        result = []
        for row in range(len(maze)):
            result.append([])
            for col in range(len(maze[0])):
                if maze[row][col] == WALL:
                    result[row].append(choice(self.wall_codes))
                else:
                    result[row].append(choice(self.floor_codes))
        return result

    def get_layers(self):
        maze = self.maze_generator.get_maze()
        layer_0 = self.replace(maze)

        layer_2 = [[EMPTY_CODE] * self.width for _ in range(self.height)]
        free_cells = []
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == EMPTY:
                    free_cells.append((row, col))

        for obj_code in LayersGenerator.objects_on_map:
            row, col = free_cells.pop(randint(0, len(free_cells) - 1))
            layer_2[row][col] = obj_code

        return {
            0: layer_0,
            2: layer_2,
            "collision_map_scheme": [[1 if col == WALL else 0 for col in row] for row in maze]
        }
