from collections import deque

from scenes.scene1.map.layers_generator.maze.MazeGenerator import MazeGenerator


def bfs(maze, start, end):
    queue = deque([start])  # Create a queue and add the start position
    paths = {start: None}   # Keep track of paths
    width, height = len(maze[0]), len(maze)

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for direction in directions:
            nx, ny = current[0] + direction[0], current[1] + direction[1]
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == 0 and (nx, ny) not in paths:
                queue.append((nx, ny))
                paths[(nx, ny)] = current  # Track the path

    # Reconstruct the path from end to start
    path = []
    while end is not None:
        path.insert(0, end)
        end = paths[end]
    return path


if __name__ == '__main__':
    maze_generator = MazeGenerator()
    maze = maze_generator.get_maze()
    path = bfs(maze, (13, 13), (1, 1))
    for row, col in path:
        maze[row][col] = 2
    for row in maze:
        for col in row:
            if col == 0:
                print(".", end='')
            elif col == 1:
                print("*", end='')
            elif col == 2:
                print("@", end='')
        print()
    print(path)
