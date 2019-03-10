import math as m
def justifyText(wordList, k):
    listLen = len(wordList)
    # Build cost matrix
    cost = [[0 for x in range(listLen)] for y in range(listLen)]

    for i in range(0, listLen):
        cost[i][i] = k - len(wordList[i])
        for j in range(i+1, listLen):
            cost[i][j] = cost[i][j-1] - len(wordList[j]) -1
    
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
        for k in range(i, j):
            builder.append(wordList[k] + " ")
        builder.append("\n")
        i = j
        if j >= listLen:
            break
    return "".join(builder)


array = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
print(justifyText(array, k))