array = [10, 5, 2, 7, 8, 7]
k = 3


def max(list, n):
    result = []
    for i in range(0, (len(list)-(n-1))):
        max = 0
        for j in range(i, i + n):
            if (max < list[j]):
                max = list[j]
        result.append(max)
    return result


print(max(array, k))
