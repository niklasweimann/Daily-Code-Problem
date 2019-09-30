def getWater(input):
    maxHeight = input[0]
    water = 0
    for i in input:
        if maxHeight < i:
            maxHeight = i
            continue
        else:
            water = water + maxHeight - i
    return water


inputMap = [3, 0, 1, 3, 0, 5]
print(getWater(inputMap))  # should be 8

inputMap2 = [2, 1, 2]
print(getWater(inputMap2))  # should be 1
