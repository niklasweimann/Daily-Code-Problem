from random import choice


def randomNotInList(n, list):
    possible = []
    for i in range(0, int(list[-1])):
        if i not in list:
            possible.append(i)
    return choice(possible)


print(randomNotInList(3, [1, 3, 4, 6, 10]))
