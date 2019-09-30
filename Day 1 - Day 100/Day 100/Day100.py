def get_steps(data):
    steps = 0
    def distance(p1, p2): return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))
    for i in range(len(data)-1):
        steps += distance(data[i], data[i + 1])
    return steps


arr = [(0, 0), (1, 1), (1, 2)]
print(get_steps(arr))  # 2
arr = [(4, 6), (1, 2), (4, 5), (10, 12)]
print(get_steps(arr))  # 14
