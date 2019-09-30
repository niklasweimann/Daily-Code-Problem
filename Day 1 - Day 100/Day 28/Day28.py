import math as m


def justifyText(wordList, k):
    listLen = len(wordList)
    # Build cost matrix
    cost = [[0 for x in range(listLen)] for y in range(listLen)]

    for i in range(0, listLen):
        cost[i][i] = k - len(wordList[i])
        for j in range(i+1, listLen):
            cost[i][j] = cost[i][j-1] - len(wordList[j]) - 1

    for i in range(0, listLen):
        for j in range(i, listLen):
            if cost[i][j] < 0:
                cost[i][j] = m.inf
            else:
                cost[i][j] = m.pow(cost[i][j], 2)

    minCost = [0 for y in range(0, listLen)]
    result = [0 for y in range(0, listLen)]

    for i in range(listLen-1, -1, -1):
        minCost[i] = cost[i][listLen-1]
        result[i] = listLen
        for j in range(listLen-1, i, -1):
            if cost[i][j-1] is m.inf:
                continue
            if minCost[i] > minCost[j]+cost[i][j-1]:
                minCost[i] = minCost[j]+cost[i][j-1]
                result[i] = j

    i = 0
    print("Minimum cost is " + str(minCost[0]))
    print("\n")
    builder = []
    while True:
        j = result[i]
        line = []
        for l in range(i, j):
            line.append(wordList[l])

        for p in range(0, len(line)):
            if p is len(line)-1:
                break
            line[p] = line[p] + " "

        spaces = k - len("".join(line))

        for n in range(len(line)):
            s = ""
            for o in range(0, m.ceil(spaces / len(line))):
                s = s + " "
            line[n] = line[n] + s

        builder.append("".join(line))
        builder.append("    " + "# {0} extra space(s)".format(spaces))
        builder.append("\n")
        i = j
        if j >= listLen:
            break
    return "".join(builder)


array = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
print(justifyText(array, k))
