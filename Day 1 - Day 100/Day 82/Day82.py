def read7(filename, start):
    with open(filename) as f:
        res = []
        for i, line in enumerate(f):
            if i >= start and i <= start + 6:
                res.append(line)
        return res


def readN(filename, n):
    res = []
    index = 0
    while n > index:
        if n - index > 7:
            for i in read7(filename, index):
                res.append(i)
            index += 7
        else:
            for i in read7(filename, index):
                if n > index:
                    res.append(i)
                    index += 1
    return res


filename = "test.txt"
print(readN(filename, 0))
print(readN(filename, 1))
print(readN(filename, 7))
print(readN(filename, 21))
print(readN(filename, 23))
