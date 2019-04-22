import random as ran


def rand7():
    return ran.randrange(1, 7)


def rand5():
    i = 7 * rand7() - rand7() - 7
    if (i > 49):
        rand5()
    return i % 5 + 1


#
result = [0 for i in range(0, 5)]
for i in range(0, 10000):
    x = rand5()
    result[x-1] += 1

print(result)
