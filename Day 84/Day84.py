def find_istlands(grid):
    if grid is None or len(grid) is 0 or len(grid[0]) is 0:
        return 0
    m = len(grid)
    n = len(grid[0])

    count = 0

    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] is 1:
                count += 1
                merge(grid, i, j)
    return count


def merge(grid, i, j):
    m = len(grid)
    n = len(grid[0])

    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] is not 1:
        return

    grid[i][j] = "X"

    merge(grid, i-1, j)
    merge(grid, i+1, j)
    merge(grid, i, j-1)
    merge(grid, i, j+1)


data = [[1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1]]


print(find_istlands(data))
