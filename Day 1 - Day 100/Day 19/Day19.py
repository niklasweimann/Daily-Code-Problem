def color(n, k, costmatrix=[[]]):
    if costmatrix is None:
        return 0

    cost = [[0 for i in range(k)] for j in range(n)]
    for j in range(0, len(costmatrix)-2):
        if j == 0:
            cost[0][j] = costmatrix[j][0]
            cost[1][j] = costmatrix[j][1]
            cost[2][j] = costmatrix[j][2]
        else:
            cost[0][j] = min(cost[1][j-1], cost[2][j-1])+costmatrix[j][0]
            cost[1][j] = min(cost[0][j-1], cost[2][j-1])+costmatrix[j][1]
            cost[2][j] = min(cost[0][j-1], cost[1][j-1])+costmatrix[j][2]

    result = min(cost[0][len(costmatrix)-3], cost[1][len(costmatrix)-3])
    return min(result, cost[2][len(costmatrix)-3])


cost_func = [[4, 0, 3], [8, 3, 8], [4, 5, 0], [3, 4, 4], [8, 8, 0]]
print(color(5, 3, cost_func))
