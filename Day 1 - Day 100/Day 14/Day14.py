import random as random
import math as math


def getPi(accuracy):
    hit = 0
    for i in range(0, accuracy):
        x = random.random() ** 2
        y = random.random() ** 2
        if math.sqrt(x + y) < 1.0:
            hit += 1
    return (float(hit) / accuracy) * 4


print(getPi(500000))
