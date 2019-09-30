def getItem(data):
    data.sort()
    for i in range(0, len(data) - 1):
        if i is len(data) - 2 and data[i+1] is not data[i]:
            return data[i+1]
        if data[i - 1] is not data[i] and data[i + 1] is not data[i]:
            return data[i]
    return None


array = [6, 1, 3, 3, 3, 6, 6]
print(getItem(array))  # 1
array = [13, 19, 13, 13]
print(getItem(array))  # 19
array = [1, 1, 2]
print(getItem(array))  # 2
array = [2, 1, 2]
print(getItem(array))  # 1
array = [1, 2, 2]
print(getItem(array))  # 1
