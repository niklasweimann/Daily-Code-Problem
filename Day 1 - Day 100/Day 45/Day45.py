import random as ran


def rand5():
    return ran.randrange(1, 5)


def rand7():
    i = 5 * rand5() - rand5() - 5
    if (i > 21):
        rand7()
    return i % 7 + 1


result = [0 for i in range(0, 7)]
for i in range(0, 10000):
    x = rand7()
    result[x-1] += 1

print(result)
