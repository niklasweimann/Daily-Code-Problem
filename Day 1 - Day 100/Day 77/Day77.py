def remove_overlapping_intervals(data):
    if data is None or len(data) <= 1:
        return data
    data = sorted(data, key=lambda x: x[0])
    result = []
    top = data[0]
    for i in range(1, len(data)):
        current = data[i]
        if current[0] <= top[1]:
            top = (top[0], max(top[1], current[1]))
        else:
            result.append(top)
            top = current
    result.append(top)
    return result


list1 = [(1, 3), (20, 25), (5, 8), (4, 10)]
print(remove_overlapping_intervals(list1))
