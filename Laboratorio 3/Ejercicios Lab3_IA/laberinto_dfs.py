import random

def solve_maze(maze, start, end):
    stack = [start] # [1,0]
    while stack:
        x, y = stack[-1] #Cima de la pila

        # If reached the end point
        if (x, y) == end:
            return True, stack

        # Mark as visited
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    stack.append((nx, ny))
                    break
        else:
            stack.pop()

    return False, []


if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    
    maze = [
        ['1', '1', '1', 'E', '1'],
        ['S', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1']
    ]
        

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                start = (y, x)
            elif maze[y][x] == 'E':
                end = (y, x)

    solved, path = solve_maze(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E': #Si no es S ni E, pone un 
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))#Une a los arreglos y los concatena sin espacios
    else:
        print("No solution found.")
