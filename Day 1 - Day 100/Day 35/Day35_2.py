def sort(list):
    for j in range(0, len(list)):
        if list[j] is 'B':
            x = list.pop(j)
            list.append(x)

    for i in range(0, len(list)):
        if list[i] is 'R':
            x = list.pop(i)
            list = [x] + list

    return list

array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(sort(array))