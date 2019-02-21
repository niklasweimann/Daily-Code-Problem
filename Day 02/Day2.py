given = [3, 2, 1]
result = []
for x in range(0, len(given)):
    result.append(0)
    for y in range(0, len(given)):
        if (y != x):
            if (result[x] == 0):
                result[x] = 1
            result[x] *= given[y]
print(result)
