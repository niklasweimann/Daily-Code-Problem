def longestSequence(data):
    s = set()
    res = 0
    for i in data:
        s.add(i)
    for i in range(len(data)):
        if (data[i]-1) not in s:
            j = data[i]
            while(j in s):
                j += 1
            res = max(res, j-data[i])
    return res


arr = [100, 4, 200, 1, 3, 2]
print(longestSequence(arr))  # 4
