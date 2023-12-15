from collections import deque
import random
import time

def find_doors(maze):
    start, end = None, None

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                start = (y, x)
            elif maze[y][x] == 'E':
                end = (y, x)

    return start, end

def solve_maze(maze, start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return True, path

        # Mark as visited
        if maze[x][y] != 'S':
            maze[x][y] = '-'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == ' ' or maze[nx][ny] == 'E':
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    if maze[nx][ny] != 'E':
                        maze[nx][ny] = '-'

    return False, []

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def create_maze(rows, cols):
    maze = [[' ' for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                maze[row][col] = '#'
            else:
                if random.random() < 0.40:
                    maze[row][col] = '#'

    return maze

def set_random_door(maze, type_of_door):
    rows = len(maze)
    cols = len(maze[0])

    border = random.choice(['top', 'bottom', 'left', 'right'])

    match border:
        case 'top':
            row, col = 0, random.randint(1, cols - 2)
            maze[row + 1][col] = ' '
        case 'bottom':
            row, col = rows - 1, random.randint(1, cols - 2)
            maze[row - 1][col] = ' '
        case 'left':
            row, col = random.randint(1, rows - 2), 0
            maze[row][col + 1] = ' '
        case 'right':
            row, col = random.randint(1, rows - 2), cols - 1
            maze[row][col - 1] = ' '
        case _:
            raise ValueError('Invalid border')

    if maze[row][col] == 'S' or maze[row][col] == 'E':
        return set_random_door(maze, type_of_door)
    else:
        maze[row][col] = type_of_door

    return maze

if __name__ == '__main__':
    n, m = map(int, input("Enter the size of the maze (n m): ").split())
    start_time = time.time()
    maze = set_random_door(set_random_door(create_maze(n, m), 'S'), 'E')
    maze_copy = [row[:] for row in maze]
    solved, path = solve_maze(maze_copy, *find_doors(maze))

    if solved:
        print("[+] Maze Solved!\n")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '.'
        print_maze(maze)
    else:
        print("[x] No solution found.\n")
        print_maze(maze_copy)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution Time: {elapsed_time:.6f} seconds")
