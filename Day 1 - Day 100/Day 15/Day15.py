import random


def stream(num):
    for x in range(num):
        yield x


def randomFromString(stream):
    count = 0
    selected = None

    for item in stream:
        count += 1
        if random.random() <= 1.0 / count:
            selected = item

    return selected


print(randomFromString(stream(1000)))
