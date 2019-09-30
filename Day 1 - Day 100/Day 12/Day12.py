def getAllCombWrapper():
    steps = [1, 2]
    N = 4
    return getAllComb(0, N, steps)


def getAllComb(x, y, steps):
    if (x > y):
        return 0
    if (x == y):
        return 1
    result = 0
    for i in range(0, len(steps)):
        next = x + steps[i]
        result += getAllComb(next, y, steps)
    return result


print(getAllCombWrapper())
