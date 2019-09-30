def get_unordered_colums(data):
    res = 0
    for i in range(0, len(data[0])):
        for j in range(0, len(data)-1):
            if data[j][i] > data[j + 1][i]:
                res += 1
                break
    return res


arr1 = [['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']]
print(get_unordered_colums(arr1))  # 1
arr2 = [['a'], ['b'], ['c'], ['d'], ['e'], ['f']]
print(get_unordered_colums(arr2))  # 0
arr3 = [['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']]
print(get_unordered_colums(arr3))  # 3
