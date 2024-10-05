from typing import List, Tuple

WALL, FREE, MARKED = '*', '.', '+'


def read_input() -> Tuple[int, List[List[str]], int, int]:
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    row, col = map(int, input().split())
    return n, maze, row - 1, col - 1


def mark_free_at_maze_by_recursion(row: int, col: int, maze: List[List[str]]):
    if -1 < row < len(maze) and -1 < col < len(maze[0]):
        current = maze[row][col]
        if current == FREE:
            maze[row][col] = MARKED
            # print(*[''.join(row) for row in maze], sep="\n")
            # print()
            mark_free_at_maze_by_recursion(row - 1, col, maze)
            mark_free_at_maze_by_recursion(row + 1, col, maze)
            mark_free_at_maze_by_recursion(row, col - 1, maze)
            mark_free_at_maze_by_recursion(row, col + 1, maze)


def calculate_square(row, col, maze):
    copied_maze = maze.copy()
    mark_free_at_maze_by_recursion(row, col, copied_maze)
    result_square = 0
    for row in maze:
        for sym in row:
            print(sym, end="")
            if sym == MARKED:
                result_square += 1
        print()
    return result_square


def main():
    n, maze, row, col = read_input()
    print(calculate_square(row, col, maze))


if __name__ == '__main__':
    main()


"""
7
*******
*.*.*.*
*.*.*.*
*.*..**
*...*.*
*.*...*
*******
2 2
"""
