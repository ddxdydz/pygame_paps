import random


# Use these characters for displaying the maze:
EMPTY = '.'
MARK = '+'
WALL = '*'
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'


class MazeGenerator:
    def __init__(self, width=15, height=15, seed=None):
        self.width, self.height = None, None
        self.set_size(width, height)
        self.seed = random.randint(100000, 999999) if seed is None else seed
        self.maze = []
        self.regenerate()

    def set_size(self, width: int, height: int):
        assert width % 2 == 1 and width >= 3
        assert height % 2 == 1 and height >= 3
        self.width, self.height = width, height

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    def set_seed(self, seed: int):
        self.seed = seed

    def get_seed(self):
        return self.seed

    def __visit(self, x, y, has_visited):
        """"Carve out" empty spaces in the maze at x, y and then
        recursively move to neighboring unvisited spaces. This
        function backtracks when the mark has reached a dead end."""
        self.maze[y][x] = EMPTY  # "Carve out" the space at x, y.

        while True:
            # Check which neighboring spaces adjacent to
            # the mark have not been visited already:
            unvisited_neighbors = []
            if y > 1 and (x, y - 2) not in has_visited:
                unvisited_neighbors.append(NORTH)

            if y < self.height - 2 and (x, y + 2) not in has_visited:
                unvisited_neighbors.append(SOUTH)

            if x > 1 and (x - 2, y) not in has_visited:
                unvisited_neighbors.append(WEST)

            if x < self.width - 2 and (x + 2, y) not in has_visited:
                unvisited_neighbors.append(EAST)

            if len(unvisited_neighbors) == 0:
                # BASE CASE
                # All neighboring spaces have been visited, so this is a
                # dead end. Backtrack to an earlier space:
                return
            else:
                # RECURSIVE CASE
                # Randomly pick an unvisited neighbor to visit:
                next_intersection = random.choice(unvisited_neighbors)

                # Move the mark to an unvisited neighboring space:

                next_x, next_y = x, y
                if next_intersection == NORTH:
                    next_x = x
                    next_y = y - 2
                    self.maze[y - 1][x] = EMPTY  # Connecting hallway.
                elif next_intersection == SOUTH:
                    next_x = x
                    next_y = y + 2
                    self.maze[y + 1][x] = EMPTY  # Connecting hallway.
                elif next_intersection == WEST:
                    next_x = x - 2
                    next_y = y
                    self.maze[y][x - 1] = EMPTY  # Connecting hallway.
                elif next_intersection == EAST:
                    next_x = x + 2
                    next_y = y
                    self.maze[y][x + 1] = EMPTY  # Connecting hallway.

                has_visited.append((next_x, next_y))  # Mark as visited.
                self.__visit(next_x, next_y, has_visited)  # Recursively visit this space.

    def regenerate(self, seed=None):
        if seed is not None:
            self.seed = seed
        random.seed(self.seed)

        # Every space is a wall at first.
        self.maze = [[WALL] * self.width for _ in range(self.height)]

        # Start by visiting the top-left corner.
        self.__visit(1, 1, [(1, 1)])

    def get_maze(self):
        return self.maze

    def print_maze(self):
        for row in self.maze:
            for col in row:
                print(col, end='')
            print()


if __name__ == '__main__':
    maze_generator = MazeGenerator()
    maze_generator.print_maze()
