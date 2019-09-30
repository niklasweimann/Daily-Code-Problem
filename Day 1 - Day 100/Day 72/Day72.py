# translated from https://www.cnblogs.com/lz87/p/10354361.html
import math


class Graph:
    def __init__(self):
        self.UNVISITED = 0
        self.VISITING = 1
        self.VISITED = 2

    def constructGraph(self, s: str, edges: [[]]):
        graph = {}
        for i in range(0, len(s)):
            graph[i] = []

        for i in edges:
            graph[i[0]].append(i[1])
        return graph

    def maxGraphPath(self, s: str, edges: [[]]):
        graph = self.constructGraph(s, edges)
        if len(graph) < 2:
            return None
        states = [self.UNVISITED for i in range(0, len(s))]
        maxPaths = [[0 for i in range(0, 26)] for j in range(0, len(s))]

        for node in range(0, len(s)):
            if states[node] == self.UNVISITED:
                if self.dfs(s, graph, states, maxPaths, node):
                    return math.inf

        maxPathValue = 0
        for i in range(0, len(s)):
            for j in range(0, 26):
                maxPathValue = max(maxPaths[i][j], maxPathValue)

        return maxPathValue

    def dfs(self, s: str, graph: {}, states: [], maxPaths: [[]], node: int):
        if states[node] is self.VISITED:
            return False
        elif states[node] is self.VISITING:
            return True

        states[node] = self.VISITING
        for neighbor in graph[node]:
            self.dfs(s, graph, states, maxPaths, neighbor)

        for neighbor in graph[node]:
            for letter in range(0, 26):
                maxPaths[node][letter] = max(
                    maxPaths[node][letter], maxPaths[neighbor][letter])

        maxPaths[node][ord(s[node]) - ord('A')] += 1
        states[node] = self.VISITED
        return False


# driver code
g = Graph()
string = "ABACA"
nodes = [(0, 1),
         (0, 2),
         (2, 3),
         (3, 4)]
print(g.maxGraphPath(string, nodes))  # 3

string = "A"
nodes = [(0, 0)]
print(g.maxGraphPath(string, nodes))  # None
