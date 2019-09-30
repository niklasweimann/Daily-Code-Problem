def start(board, letter):
    res = []
    for i in range(len(board)):
        for j, v2 in enumerate(board[i]):
            if v2 is letter:
                res.append((i, j))
    return res


def findmatch(mat, pat, x, y,
              nrow, ncol, level, visited):
    l = len(pat)
    if level == l:
        return True

    if x < 0 or y < 0 or x >= nrow or y >= ncol:
        return False

    if (mat[x][y] == pat[level]):
        visited[x][y] = True
        res = False
        if x - 1 >= 0 and visited[x - 1][y] is False:
            res = res | findmatch(mat, pat, x - 1, y, nrow,
                                  ncol, level + 1, visited)
        if x + 1 < len(visited) and visited[x + 1][y] is False:
            res = res | findmatch(mat, pat, x + 1, y, nrow,
                                  ncol, level + 1, visited)
        if y - 1 >= 0 and visited[x][y-1] is False:
            res = res | findmatch(mat, pat, x, y - 1, nrow,
                                  ncol, level + 1, visited)
        if y + 1 < len(visited[0]) and visited[x][y+1] is False:
            res = res | findmatch(mat, pat, x, y + 1, nrow,
                                  ncol, level + 1, visited)
        return res
    else:
        return False


def exists(board, string):
    visited = [[False for i in range(len(board[0]))]
               for j in range(len(board))]
    for i in start(board, string[0]):
        visited[i[0]][i[1]] = True
        if(findmatch(board, string, i[0], i[1],
                     len(board), len(board[0]), 0, visited)):
            return True
    return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print(exists(board, "ABCCED"))  # true
print(exists(board, "SEE"))  # true
print(exists(board, "ABCB"))  # false
