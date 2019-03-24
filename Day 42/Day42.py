def getSubset(data, k):
    d = k
    data.sort()
    data.reverse()
    res = []
    for i in data:
        if i <= d:
            res.append(i)
            d -= i
    return  res if k is sum(res) else None

S = [12, 1, 61, 5, 9, 2]
k = 24
print(getSubset(S, k)) # [12, 9, 2, 1]

S = [12, 1, 61, 5, 9, 2]
k = 2
print(getSubset(S, k)) # [2]

S = [3, 4, 5, 6, 10]
k = 12
print(getSubset(S, k)) # NONE

S = [1,1,1,1,1,1]
k = 2
print(getSubset(S, k)) # [1,1]

S = []
k = 24
print(getSubset(S, k)) # None