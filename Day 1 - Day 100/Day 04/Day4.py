array = [1, 2, 0]
result = 0
array.sort()
for x in range(1, (max(array) + 2)):
    if (x not in array):
        print(x)
        break
