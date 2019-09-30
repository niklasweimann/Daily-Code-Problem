given = [10, 15, 3, 7]
k = 25
result = False
given.sort()
for x in given:
    for y in given:
        if x + y == k:
            result = True
print(result)
