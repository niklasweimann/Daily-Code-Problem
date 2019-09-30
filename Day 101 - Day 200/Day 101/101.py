def isPrime(number):
    if number < 2:
        return False
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True


def getSoultion(input):
    for i in range(0, input):
        for j in range(0, input):
            if i + j == input and isPrime(i) and isPrime(j):
                return (i, j)


def printSolution(input):
    x = getSoultion(input)
    return "{0} + {1} = {2}".format(x[0], x[1], x[0]+x[1])


print(printSolution(4))  # 2+2=4
print(printSolution(6))  # 3+3=6
print(printSolution(8))  # 3+5=8
