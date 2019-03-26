def getInversions(data):
    res = []
    for index, value in enumerate(data):
        sub_data = data[index:]
        max_sub_data = [(value, x) for x in sub_data if x < value]
        res.extend(max_sub_data)
    return res


# Result: [(2, 1), (4, 1), (4, 3)] => Len = 3
array = [2, 4, 1, 3, 5]
result = getInversions(array)
print("Result: {0} => Len = {1}".format(result, len(result)))
# Result: [(5, 4), (5, 3), (5, 2), (5, 1), (4, 3), (4, 2), (4, 1), (3, 2), (3, 1), (2, 1)] => Len = 10
array = [5, 4, 3, 2, 1]
result = getInversions(array)
print("Result: {0} => Len = {1}".format(result, len(result)))
