from math import log


def arbitrage(table):
    transformed_graph = [[-log(edge) for edge in row] for row in table]

    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[0] = 0

    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                min_dist[w] = min_dist[v] + transformed_graph[v][w]

    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False


print(arbitrage([[1, 2], [2, 1]]))
print(arbitrage([[1, 1], [1, 1]]))
