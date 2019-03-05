import math
shortestDistance = math.inf


def shortestPath(maze, start, end, visited, currentDistance):
    global shortestDistance
    (x, y) = start

    if x not in range(0, len(maze)) or y not in range(0, len(maze)):
        return

    if maze[x][y] == True or start in visited:
        return

    if start == end:
        if currentDistance < shortestDistance:
            shortestDistance = currentDistance
            return

    shortestPath(maze, (x-1, y), end,
                 visited+[start], currentDistance+1)
    shortestPath(maze, (x, y-1), end,
                 visited+[start], currentDistance+1)
    shortestPath(maze, (x, y+1), end,
                 visited + [start], currentDistance + 1)
    shortestPath(maze, (x+1, y), end,
                 visited + [start], currentDistance + 1)
    return shortestDistance


maze = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]

start = (3, 0)
end = (0, 0)

print(shortestPath(maze, start, end, [], 0))
