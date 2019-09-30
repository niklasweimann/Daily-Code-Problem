# this code is just a python version of the C# Solution on
# https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/


def isSafe(x: int, y: int, sol, N: int):
    return x >= 0 and x < N and y >= 0 and y < N and sol[x][y] == -1


def printSolution(sol):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in sol]))


def solveKt(sol, N):
    possible_x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    possible_y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    sol[0][0] = 0

    if not solveKtUtil(0, 0, 1, sol, possible_x_moves, possible_y_moves, N):
        print("Solution does not exist")
        return False
    else:
        printSolution(sol)
    return True


def solveKtUtil(x: int, y: int, movei: int, sol, possible_x_moves: int, possible_y_moves: int, N: int):
    if movei == N * N:
        return True
    for k in range(0, N):
        next_x = x + possible_x_moves[k]
        next_y = y + possible_y_moves[k]
        if (isSafe(next_x, next_y, sol, N)):
            sol[next_x][next_y] = movei
            if solveKtUtil(next_x, next_y, movei + 1, sol, possible_x_moves, possible_y_moves, N):
                return True
            else:
                sol[next_x][next_y] = -1
    return False


    # driver code
size = 8
arr = [[-1 for j in range(0, size)] for i in range(0, size)]
print(solveKt(arr, size))
